import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import pandas as pd

# Define the data 
susc_data = np.array([0.25,	0.5,	0.75,	1,	1.5,	2,	2.5,	3,	3.5,	4,	4.5,	5,	5.5,	6,	6.5,	7,	7.5,	8])
#p1 data for og model function
p1_data_og=np.array([-0.20975847,	-2.27347337,	-7.34617136,	-17.25318627,	-56.57848704,	-133.5033841,	-244.3826337,	-394.1402912,	-580.6618104,	-807.5131773,	-1068.359831,	-1359.106099,	-1672.833852,	-2024.138745,	-2418.810497,	-2815.438018,	-3256.573484,	-3697.922279])
#p2 data for og model function
p2_data_og=np.array([1.29361179,	13.2402318,	42.60166485,	98.93280559,	320.7904955,	748.1109369,	1361.145555,	2184.896802,	3208.044282,	4447.113412,	5868.397083,	7450.118922,	9156.26101,	11062.38345,	13199.89479,	15347.4229,	17729.39342,	20116.79765])
#p3 data for og model function
p3_data_og=np.array([-2.17080118,	-20.44229752,	-64.85237766,	-147.7634726,	-466.9827876,	-1065.257346,	-1914.44905,	-3044.337474,	-4439.946273,	-6117.778379,	-8034.780029,	-10162.59307,	-12452.7227,	-15003.65583,	-17854.86063,	-20719.24773,	-23885.13414,	-27062.06183])

#p0 data for varied model function
p0_data_vary=np.array([-0.3382302,	0.1350877,	2.36650932,	8.98902017,	39.16419506,	106.0719205,	206.9568714,	349.5641676,	526.8857616,	753.5218663,	1013.474442,	1308.666076,	1624.499411,	1985.267583,	2391.083798,	2807.670988,	3276.575598,	3737.775746])
#p1 data for varied model function
p1_data_vary=np.array([-1.04226084,	-15.18631123,	-48.86931314,	-122.9535287,	-423.3423466,	-1044.867835,	-1961.142354,	-3236.29002,	-4814.001846,	-6810.533794,	-9096.268017,	-11682.10129,	-14448.6662,	-17598.12202,	-21137.2718,	-24760.39884,	-28830.67928,	-32840.87378])
#p2 data for varied model function
p2_data_vary=np.array([3.38689108,	45.70881835,	147.0092135,	364.7102345,	1242.997077,	3039.684418,	5677.839069,	9331.318683,	13852.53433,	19541.36302,	26054.10975,	33406.69579,	41280.35657,	50222.26842,	60266.38731,	70526.76246,	82034.00975,	93395.07068])
#p3 data for varied model function
p3_data_vary=np.array([-3.8913934,	-47.13018195,	-150.6712238,	-366.2219364,	-1224.99985,	-2948.839519,	-5462.599223,	-8918.411658,	-13189.29334,	-18524.65032,	-24626.63172,	 -31497.86542625,	-38857.45031,	-47191.52210606,	-56541.64244,	-66074.46654,	-76740.96749,	-87293.88327])

# effective susceptibility
susc_eff_data=(3*susc_data)/(susc_data+3)

# #Power law
# def func(susc, a, b ):
#     return a*(susc**b)

#Cubic model
def func(susc, a, b, c, d):
    return a*(susc**3) + b*(susc**2) + c*(susc) + d

p_data=p1_data_og

#Fit for the parameters of the function func:
popt, pcov = curve_fit(func, susc_eff_data, p_data)

#One standard deviation for parameters
perr = np.sqrt(np.diag(pcov))
print('parameters:', popt)
print('Standard Deviation of Parameters:',perr)

#Calculate Least Sqaures error
p_cal=func(susc_eff_data, *popt)
residuals=p_data-p_cal
l_sq_err=np.sum(residuals**2)
squaresum = np.sum((p_data-np.mean(p_data))**2)
R2 = 1 - (l_sq_err/squaresum)
print('Least squares error',l_sq_err)
print('R^2 value',R2)

# plot
plt.plot(susc_eff_data, p_data, 'b+', label='data')
plt.plot(susc_eff_data, func(susc_eff_data, *popt), 'r-',\
    # label='model fit: a=%5.4f, b=%5.4f' % tuple(popt))
    label='model fit: a=%5.4f, b=%5.4f, c=%5.4f, d=%5.4f' % tuple(popt))
# plt.xlabel('$\chi$')
plt.xlabel('$\chi_{eff}$ (effective susceptibility)')
plt.ylabel('p1 parameter')
plt.title(r"a=1 m, H0=1 A/m, $\theta$=0")
plt.grid('on')
plt.legend()
plt.show()