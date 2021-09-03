# Trial for the scipy curve fit function 
# for a=1 m, H0=1, theta=0, susc=1
import matplotlib.pyplot as plt
import matplotlib
# matplotlib.rcParams['text.usetex'] = True
from scipy.optimize import curve_fit
import numpy as np

# define model function
def func(c, p1, p2, p3):
    mu0=4.0*np.pi*1e-7
    susc=1
    susc_eff=3*susc/(3+susc)
    F_DM=-8*np.pi*susc_eff**2/(3*c**4)
    return mu0*(F_DM + p1/(c**5) + p2/(c**6) + p3/(c**6))

# Define the data 
c_data = np.linspace(2,4.2,12)
fz_data=np.array([-5.57E-07,	-3.17E-07,	-2.07E-07,	-1.43E-07,	-1.04E-07,	-7.73E-08,	-5.90E-08,	-4.59E-08,	-3.63E-08,	-2.91E-08,	-2.36E-08,	-1.93E-08])
plt.plot(c_data, fz_data, 'b+', label='data')

#Fit for the parameters a, b, c of the function func:
popt, pcov = curve_fit(func, c_data, fz_data)
plt.plot(c_data, func(c_data, *popt), 'r-',\
    label='model fit: p1=%5.3f, p2=%5.3f, p3=%5.3f' % tuple(popt))

plt.xlabel('c')
plt.ylabel('fz (N)')
plt.title(r"a=1 m, H0=1 A/m, $\theta$=0, $\chi=1$")
plt.grid('on')
plt.legend()
plt.show()