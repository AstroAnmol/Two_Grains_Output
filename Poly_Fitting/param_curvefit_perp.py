import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import pandas as pd
import sys

## Perpendicular Case

# import parameter data
param_data_H1_a1_th90=pd.read_csv("Data/csv_files/param_data_H1_a1_th90.csv", index_col=0, header=None)
vary_param_data_H1_a1_th90=pd.read_csv("Data/csv_files/param_data_H1_a1_th90_vary.csv", index_col=0, header=None)

# model function
def func(susc, s0, s1, s2, s3):#, s4, s5):
    return s0 + s1*(susc**1) + s2*(susc**2) + s3*(susc**3)# + s4*(susc**4) + s5*(susc**5)    
start_susc=19
end_susc=37

file_path = 'Results_txt/param_fitting_results_th90.txt'
sys.stdout = open(file_path, "w")

print("####################################################")
print("Parameter Fitting Theta=90 deg case (Perpendicular)")
print("####################################################")
print("####################################################")
print()
print()


for ind in range(2):
    func_selection=ind # 0 for FDM and 1 for varied
    if func_selection==0:
        data=param_data_H1_a1_th90

        data=data.drop([20,21,22,23,24,25,26,27,28,30], axis=1)
        susc_data=np.array(data.loc['susc', start_susc:end_susc])
        p1=np.array(data.loc['p1', start_susc:end_susc])
        p2=np.array(data.loc['p2', start_susc:end_susc])
        p3=np.array(data.loc['p3', start_susc:end_susc])

        p_data_com=np.array([p1,p2,p3])
        tot_param=3
        print("####################################################")
        print("susceptibility data considered")
        print(susc_data)
        print("####################################################")
        print()
        print()
        print("FDM FUNCTION")
        print("####################################################")


    elif func_selection==1:
        data=vary_param_data_H1_a1_th90

        data=data.drop([20,21,22,23,24,25,26,27,28,30], axis=1)
        susc_data=np.array(data.loc['susc', start_susc:end_susc])
        p0=np.array(data.loc['p0', start_susc:end_susc])
        p1=np.array(data.loc['p1', start_susc:end_susc])
        p2=np.array(data.loc['p2', start_susc:end_susc])
        p3=np.array(data.loc['p3', start_susc:end_susc])

        p_data_com=np.array([p0,p1,p2,p3])
        tot_param=4

        print()
        print()
        print("VARIED FUNCTION")
        print("####################################################")
    

    # effective susceptibility
    susc_eff_data=(3*susc_data)/(susc_data+3)    
    
    for j in range(2):
        
        if j==0:
            print()
            print()
            print("Susceptibility based")
            print("#####################################################")
        if j==1:
            susc_data=susc_eff_data
            print()
            print()
            print("Effective Susceptibility based")
            print("#####################################################")

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

            if ind==1:
                param_str=["p0", "p1", "p2", "p3"]
                func_str="Varied model fit"
            elif ind==0:
                param_str=["p1", "p2", "p3"]
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
            # plt.show()
            if ind==0:
                if j==0:
                    plt.savefig("Plots/Fitting/Perpendicular_Case/Cubic_Poly/Parameters/a_1_H0_1_th_90_" + param_str[i] + ".png", bbox_inches='tight')
                elif j==1:
                    plt.savefig("Plots/Fitting/Perpendicular_Case/Cubic_Poly/Parameters/a_1_H0_1_th_90_" + param_str[i] + "_susceff.png", bbox_inches='tight')
            elif ind==1:
                if j==0:
                    plt.savefig("Plots/Fitting/Perpendicular_Case/Cubic_Poly/Parameters/vary_a_1_H0_1_th_90_" + param_str[i] + ".png", bbox_inches='tight')
                elif j==1:
                    plt.savefig("Plots/Fitting/Perpendicular_Case/Cubic_Poly/Parameters/vary_a_1_H0_1_th_90_" + param_str[i] + "_susceff.png", bbox_inches='tight')
            plt.close()

            i=i+1