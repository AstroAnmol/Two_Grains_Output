import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import pandas as pd

## Perpendicular Case

# import parameter data
param_data_H1_a1_th90=pd.read_csv("Data/csv_files/param_data_H1_a1_th90.csv", index_col=0, header=None)
vary_param_data_H1_a1_th90=pd.read_csv("Data/csv_files/param_data_H1_a1_th90_vary.csv", index_col=0, header=None)

# model function
def func(susc, s0, s1, s2, s3, s4, s5):
    return s0 + s1*(susc**1) + s2*(susc**2) + s3*(susc**3) + s4*(susc**4) + s5*(susc**5)    
start_susc=19
end_susc=37

for ind in range(2):
    func_selection=ind # 0 for FDM and 1 for varied
    if func_selection==0:
        data=param_data_H1_a1_th90

        data=data.drop([20,21,22,23,24,25,26,27,28,30], axis=1)
        susc_data=np.array(data.loc['susc', start_susc:end_susc])
        p1=np.array(data.loc['p1', start_susc:end_susc])
        p2=np.array(data.loc['p2', start_susc:end_susc])
        p3=np.array(data.loc['p3', start_susc:end_susc])
        # p4=np.array(data.loc['p4', start_susc:end_susc])
        # p5=np.array(data.loc['p5', start_susc:end_susc])
        # p6=np.array(data.loc['p6', start_susc:end_susc])

        p_data_com=np.array([p1,p2,p3])#,p4,p5,p6])
        tot_param=3
        print(susc_data)

    elif func_selection==1:
        data=vary_param_data_H1_a1_th90

        data=data.drop([20,21,22,23,24,25,26,27,28,30], axis=1)
        susc_data=np.array(data.loc['susc', start_susc:end_susc])
        p0=np.array(data.loc['p0', start_susc:end_susc])
        p1=np.array(data.loc['p1', start_susc:end_susc])
        p2=np.array(data.loc['p2', start_susc:end_susc])
        p3=np.array(data.loc['p3', start_susc:end_susc])
        # p4=np.array(data.loc['p4', start_susc:end_susc])
        # p5=np.array(data.loc['p5', start_susc:end_susc])
        # p6=np.array(data.loc['p6', start_susc:end_susc])

        p_data_com=np.array([p0,p1,p2,p3])#,p4,p5,p6])
        tot_param=4
    

    # effective susceptibility
    susc_eff_data=(3*susc_data)/(susc_data+3)    
    
    i=0
    while i < tot_param:

        p_data=p_data_com[i]

        #Fit for the parameters of the function func using susc
        popt, pcov = curve_fit(func, susc_data, p_data)

        #One standard deviation for parameters
        perr = np.sqrt(np.diag(pcov))
        print('parameters:', popt)
        print('Standard Deviation of Parameters:',perr)

        #Calculate Least Sqaures error
        p_cal=func(susc_data, *popt)
        residuals=p_data-p_cal
        l_sq_err=np.sum(residuals**2)
        squaresum = np.sum((p_data-np.mean(p_data))**2)
        R2 = 1 - (l_sq_err/squaresum)
        print('Least squares error',np.sqrt(l_sq_err))
        print('R^2 value',R2)

        if tot_param==4:
            param_str=["p0", "p1", "p2", "p3"]#, "p4", "p5", "p6"]
            func_str="Varied model fit"
        elif tot_param==3:
            param_str=["p1", "p2", "p3"]#, "p4", "p5", "p6"]
            func_str="FDM model fit"

        # plot
        plt.figure()
        plt.plot(susc_data, p_data, 'b+', label='data')
        plt.plot(susc_data, func(susc_data, *popt), 'r-', label=func_str)
        plt.xlabel('$\chi$')
        plt.ylabel(param_str[i] + ' parameter')
        plt.title(r"a=1 m, H0=1 A/m, $\theta$=90 deg")
        plt.grid('on')
        plt.legend()
        plt.show()
        plt.close()

        i=i+1