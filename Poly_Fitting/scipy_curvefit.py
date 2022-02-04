from unittest import case
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import pandas as pd
import sys

## Polynomial fitting for mag data

case_selection=0 ## 0 for parallel and 1 for perpendicular

#import the data
data_H1_a1_th0=pd.read_csv('Data/csv_files/data_H1_a1_th0.csv')
data_H1_a1_th90=pd.read_csv('Data/csv_files/data_H1_a1_th90.csv')

# data=data_H1_a1_th90
# data=data_H1_a1_th0
if case_selection==0:
    file_path = 'Results_txt/fitting_results_th00.txt'
    sys.stdout = open(file_path, "w")
    
    data=data_H1_a1_th0
    print("####################################################")
    print("Theta=0 deg case (Parallel)")
    print("####################################################")
    
elif case_selection==1:
    file_path = 'Results_txt/fitting_results_th90.txt'
    sys.stdout = open(file_path, "w")
    
    data=data_H1_a1_th90
    print("####################################################")
    print("Theta=90 deg case (Perpendicular)")
    print("####################################################")

c_data=data['c']

if case_selection==0:
    susc_data=np.array([0.1, 0.15, 0.2, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, \
        7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0, 70.0, 75.0, 80.0, 85.0, 90.0, 95.0, 100.0])
    tot_ind=susc_data.size
elif case_selection==1:
    susc_data=np.array([0.1, 0.15, 0.2, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, \
        8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 15.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0])
    tot_ind=susc_data.size

