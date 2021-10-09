## Perpendicular case

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import pandas as pd


#import the data
data_H1_a1_th90=pd.read_csv('Data/data_H1_a1_th90.csv')
#create mesh arrays
c_data=data_H1_a1_th90['c']
susc_data=np.array([0.25,	0.5,	0.75,	1,	1.5,	2,	2.5,	3,	3.5,	4,	4.5,	5,	5.5,	6,	6.5,	7,	7.5,	8])
c_c, susc_susc = np.meshgrid(c_data, susc_data)
susc_susc=np.reshape(susc_susc,18*12)
c_c=np.reshape(c_c,18*12)
susc_strings=np.array(['0.25','0.5','0.75','1.0','1.5','2.0','2.5','3.0','3.5','4.0','4.5','5.0','5.5','6.0','6.5','7.0','7.5','8.0'])
fz_data=data_H1_a1_th90['0.25']
for ind in range(17):
    fz_data=np.append(fz_data,data_H1_a1_th90[susc_strings[ind+1]])


## Effective Suscpetibility based

# model function F = muo*(Fdm + p1/r^5 + p2/r^6 + p3/r^7)
def func(data, a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3):
    c=data[0]
    susc=data[1]
    mu0=4.0*np.pi*1e-7
    susc_eff=3*susc/(3+susc)
    p1=a1*(susc_eff**3) + b1*(susc_eff**2) + c1*(susc_eff) + d1
    p2=a2*(susc_eff**3) + b2*(susc_eff**2) + c2*(susc_eff) + d2
    p3=a3*(susc_eff**3) + b3*(susc_eff**2) + c3*(susc_eff) + d3
    F_DM=4*np.pi*susc_eff**2/(3*c**4)
    return mu0*(F_DM + p1/(c**5) + p2/(c**6) + p3/(c**7))

# model function F = muo*(po/r^4 + p1/r^5 + p2/r^6 + p3/r^7)
def func_vary(data, a0, b0, c0, d0, a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3):
    c=data[0]
    susc=data[1]
    mu0=4.0*np.pi*1e-7
    susc_eff=3*susc/(3+susc)
    p0=a0*(susc_eff**3) + b0*(susc_eff**2) + c0*(susc_eff) + d0
    p1=a1*(susc_eff**3) + b1*(susc_eff**2) + c1*(susc_eff) + d1
    p2=a2*(susc_eff**3) + b2*(susc_eff**2) + c2*(susc_eff) + d2
    p3=a3*(susc_eff**3) + b3*(susc_eff**2) + c3*(susc_eff) + d3
    return mu0*(p0/(c**4) + p1/(c**5) + p2/(c**6) + p3/(c**7))

#Parameters
    #original
params=np.array([2.1679403, -5.10571752, 0.91979498, -0.14520514, -11.99291281, 32.60814942, -8.5414691, 1.26892871, \
    12.57083862, -53.1809105, 17.62267505, -2.66077834]) 
    #varied
params_vary=np.array([-2.35006285, 8.70658619, -2.96749461, 0.51760021, 20.29772718, -39.95880704, 23.81296509, -4.13832093, \
    -57.57941163, 120.244874, -66.10561194, 11.3095235, 50.04124488, -125.2151948, 64.93845222, -10.91382394])


#Fit for the parameters of the function func:
print('Fit using complete model function')
popt, pcov = curve_fit(func, (c_c,susc_susc), fz_data)

print('fitted parameters', popt)

modelPredictions = func((c_c,susc_susc), *popt) 

absError = modelPredictions - fz_data

SE = np.square(absError) # squared errors
MSE = np.mean(SE) # mean squared errors
RMSE = np.sqrt(MSE) # Root Mean Squared Error, RMSE
Rsquared = 1.0 - (np.var(absError) / np.var(fz_data))
print('RMSE:', RMSE)
print('R-squared:', Rsquared, '\n') 


#Check earlier model fit
print('Fit using parameters separately')
print('fitted parameters', params)

modelPredictions = func((c_c,susc_susc), *params) 

absError = modelPredictions - fz_data

