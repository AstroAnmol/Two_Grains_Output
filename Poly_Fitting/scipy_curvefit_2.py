import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import pandas as pd


#import the data
data_H1_a1_th0=pd.read_csv('Data/data_H1_a1_th0.csv')
#create mesh arrays
c_data=data_H1_a1_th0['c']
susc_data=np.array([0.25,	0.5,	0.75,	1,	1.5,	2,	2.5,	3,	3.5,	4,	4.5,	5,	5.5,	6,	6.5,	7,	7.5,	8])
c_c, susc_susc = np.meshgrid(c_data, susc_data)
susc_susc=np.reshape(susc_susc,18*12)
c_c=np.reshape(c_c,18*12)
susc_strings=np.array(['0.25','0.5','0.75','1.0','1.5','2.0','2.5','3.0','3.5','4.0','4.5','5.0','5.5','6.0','6.5','7.0','7.5','8.0'])
fz_data=data_H1_a1_th0['0.25']
for ind in range(17):
    fz_data=np.append(fz_data,data_H1_a1_th0[susc_strings[ind+1]])



## Polynomial fitting for mag data

# model function F = muo*(Fdm + p1/r^5 + p2/r^6 + p3/r^7)
def func(data, a0, b0, c0, a1, b1, c1):
    c=data[0]
    susc=data[1]
    mu0=4.0*np.pi*1e-7
    susc_eff=3*susc/(3+susc)
    p1=a0*(susc_eff**a1)
    p2=b0*(susc_eff**b1)
    p3=c0*(susc_eff**c1)
    F_DM=-8*np.pi*susc_eff**2/(3*c**4)
    return mu0*(F_DM + p1/(c**5) + p2/(c**6) + p3/(c**7))

# #model function F = mu0*(p0/r^ + p1/r^5 + p2/r^6 + p3/r^7)
# def func(c, p0, p1, p2, p3):
#     mu0=4.0*np.pi*1e-7
#     return mu0*(p0/(c**4) + p1/(c**5) + p2/(c**6) + p3/(c**7))

# plt.plot(c_data, fz_data, 'b+', label='data')

#Fit for the parameters of the function func:
print('fit using complete model function')
popt, pcov = curve_fit(func, (c_c,susc_susc), fz_data)

print('fitted parameters', popt)

modelPredictions = func((c_c,susc_susc), *popt) 

absError = modelPredictions - fz_data

SE = np.square(absError) # squared errors
MSE = np.mean(SE) # mean squared errors
RMSE = np.sqrt(MSE) # Root Mean Squared Error, RMSE
Rsquared = 1.0 - (np.var(absError) / np.var(fz_data))
print('RMSE:', RMSE)
print('R-squared:', Rsquared)


#Check earlier model fit
print('fit using parameters separately')
params=np.array([-24.754,	140.732, 	-205.165,    6.394,	    6.337,  	6.233])
print('fitted parameters', params)

modelPredictions = func((c_c,susc_susc), *params) 

absError = modelPredictions - fz_data

SE = np.square(absError) # squared errors
MSE = np.mean(SE) # mean squared errors
RMSE = np.sqrt(MSE) # Root Mean Squared Error, RMSE
Rsquared = 1.0 - (np.var(absError) / np.var(fz_data))
print('RMSE:', RMSE)
print('R-squared:', Rsquared)

#Fit for the parameters of the function func with initial guess as params:
print('fit using complete model function with inital guess')
popt, pcov = curve_fit(func, (c_c,susc_susc), fz_data, p0=params)

print('fitted parameters', popt)

modelPredictions = func((c_c,susc_susc), *popt) 

absError = modelPredictions - fz_data

SE = np.square(absError) # squared errors
MSE = np.mean(SE) # mean squared errors
RMSE = np.sqrt(MSE) # Root Mean Squared Error, RMSE
Rsquared = 1.0 - (np.var(absError) / np.var(fz_data))
print('RMSE:', RMSE)
print('R-squared:', Rsquared)
