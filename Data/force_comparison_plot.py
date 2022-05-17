import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tikzplotlib as tpl

plt.rcParams['text.usetex'] = True

def surf_g(a, g):
    rho=5000 #kg/m^3
    return rho*(4.0/3.0)*np.pi*a**3*g

def self_g(a):
    rho=5000 #kg/m^3
    G=6.6743e-11 #m^3/kg s^2
    return G*(rho*np.pi*a**2/3.0)**2

def cohesion(a,S):
    return 3.6e-2*a*S**2

def mag_force(a,B0):
    mu0=4.0*np.pi*1e-7
    H0=B0/mu0
    f=0.000203331052979
    return (a**2)*(H0**2)*f

a=np.logspace(-7,0,10)
print(a)
#surface gravity plots
plt.loglog(a, surf_g(a, 1e-4), '-.', label='Grav g=1.0e-4 m/s$^2$')
plt.loglog(a, surf_g(a, 1e-3), '-.', label='Grav g=1.0e-3 m/s$^2$')
plt.loglog(a, surf_g(a, 1e-2), '-.', label='Grav g=1.0e-2 m/s$^2$')
plt.loglog(a, surf_g(a, 1e-1), '-.', label='Grav g=1.0e-1 m/s$^2$')
# self gravity plot
plt.loglog(a, self_g(a), ':', label='Self Grav')
#Cohesion plots
plt.loglog(a, cohesion(a,0.1), '--', label='Cohesion S=0.1')
plt.loglog(a, cohesion(a,1.0), '--', label='Cohesion S=1.0')
#Magnetic force plots
plt.loglog(a, mag_force(a,5e-7), label='mag B=5.0e-7 T')
plt.loglog(a, mag_force(a,5e-6), label='mag B=5.0e-6 T')
plt.loglog(a, mag_force(a,5e-5), label='mag B=5.0e-5 T')
plt.loglog(a, mag_force(a,5e-4), label='mag B=5.0e-4 T')
plt.loglog(a, mag_force(a,5e-3), label='mag B=5.0e-3 T')

plt.ylim(1.0e-20,1.0e5)
plt.xlim(1.0e-7,1)
plt.legend(ncol=2)
plt.yticks(rotation=90)
plt.title(r"$B_0=5 \times 10^{-5}$ T and $\rho= 5\ g\ cm^{-3}$")
plt.ylabel('Force (N)')
plt.xlabel('Particle Radius (meters)')
plt.grid(True)

tpl.save("/home/aerospacenerd/Research/Planetary_Science_Journal/Tikz/test_force_comp.tex")

plt.show()