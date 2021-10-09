# Perpendicular Case

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import pandas as pd


#import the data
data_H1_a1_th90=pd.read_csv('Data/extra_data_H1_a1_th90.csv')
#create mesh arrays
c_data=data_H1_a1_th90['c']
susc_data=np.array([0.1,	0.15,	0.2,	8.5,	9,	    9.5,	10, 	10.5,	11,     11.5,	12])
c_c, susc_susc = np.meshgrid(c_data, susc_data)
susc_susc=np.reshape(susc_susc,11*12)
c_c=np.reshape(c_c,11*12)
susc_strings=np.array(['0.1','0.15','0.2','8.5','9.0','9.5','10.0','10.5','11.0','11.5','12.0'])
fz_data=data_H1_a1_th90['0.1']
for ind in range(10):
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

#Parameters
    #original
params=np.array([2.1679403, -5.10571752, 0.91979498, -0.14520514, -11.99291281, 32.60814942, -8.5414691, 1.26892871, \
    12.57083862, -53.1809105, 17.62267505, -2.66077834]) 

#Check model fit
print('Check Model Fit for extrapolation')

print('fitted parameters', params)

modelPredictions = func((c_c,susc_susc), *params) 

absError = modelPredictions - fz_data

SE = np.square(absError) # squared errors
MSE = np.mean(SE) # mean squared errors
RMSE = np.sqrt(MSE) # Root Mean Squared Error, RMSE
Rsquared = 1.0 - (np.var(absError) / np.var(fz_data))
print('RMSE:', RMSE)
print('R-squared:', Rsquared, '\n')