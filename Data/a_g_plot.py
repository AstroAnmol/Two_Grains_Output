import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True

fz_th0_data=np.array([-9.30E-06,-2.80E-05,-5.22E-05,-7.99E-05,-1.09E-04,-1.38E-04,-1.73E-04,-2.03E-04,-2.33E-04,-2.63E-04,-3.35E-04,-3.73E-04,-4.09E-04,-4.46E-04,-4.93E-04,-5.29E-04,-5.64E-04,-5.99E-04,-6.33E-04,-6.66E-04])
susc_data=np.arange(5.0,100.0,5.0)
g_data=np.array([1.0e-8,  1.0e-7,   1.0e-6,     1.0e-5,     1.0e-4,     1.0e-3,     1.0e-2,     1.0e-1, 1.0])


## function for bond number = 1
def func(g, i):
    B=500*(1.0e-9)    #tesla
    rho=4000            #Kg/m^3
    mu0=4.0*np.pi*1.0e-7
    chi=susc_data[i]
    H=B/(mu0*(1+chi))
    ans=3*(H**2)*fz_th0_data[i]/(4*np.pi*rho)
    return -ans/(g*9.81)

# def func_self(g):
#     return (g*9.81)/(1.0e-6)
#     S=1
#     return np.sqrt((2.5*1e-6)*(S**2)/(g))

print(susc_data[7],susc_data[11],susc_data[15])
print(fz_th0_data[7],fz_th0_data[11],fz_th0_data[15])
plt.figure()
plt.loglog(g_data,func(g_data,0), '--', label='$\chi=5.0$')
plt.loglog(g_data,func(g_data,1), '--', label='$\chi=10.0$')
plt.loglog(g_data,func(g_data, 3), '--', label='$\chi=20.0$')
plt.loglog(g_data,func(g_data, 7), '--', label='$\chi=40.0$')
#plt.loglog(g_data,func(g_data,11), '--', label='$\chi=60.0$')
plt.loglog(g_data,func(g_data,15), '--', label='$\chi=80.0$')

# plt.loglog(g_data,func_self(g_data), label='self gravity radius')

# plt.ylim(1.0e-6,1)
plt.xlim(1.0e-8,1)
plt.legend()
plt.yticks(rotation=90)
# plt.title("")
plt.xlabel('Ambient Gravitational Acceleration (Earth Gs)')
plt.ylabel('Particle Radius (meters)')
plt.grid(True)
plt.show()