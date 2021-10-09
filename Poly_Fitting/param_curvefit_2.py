import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import pandas as pd

## Perpendicular Case

# Define the data 
susc_data = np.array([0.25,	0.5,	0.75,	1,	1.5,	2,	2.5,	3,	3.5,	4,	4.5,	5,	5.5,	6,	6.5,	7,	7.5,	8])
#p1 data for og model function
p1_data_og=np.array([-0.17999811,	-0.52059341,	-1.03793375,	-1.29247659,	-2.19097308,	-2.74844985,	-2.38517937,	-3.26331726,	-3.11407228,	-3.04015003,	-1.90261958,	-2.09066605,	-1.70764812,	-1.27413566,	-0.85913386,	-0.61678646,	-0.33460259,	-0.12452357])
#p2 data for og model function
p2_data_og=np.array([0.83169057,	2.6918324,	5.72875866,	7.61549648,	13.49146314,	17.67385832,	17.32272396,	22.78958443,	23.46630538,	23.82708076,	19.14421771,	21.00650941,	19.87487047,	18.30531041,	16.50653898,	15.90405396,	14.96980574,	14.0731785])
#p3 data for og model function
p3_data_og=np.array([-1.06815579,	-4.01651512,	-9.18156295,	-13.53289384,	-25.75806534,	-36.75920156,	-42.51232199,	-54.97446328,	-61.84990563,	-67.49202097,	-66.97205511,	-74.08792611,	-77.14226277,	-79.33847019,	-80.68651029,	-83.57685415,	-85.68965691,	-87.52551049])

#p0 data for varied model function
p0_data_vary=np.array([0.13809788,	0.75088642,	1.65229327,	2.03761427,	3.76907733,	5.75720748,	6.04708705,	8.01338806,	8.30515826,	9.40932421,	9.35434871,	10.99572601,	10.44885843,	10.30139829,	10.38077524,	11.29429727,	10.33674547,	11.51252748])
#p1 data for varied model function
p1_data_vary=np.array([0.47553721,	-0.37800356,	-2.15136673,	1.16522969,	1.04692694,	-0.6296448,	11.05347449,	7.62493282,	17.1393721,	19.33662353,	30.63219678,	26.68841869,	39.45105453,	48.51379788,	55.20903941,	54.76039164,	68.30577078,	64.88998054])
#p2 data for varied model function
p2_data_vary=np.array([-0.8166152,	2.33329838,	8.52842143,	1.43573535,	5.34995007,	12.34624919,	-16.46800041,	-4.58828975,	-27.45981017,	-32.43802684,	-62.66261453,	-51.35684159,	-83.61630178,	-106.8835739,	-124.4736358,	-123.3386799,	-157.6227021,	-149.4021802])
#p3 data for varied model function
p3_data_vary=np.array([0.28668588,	-3.72181441,	-11.482774,	-8.45337618,	-19.0660659,	-32.38012192,	-14.73769022,	-32.47094368,	-19.99066986,	-21.24434429,	0.26983701,	-14.60813424,	7.92334807,	23.56180104,	35.19356565,	30.87513302,	56.17467855,	46.84481547])

# effective susceptibility
susc_eff_data=(3*susc_data)/(susc_data+3)

#model function F = mu0*(p0/r^ + p1/r^5 + p2/r^6 + p3/r^7)
def func(susc, a, b, c, d):
    return a*(susc**3) + b*(susc**2) + c*(susc) + d

p_data=p3_data_og

#Fit for the parameters of the function func:
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
print('Least squares error',l_sq_err)
print('R^2 value',R2)

# plot
plt.plot(susc_data, p_data, 'b+', label='data')
plt.plot(susc_data, func(susc_data, *popt), 'r-',\
    label='model fit: a=%5.4f, b=%5.4f, c=%5.4f, d=%5.4f' % tuple(popt))
plt.xlabel('$\chi$')
plt.ylabel('p3 parameter')
plt.title(r"a=1 m, H0=1 A/m, $\theta$=90")
plt.grid('on')
plt.legend()
plt.show()