SE = np.square(absError) # squared errors
MSE = np.mean(SE) # mean squared errors
RMSE = np.sqrt(MSE) # Root Mean Squared Error, RMSE
Rsquared = 1.0 - (np.var(absError) / np.var(fz_data))
print('RMSE:', RMSE)
print('R-squared:', Rsquared, '\n')

#Fit for the parameters of the function func with initial guess as params:
print('Fit using complete model function with initial guess')
popt, pcov = curve_fit(func, (c_c,susc_susc), fz_data, p0=params)

print('fitted parameters', popt)

modelPredictions = func((c_c,susc_susc), *popt) 

absError = modelPredictions - fz_data

SE = np.square(absError) # squared errors
MSE = np.mean(SE) # mean squared errors
RMSE = np.sqrt(MSE) # Root Mean Squared Error, RMSE
Rsquared = 1.0 - (np.var(absError) / np.var(fz_data))
print('RMSE:', RMSE)
print('R-squared:', Rsquared, '\n')

#Check Stability of the fitted parameters
print('Check stability of fitted parameters (1% more)')
params=popt + popt*0.01
print('Parameters', params)

modelPredictions = func((c_c,susc_susc), *params) 

absError = modelPredictions - fz_data

SE = np.square(absError) # squared errors
MSE = np.mean(SE) # mean squared errors
RMSE = np.sqrt(MSE) # Root Mean Squared Error, RMSE
Rsquared = 1.0 - (np.var(absError) / np.var(fz_data))
print('RMSE:', RMSE)
print('R-squared:', Rsquared, '\n')

#Check Stability of the fitted parameters
print('Check stability of fitted parameters (1% less)')
params=popt - popt*0.01
print('Parameters', params)

modelPredictions = func((c_c,susc_susc), *params) 

absError = modelPredictions - fz_data

SE = np.square(absError) # squared errors
MSE = np.mean(SE) # mean squared errors
RMSE = np.sqrt(MSE) # Root Mean Squared Error, RMSE
Rsquared = 1.0 - (np.var(absError) / np.var(fz_data))
print('RMSE:', RMSE)
print('R-squared:', Rsquared, '\n')

#Check Stability of the fitted parameters
print('Check stability of fitted parameters (5% more)')
params=popt + popt*0.05
print('Parameters', params)

modelPredictions = func((c_c,susc_susc), *params) 

absError = modelPredictions - fz_data

SE = np.square(absError) # squared errors
MSE = np.mean(SE) # mean squared errors
RMSE = np.sqrt(MSE) # Root Mean Squared Error, RMSE
Rsquared = 1.0 - (np.var(absError) / np.var(fz_data))
print('RMSE:', RMSE)
print('R-squared:', Rsquared, '\n')


#Check Stability of the fitted parameters
print('Check stability of fitted parameters (5% less)')
params=popt - popt*0.05
print('Parameters', params)

modelPredictions = func((c_c,susc_susc), *params) 

absError = modelPredictions - fz_data

SE = np.square(absError) # squared errors
MSE = np.mean(SE) # mean squared errors
RMSE = np.sqrt(MSE) # Root Mean Squared Error, RMSE
Rsquared = 1.0 - (np.var(absError) / np.var(fz_data))
print('RMSE:', RMSE)
print('R-squared:', Rsquared, '\n')

#Check stability of the fitted parameter
for i in range(100):
    # Generate random parameters around the popt parameters
    print('Check stability around the fitted parameters (5%)', i+1, 'th run')
    rand_set=np.random.uniform(-0.05,0.05, 12)
    print('Random set', rand_set)
    params=popt+ np.multiply(popt,rand_set)
    print('Parameters', params)

    modelPredictions = func((c_c,susc_susc), *params) 

    absError = modelPredictions - fz_data

    SE = np.square(absError) # squared errors
    MSE = np.mean(SE) # mean squared errors
    RMSE = np.sqrt(MSE) # Root Mean Squared Error, RMSE
    Rsquared = 1.0 - (np.var(absError) / np.var(fz_data))
    print('RMSE:', RMSE)
    print('R-squared:', Rsquared, '\n')