for i in range(2):
    func_selection=i
    if func_selection==0:
        print("Fitting for FDM based function")
        print()
        print()
        # model function F = muo*(Fdm + p1/r^5 + p2/r^6 + p3/r^7)
        def func(c, p1, p2, p3):
            mu0=4.0*np.pi*1e-7
            susc_eff=3*susc/(3+susc)
            # F_DM=-8*np.pi*susc_eff**2/(3*c**4) # (parallel case)
            F_DM=4*np.pi*susc_eff**2/(3*c**4) # (perpendicular case)
            return mu0*(F_DM + p1/(c**5) + p2/(c**6) + p3/(c**7))
    
    elif func_selection==1:
        print("Fitting for varied based function")
        print()
        print()
        #model function F = mu0*(p0/r^ + p1/r^5 + p2/r^6 + p3/r^7)
        def func(c, p0, p1, p2, p3):
            mu0=4.0*np.pi*1e-7
            return mu0*(p0/(c**4) + p1/(c**5) + p2/(c**6) + p3/(c**7))
    
    if func_selection==0:
        complete_param_data=np.zeros((tot_ind,8))
    elif func_selection==1:
        complete_param_data=np.zeros((tot_ind,10))

    for ind in range(tot_ind):
        if case_selection==0:
            susc_strings=np.array(['0.1','0.15','0.2','0.25','0.5','0.75','1.0','1.5','2.0','2.5','3.0','3.5','4.0','4.5','5.0','5.5','6.0','6.5','7.0',\
                '7.5','8.0','8.5','9.0','9.5','10.0','10.5','11.0','11.5','12.0','15.0','20.0','25.0','30.0','35.0','40.0','45.0','50.0','55.0','60.0','65.0','70.0','75.0','80.0','85.0','90.0','95.0','100.0'])
        elif case_selection==1:
            susc_strings=np.array(['0.1','0.15','0.2','0.25','0.5','0.75','1.0','1.5','2.0','2.5','3.0','3.5','4.0','4.5','5.0','5.5','6.0','6.5','7.0','7.5','8.0',\
                '8.5','9.0','9.5','10.0','10.5','11.0','11.5','12.0','15.0','20.0','30.0','40.0','50.0','60.0','70.0','80.0','90.0','100.0'])
        susc=susc_data[ind]
        fz_data=data[susc_strings[ind]]

        #Fit for the parameters of the function func:
        popt, pcov = curve_fit(func, c_data, fz_data)

        #One standard deviation for parameters
        perr = np.sqrt(np.diag(pcov))
        print('Susceptibilty:'+susc_strings[ind])
        print('Optimised parameters',popt)
        print('Standard Deviation of Parameters:',perr)

        #Calculate Least Sqaures error
        fz_cal=func(c_data, *popt)
        print("Calculated force")
        print(np.array(fz_cal))
        residuals=fz_data-fz_cal
        l_sq_err=np.sum(residuals**2)
        squaresum = np.sum((fz_data-np.mean(fz_data))**2)
        R2 = 1 - (l_sq_err/squaresum)
        print('Least squares error',np.sqrt(l_sq_err))
        print('R^2 value',R2)
        print()

        param_data=np.append(popt, perr)
        param_data=np.append(param_data,np.sqrt(l_sq_err))
        param_data=np.append(param_data,R2)

        complete_param_data[ind]=param_data

        # plot
        plt.figure()
        plt.plot(c_data, fz_data, 'b+', label='data')
        if func_selection==0:
            plt.plot(c_data, func(c_data, *popt), 'r-', label='FDM based model fit')
        elif func_selection==1:
            plt.plot(c_data, func(c_data, *popt), 'r-', label='Varied model fit')
        
        # if func_selection==0:
        #     plt.plot(c_data, func(c_data, popt[0]+perr[0],popt[1]-perr[1],popt[2]+perr[2]), 'r--')
        #     plt.plot(c_data, func(c_data, popt[0]-perr[0],popt[1]+perr[1],popt[2]-perr[2]), 'r--')
        # elif func_selection==1:
        #     plt.plot(c_data, func(c_data, popt[0]+perr[0],popt[1]-perr[1],popt[2]+perr[2],popt[3]-perr[3]), 'r--')
        #     plt.plot(c_data, func(c_data, popt[0]-perr[0],popt[1]+perr[1],popt[2]-perr[2],popt[3]+perr[3]), 'r--')

        plt.xlabel('c')
        plt.ylabel('fz (N)')
        plt.title(r"a=1 m, H0=1 A/m, $\theta$=90, $\chi=$"+susc_strings[ind])
        plt.grid('on')
        plt.legend()
        
        if case_selection==0:
            susc_strings=np.array(['0,10','0,15','0,20','0,25','0,50','0,75','1,0','1,5','2,0','2,5','3,0','3,5','4,0','4,5','5,0','5,5','6,0','6,5','7,0',\
                '7,5','8,0','8,5','9,0','9,5','10,0','10,5','11,0','11,5','12,0','15,0','20,0','25,0','30,0','35,0','40,0','45,0','50,0','55,0','60,0','65,0','70,0','75,0','80,0','85,0','90,0','95,0','100,0'])
            if func_selection==0:
                plt.savefig('Plots/Fitting/Parallel_Case/a_1_H0_1_th_0_chi_'+susc_strings[ind]+'.png', bbox_inches='tight')
            elif func_selection==1:
                plt.savefig('Plots/Fitting/Parallel_Case/vary_a_1_H0_1_th_0_chi_'+susc_strings[ind]+'.png', bbox_inches='tight')
        elif case_selection==1:
            susc_strings=np.array(['0,10','0,15','0,20','0,25','0,50','0,75','1,0','1,5','2,0','2,5','3,0','3,5','4,0','4,5','5,0','5,5','6,0','6,5','7,0','7,5','8,0',\
                '8,5','9,0','9,5','10,0','10,5','11,0','11,5','12,0','15,0','20,0','30,0','40,0','50,0','60,0','70,0','80,0','90,0','100,0'])
            if func_selection==0:
                plt.savefig('Plots/Fitting/Perpendicular_Case/a_1_H0_1_th_90_chi_'+susc_strings[ind]+'.png', bbox_inches='tight')
            elif func_selection==1:
                plt.savefig('Plots/Fitting/Perpendicular_Case/vary_a_1_H0_1_th_90_chi_'+susc_strings[ind]+'.png', bbox_inches='tight')
    
        plt.close()
    
    if case_selection==0:
        if func_selection==0:
            param_data_H1_a1_th0=pd.DataFrame(complete_param_data.transpose(),columns=['0.1','0.15','0.2','0.25','0.5','0.75','1.0','1.5','2.0','2.5','3.0','3.5','4.0','4.5','5.0','5.5','6.0','6.5','7.0',\
                '7.5','8.0','8.5','9.0','9.5','10.0','10.5','11.0','11.5','12.0','15.0','20.0','25.0','30.0','35.0','40.0','45.0','50.0','55.0','60.0','65.0','70.0','75.0','80.0','85.0','90.0','95.0','100.0'])
            param_data_H1_a1_th0['Parameters']=['p1','p2','p3','std p1','std p2','std p3','least sq err','R2']
            param_data_H1_a1_th0.set_index('Parameters', inplace=True)
            param_data_H1_a1_th0.to_csv('Data/csv_files/param_data_H1_a1_th0.csv')
        elif func_selection==1:
            param_data_H1_a1_th0=pd.DataFrame(complete_param_data.transpose(),columns=['0.1','0.15','0.2','0.25','0.5','0.75','1.0','1.5','2.0','2.5','3.0','3.5','4.0','4.5','5.0','5.5','6.0','6.5','7.0',\
                '7.5','8.0','8.5','9.0','9.5','10.0','10.5','11.0','11.5','12.0','15.0','20.0','25.0','30.0','35.0','40.0','45.0','50.0','55.0','60.0','65.0','70.0','75.0','80.0','85.0','90.0','95.0','100.0'])
            param_data_H1_a1_th0['Parameters']=['p0','p1','p2','p3','std p0','std p1','std p2','std p3','least sq err','R2']
            param_data_H1_a1_th0.set_index('Parameters', inplace=True)
            param_data_H1_a1_th0.to_csv('Data/csv_files/param_data_H1_a1_th0_vary.csv')

    elif case_selection==1:
        if func_selection==0:
            param_data_H1_a1_th90=pd.DataFrame(complete_param_data.transpose(),columns=['0.1','0.15','0.2','0.25','0.5','0.75','1.0','1.5','2.0','2.5','3.0','3.5','4.0','4.5','5.0','5.5','6.0','6.5','7.0','7.5','8.0',\
                '8.5','9.0','9.5','10.0','10.5','11.0','11.5','12.0','15.0','20.0','30.0','40.0','50.0','60.0','70.0','80.0','90.0','100.0'])
            param_data_H1_a1_th90['Parameters']=['p1','p2','p3','std p1','std p2','std p3','least sq err','R2']
            param_data_H1_a1_th90.set_index('Parameters', inplace=True)
            param_data_H1_a1_th90.to_csv('Data/csv_files/param_data_H1_a1_th90.csv')
        elif func_selection==1:
            param_data_H1_a1_th90=pd.DataFrame(complete_param_data.transpose(),columns=['0.1','0.15','0.2','0.25','0.5','0.75','1.0','1.5','2.0','2.5','3.0','3.5','4.0','4.5','5.0','5.5','6.0','6.5','7.0','7.5','8.0',\
                '8.5','9.0','9.5','10.0','10.5','11.0','11.5','12.0','15.0','20.0','30.0','40.0','50.0','60.0','70.0','80.0','90.0','100.0'])
            param_data_H1_a1_th90['Parameters']=['p0','p1','p2','p3','std p0','std p1','std p2','std p3','least sq err','R2']
            param_data_H1_a1_th90.set_index('Parameters', inplace=True)
            param_data_H1_a1_th90.to_csv('Data/csv_files/param_data_H1_a1_th90_vary.csv')