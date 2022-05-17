import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import pandas as pd
import sys

## Data
susc=np.array([0.1,0.15,0.2,0.25,0.5,0.75,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0,9.5,10.0,10.5,11.0,11.5,12.0,15.0,20.0,25.0,30.0,35.0,40.0,45.0,50.0,55.0,60.0,65.0,70.0,75.0,80.0,85.0,90.0,95.0,100.0])
data=np.array([-6.44e-09,-1.44e-08,-2.53e-08,-3.92e-08,-1.51e-07,-3.26e-07,-5.57e-07,-1.17e-06,-1.97e-06,-2.91e-06,-3.98e-06,-5.17e-06,-6.46e-06,-7.84e-06,-9.3e-06,-1.08e-05,-1.24e-05,-1.41e-05,-1.58e-05,-1.76e-05,-1.94e-05,-2.18e-05,-2.38e-05,-2.59e-05,-2.8e-05,-3.01e-05,-3.23e-05,-3.45e-05,-3.67e-05,-5.22e-05,-7.99e-05,-0.000109,-0.000138,-0.000173,-0.000203,-0.000233,-0.000263,-0.000335,-0.000373,-0.000409,-0.000446,-0.000493,-0.000529,-0.000564,-0.000599,-0.000633,-0.000666])

# susc data from 7.5 only considered
susc=np.delete(susc, [20,21,22,23,24,26,27,28])
data=np.delete(data, [20,21,22,23,24,26,27,28])
susc=susc[19:]
data=data[19:]
print(susc)

def func(x, a, b, c, d):#, p4, p5, p6):
    # return (c*susc + d)/(a*susc+d)
    return a*x**3 + b*x**2 + c*x + d


#Fit for the parameters of the function func:
popt, pcov = curve_fit(func, susc, data)

#Calculate Least Sqaures error
fz_cal=func(susc, *popt)
print("Calculated force")
# print(np.array(fz_cal))
residuals=data-fz_cal
l_sq_err=np.sum(residuals**2)
squaresum = np.sum((data-np.mean(data))**2)
R2 = 1 - (l_sq_err/squaresum)
print('Least squares error',np.sqrt(l_sq_err))
print('R^2 value',R2)
print()

#One standard deviation for parameters
perr = np.sqrt(np.diag(pcov))
# print('Susceptibilty:'+susc_strings[ind])
print('Optimised parameters',popt)
print('Standard Deviation of Parameters:',perr)

plt.plot(susc,data , '+')
plt.plot(susc, func(susc, *popt), 'r-', label='FDM based model fit')
plt.show()