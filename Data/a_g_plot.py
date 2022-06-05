import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tikzplotlib as tpl

plt.rcParams['text.usetex'] = True

fz_th0_data=np.array([-9.30E-06,-2.80E-05,-5.22E-05,-7.99E-05,-1.09E-04,-1.38E-04,-1.73E-04,-2.03E-04,-2.33E-04,-2.63E-04,-3.35E-04,-3.73E-04,-4.09E-04,-4.46E-04,-4.93E-04,-5.29E-04,-5.64E-04,-5.99E-04,-6.33E-04,-6.66E-04])
fz_th90_data=np.array([7.60E-07, 1.07E-06, 1.23E-06, 1.32E-06, 1.41E-06, 1.47E-06, 1.50E-06, 1.52E-06, 1.54E-06, 1.55E-06, 1.55E-06, 1.56E-06, 1.56E-06])
susc_data_th0=np.arange(5.0,100.0,5.0)
susc_data_th90=np.array([5.0,	10.0,	15.0,	20.0,	30.0,	40.0,	50.0,	60.0,	70.0,	75.0,	80.0,	85.0,	90.0,	100.0])
g_data=np.array([1.0e-8,  1.0e-7,   1.0e-6,     1.0e-5,     1.0e-4,     1.0e-3,     1.0e-2,     1.0e-1, 1.0])


## Parallel
def func_th0(g, i):
    B=5.0e-5   #tesla
    rho=5000            #Kg/m^3
    mu0=4.0*np.pi*1.0e-7
    chi=susc_data_th0[i]
    H=B/(mu0)#*(1+chi))
    ans=3*(H**2)*fz_th0_data[i]/(4*np.pi*rho)
    return -ans/(g*9.81)


def func_mag_th0(g, mag):
    # mag=mag*(1.0e-9)
    rho=5000
    mu0=4.0*np.pi*1.0e-7
    chi=40.0
    H=mag/(mu0)#*(1+chi))
    ans=3*(H**2)*(-0.000203331052979)/(4*np.pi*rho)
    return (-ans/(g*9.81))


def func_rho_th0(g, rho):
    mag=5.0e-5
    # rho=5000
    mu0=4.0*np.pi*1.0e-7
    chi=40.0
    H=mag/(mu0)#*(1+chi))
    ans=3*(H**2)*(-0.000203331052979)/(4*np.pi*rho)
    return (-ans/(g*9.81))

## Perpendicular 
def func_th90(g, i):
    B=5.0e-5   #tesla
    rho=5000            #Kg/m^3
    mu0=4.0*np.pi*1.0e-7
    chi=susc_data_th90[i]
    H=B/(mu0)#*(1+chi))
    ans=3*(H**2)*fz_th90_data[i]/(4*np.pi*rho)
    return ans/(g*9.81)


def func_mag_th90(g, mag):
    # mag=mag*(1.0e-9)
    rho=5000
    mu0=4.0*np.pi*1.0e-7
    chi=40.0
    H=mag/(mu0)#*(1+chi))
    ans=3*(H**2)*(0.00000146631384643516)/(4*np.pi*rho)
    return (ans/(g*9.81))


def func_rho_th90(g, rho):
    mag=5.0e-5
    # rho=5000
    mu0=4.0*np.pi*1.0e-7
    chi=40.0
    H=mag/(mu0)#*(1+chi))
    ans=3*(H**2)*(0.00000146631384643516)/(4*np.pi*rho)
    return (ans/(g*9.81))

# def func_self(g):
#     return (g*9.81)/(1.0e-6)

# def func_vand(g):
#     S=0.01
#     return np.sqrt((2.5*1e-6)*(S**2)/(g*9.81))
    
# print(susc_data_th90[0],susc_data_th90[1],susc_data_th90[3],susc_data_th90[5],susc_data_th90[10])
# print(fz_th0_data[7],fz_th0_data[11],fz_th0_data[15])
plt.figure()
# plt.loglog(g_data,func_th0(g_data,0), '--', label='$\chi=5.0$')
# plt.loglog(g_data,func_th0(g_data,1), '--', label='$\chi=10.0$')
# plt.loglog(g_data,func_th0(g_data, 3), '--', label='$\chi=20.0$')
# plt.loglog(g_data,func_th0(g_data, 7), '--', label='$\chi=40.0$')
# #plt.loglog(g_data,func(g_data,11), '--', label='$\chi=60.0$')
# plt.loglog(g_data,func_th0(g_data,15), '--', label='$\chi=80.0$')

plt.loglog(g_data,func_th90(g_data,0), '--', label='$\chi=5.0$')
plt.loglog(g_data,func_th90(g_data,1), '--', label='$\chi=10.0$')
plt.loglog(g_data,func_th90(g_data, 3), '--', label='$\chi=20.0$')
plt.loglog(g_data,func_th90(g_data, 5), '--', label='$\chi=40.0$')
#plt.loglog(g_data,func(g_data,11), '--', label='$\chi=60.0$')
plt.loglog(g_data,func_th90(g_data,10), '--', label='$\chi=80.0$')


