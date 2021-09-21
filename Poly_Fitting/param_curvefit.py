import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import pandas as pd

# Define the data 
susc_data = np.array([0.25,	0.5,	0.75,	1,	1.5,	2,	2.5,	3,	3.5,	4,	4.5,	5,	5.5,	6,	6.5,	7,	7.5,	8])
#p1 data for og model function
p1_data_og=np.array([-0.21,	-2.273,	-7.346,	-17.253,	-56.578,	-133.503,	-244.383,	-394.14,	-580.662,	-807.513,	-1068.36,	-1359.106,	-1672.834,	-2024.139,	-2418.81,	-2815.438,	-3256.573,	-3697.922])
#p2 data for og model function
p2_data_og=np.array([1.294,	13.24,	42.602,	98.933,	320.79,	748.111,	1361.146,	2184.897,	3208.044,	4447.113,	5868.397,	7450.119,	9156.261,	11062.383,	13199.895,	15347.423,	17729.393,	20116.798])
#p3 data for og model function
p3_data_og=np.array([-2.171,	-20.442,	-64.852,	-147.763,	-466.983,	-1065.257,	-1914.449,	-3044.337,	-4439.946,	-6117.778,	-8034.78,	-10162.593,	-12452.723,	-15003.656,	-17854.861,	-20719.248,	-23885.134,	-27062.062])

#p0 data for varied model function
p0_data_vary=np.array([-0.338,	0.135,	2.367,	8.989,	39.164,	106.072,	206.957,	349.564,	526.886,	753.522,	1013.474,	1308.666,	1624.499,	1985.268,	2391.084,	2807.671,	3276.576,	3737.776])
#p1 data for varied model function
p1_data_vary=np.array([-1.042,	-15.186,	-48.869,	-122.954,	-423.342,	-1044.868,	-1961.142,	-3236.29,	-4814.002,	-6810.534,	-9096.268,	-11682.101,	-14448.666,	-17598.122,	-21137.272,	-24760.399,	-28830.679,	-32840.874])
#p2 data for varied model function
p2_data_vary=np.array([3.387,	45.709,	147.009,	364.71,	1242.997,	3039.684,	5677.839,	9331.319,	13852.534,	19541.363,	26054.11,	33406.696,	41280.357,	50222.268,	60266.387,	70526.762,	82034.01,	93395.071])
#p3 data for varied model function
p3_data_vary=np.array([-3.891,	-47.13,	-150.671,	-366.222,	-1225,	-2948.84,	-5462.599,	-8918.412,	-13189.293,	-18524.65,	-24626.632,	-31497.865,	-38857.45,	-47191.522,	-56541.642,	-66074.467,	-76740.967,	-87293.883])

# effective susceptibility
susc_eff_data=(3*susc_data)/(susc_data+3)

#model function F = mu0*(p0/r^ + p1/r^5 + p2/r^6 + p3/r^7)
def func(susc, a, b ):
    return a*(susc**b)

p_data=p2_data_og

#Fit for the parameters of the function func:
popt, pcov = curve_fit(func, susc_data, p_data)

#One standard deviation for parameters
perr = np.sqrt(np.diag(pcov))
print('Standard Deviation of Parameters:',perr)

#Calculate Least Sqaures error
p_cal=func(susc_data, *popt)
residuals=p_data-p_cal
l_sq_err=np.sum(residuals**2)
squaresum = np.sum((p_data-np.mean(p_data))**2)
R2 = 1 - (l_sq_err/squaresum)
print('Least squares error',l_sq_err)
print('R^2 value',R2)

# plot
plt.plot(susc_data, p_data, 'b+', label='data')
plt.plot(susc_data, func(susc_data, *popt), 'r-',\
    label='model fit: a=%5.4f, b=%5.4f' % tuple(popt))
plt.xlabel('$\chi_{eff}$ (effective susceptibility)')
plt.ylabel('p0 parameter')
plt.title(r"a=1 m, H0=1 A/m, $\theta$=0 (varied)")
plt.grid('on')
plt.legend()
plt.show()