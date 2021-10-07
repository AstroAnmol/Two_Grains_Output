import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import pandas as pd

## Polynomial fitting for mag data


# model function F = muo*(Fdm + p1/r^5 + p2/r^6 + p3/r^7)
def func(c, p1, p2, p3):
    mu0=4.0*np.pi*1e-7
    susc_eff=3*susc/(3+susc)
    # F_DM=-8*np.pi*susc_eff**2/(3*c**4) # (parallel case)
    F_DM=4*np.pi*susc_eff**2/(3*c**4) # (perpendicular case)
    return mu0*(F_DM + p1/(c**5) + p2/(c**6) + p3/(c**7))

# #model function F = mu0*(p0/r^ + p1/r^5 + p2/r^6 + p3/r^7)
# def func(c, p0, p1, p2, p3):
#     mu0=4.0*np.pi*1e-7
#     return mu0*(p0/(c**4) + p1/(c**5) + p2/(c**6) + p3/(c**7))

#import the data
data_H1_a1_th0=pd.read_csv('Data/data_H1_a1_th0.csv')
data_H1_a1_th90=pd.read_csv('Data/data_H1_a1_th90.csv')

data=data_H1_a1_th90
# data=data_H1_a1_th0

susc_data=np.array([0.25,	0.5,	0.75,	1,	1.5,	2,	2.5,	3,	3.5,	4,	4.5,	5,	5.5,	6,	6.5,	7,	7.5,	8])
c_data=data['c']    


for ind in range(18):
    susc_strings=np.array(['0.25','0.5','0.75','1.0','1.5','2.0','2.5','3.0','3.5','4.0','4.5','5.0','5.5','6.0','6.5','7.0','7.5','8.0'])
    susc=susc_data[ind]
    fz_data=data[susc_strings[ind]]

    #Fit for the parameters of the function func:
    popt, pcov = curve_fit(func, c_data, fz_data)
    
    #One standard deviation for parameters
    perr = np.sqrt(np.diag(pcov))
    print('Susceptibilty:'+susc_strings[ind])
    print('Optimised parameters',popt)
    print('Standard Deviation of Parameters:',perr)

    # plt.plot(c_data, func(c_data, popt[0]+perr[0],popt[1]-perr[1],popt[2]+perr[2],popt[3]-perr[3]), 'r--')
    # plt.plot(c_data, func(c_data, popt[0]-perr[0],popt[1]+perr[1],popt[2]-perr[2],popt[3]+perr[3]), 'r--')

    #Calculate Least Sqaures error
    fz_cal=func(c_data, *popt)
    residuals=fz_data-fz_cal
    l_sq_err=np.sum(residuals**2)
    squaresum = np.sum((fz_data-np.mean(fz_data))**2)
    R2 = 1 - (l_sq_err/squaresum)
    print('Least squares error',l_sq_err)
    print('R^2 value',R2)
    print()

    # plot
    plt.figure()
    plt.plot(c_data, fz_data, 'b+', label='data')
    plt.plot(c_data, func(c_data, *popt), 'r-',\
        # label='model fit: p0=%5.3f, p1=%5.3f, p2=%5.3f, p3=%5.3f' % tuple(popt))
        label='model fit: p1=%5.3f, p2=%5.3f, p3=%5.3f' % tuple(popt))
    plt.xlabel('c')
    plt.ylabel('fz (N)')
    plt.title(r"a=1 m, H0=1 A/m, $\theta$=90, $\chi=$"+susc_strings[ind])
    plt.grid('on')
    plt.legend()
    susc_strings=np.array(['0,25','0,50','0,75','1,0','1,5','2,0','2,5','3,0','3,5','4,0','4,5','5,0','5,5','6,0','6,5','7,0','7,5','8,0'])
    plt.savefig('Plots/Fitting/Perpendicular_Case/a_1_H0_1_th_90_chi_'+susc_strings[ind]+'.png')
    # plt.savefig('Plots/Fitting/Parallel_Case/a_1_H0_1_th_0_chi_'+susc_strings[ind]+'.png')