plt.axvline(x = 0.144/9.81 , color = 'b', linestyle='-.')#, label = '')
plt.annotate(xy=[0.2/9.81, 1.2e-6], text='Psyche')
# plt.loglog(g_data,func_self(g_data), label='self gravity radius')
# plt.loglog(g_data,func_vand(g_data), label='VDW for S=0.01')

# plt.ylim(1.0e-6,1)
plt.xlim(1.0e-8,1)
plt.legend(loc=3)
plt.yticks(rotation=90)
plt.title(r"$B_0=5 \times 10^{-5}$ T and $\rho= 5\ g\ cm^{-3}$")
plt.xlabel('Ambient Gravitational Acceleration (Earth Gs)')
plt.ylabel('Particle Radius (meters)')
plt.grid(True)
# plt.show()

# plt.figure()
# plt.loglog(g_data,func_mag_th0(g_data,5e-7), '--', label=r'$B_0=5 \times 10^{-7}$ T')
# plt.loglog(g_data,func_mag_th0(g_data,5e-6), '--', label=r'$B_0=5 \times 10^{-6}$ T')
# plt.loglog(g_data,func_mag_th0(g_data,5e-5), '--', label=r'$B_0=5 \times 10^{-5}$ T')
# plt.loglog(g_data,func_mag_th0(g_data,5e-4), '--', label=r'$B_0=5 \times 10^{-4}$ T')
# plt.loglog(g_data,func_mag_th0(g_data,5e-3), '--', label=r'$B_0=5 \times 10^{-3}$ T')

# plt.loglog(g_data,func_mag_th90(g_data,5e-7), '--', label=r'$B_0=5 \times 10^{-7}$ T')
# plt.loglog(g_data,func_mag_th90(g_data,5e-6), '--', label=r'$B_0=5 \times 10^{-6}$ T')
# plt.loglog(g_data,func_mag_th90(g_data,5e-5), '--', label=r'$B_0=5 \times 10^{-5}$ T')
# plt.loglog(g_data,func_mag_th90(g_data,5e-4), '--', label=r'$B_0=5 \times 10^{-4}$ T')
# plt.loglog(g_data,func_mag_th90(g_data,5e-3), '--', label=r'$B_0=5 \times 10^{-3}$ T')

# plt.axvline(x = 0.144/9.81 , color = 'b', linestyle='-.')#, label = '')
# plt.annotate(xy=[0.2/9.81, 3e-7], text='Psyche')

# plt.xlim(1.0e-8,1)
# plt.ylim(1.0e-8,1)
# plt.legend()
# plt.yticks(rotation=90)
# plt.title(r"$\chi=40.0$ and $\rho= 5\ g\ cm^{-3}$")
# plt.xlabel('Ambient Gravitational Acceleration (Earth Gs)')
# plt.ylabel('Particle Radius (meters)')
# plt.grid(True)
# plt.show()

# plt.figure()
# plt.loglog(g_data,func_rho_th0(g_data,1000), '--', label=r'$\rho= 1\ g\ cm^{-3}$')
# plt.loglog(g_data,func_rho_th0(g_data,3000), '--', label=r'$\rho= 3\ g\ cm^{-3}$')
# plt.loglog(g_data,func_rho_th0(g_data,5000), '--', label=r'$\rho= 5\ g\ cm^{-3}$')
# plt.loglog(g_data,func_rho_th0(g_data,7000), '--', label=r'$\rho= 7\ g\ cm^{-3}$')
# plt.loglog(g_data,func_rho_th0(g_data,9000), '--', label=r'$\rho= 9\ g\ cm^{-3}$')

# plt.loglog(g_data,func_rho_th90(g_data,1000), '-', label=r'$\rho= 1\ g\ cm^{-3}$')
# plt.loglog(g_data,func_rho_th90(g_data,3000), '-', label=r'$\rho= 3\ g\ cm^{-3}$')
# plt.loglog(g_data,func_rho_th90(g_data,5000), '-', label=r'$\rho= 5\ g\ cm^{-3}$')
# plt.loglog(g_data,func_rho_th90(g_data,7000), '-', label=r'$\rho= 7\ g\ cm^{-3}$')
# plt.loglog(g_data,func_rho_th90(g_data,9000), '-', label=r'$\rho= 9\ g\ cm^{-3}$')

# plt.axvline(x = 0.144/9.81 , color = 'b', linestyle='-.')#, label = '')
# plt.annotate(xy=[0.2/9.81, 3e-7], text='Psyche')

# plt.xlim(1.0e-8,1)
# plt.ylim(1.0e-8,1)
# plt.legend()
# plt.yticks(rotation=90)
# plt.title(r"$\chi=40.0$ and $B_0=5 \times 10^{-5}$ T")
# plt.xlabel('Ambient Gravitational Acceleration (Earth Gs)')
# plt.ylabel('Particle Radius (meters)')
# plt.grid(True)
# plt.show()

tpl.save("/home/dusty-sikka/Research/Planetary_Science_Journal/Tikz/test_ag.tex")
plt.show()