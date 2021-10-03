import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import pandas as pd


#import the data
data_H1_a1_th0=pd.read_csv('Data/extra_data_H1_a1_th0.csv')
#create mesh arrays
c_data=data_H1_a1_th0['c']
susc_data=np.array([0.1,	0.15,	0.2,	8.5,	9,	    9.5,	10, 	10.5,	11,     11.5,	12])
c_c, susc_susc = np.meshgrid(c_data, susc_data)
susc_susc=np.reshape(susc_susc,11*12)
c_c=np.reshape(c_c,11*12)
susc_strings=np.array(['0.1','0.15','0.2','8.5','9.0','9.5','10.0','10.5','11.0','11.5','12.0'])
fz_data=data_H1_a1_th0['0.1']
for ind in range(10):
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


#Check model fit
print('Check Model Fit for extrapolation')
params=np.array([-56.47485756,  282.0725787,  -365.87755112,    5.25623737,    5.37819318,  5.43538851])
print('fitted parameters', params)

modelPredictions = func((c_c,susc_susc), *params) 

absError = modelPredictions - fz_data

SE = np.square(absError) # squared errors
MSE = np.mean(SE) # mean squared errors
RMSE = np.sqrt(MSE) # Root Mean Squared Error, RMSE
Rsquared = 1.0 - (np.var(absError) / np.var(fz_data))
print('RMSE:', RMSE)
print('R-squared:', Rsquared, '\n')