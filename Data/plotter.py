import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True


sep=np.arange(2.0, 4.3, 0.2)

MDM_96 = np.array([-1.76216,-1.16587,	-0.80543,	-0.575792,	-0.423281,	-0.318505,
    -0.244461,	-0.190866,	-0.15126,	-0.121461,	-0.0986796,
    -0.0810154,	-0.0671443,	-0.0561265,	-0.0472839,	-0.04101197,
    -0.0342648,	-0.0294419,	-0.0254397,	-0.0220959,	-0.0192845,
    -0.0169069,	-0.014885,	-0.0131569,	-0.0116726,	-0.010392])

FVM_96 = np.array([-1.4527,	-0.96762,	-0.66821,	-0.48026,	-0.3592,
    -0.27257,	-0.21181,	-0.16662,	-0.13401,	-0.10838,
    -0.08734,   -0.073799,	-0.061505,	-0.05106,	-0.043702,
    -0.037189,  -0.032038,	-0.027658,	-0.023973,	-0.020996,
    -0.018301,  -0.016134,	-0.014249,	-0.012641,	-0.011215])

Multipole_96=np.array([-2.30930227717349e-13,-1.32303550148865e-13,
    -8.64014677735036e-14,-6.00756972426264e-14,-4.34924935022301e-14,
    -3.24315356227174e-14,-2.47519360919035e-14,-1.92546120641153e-14,
    -1.52217335973884e-14,-1.22021902842460e-14,-9.90164967585626e-15,
    -8.12217479200644e-15])

MDM_96=MDM_96*1e-13
FVM_96=FVM_96*1e-13

MDM_4_k=np.array([-2.63E-06,	-1.66E-06,	-1.11E-06,	-7.74E-07,	-5.60E-07,
    -4.16E-07,	-3.17E-07,	-2.46E-07,	-1.94E-07,	-1.55E-07,
    -1.25E-07,	-1.03E-07])
Multipole_4_k=np.array([-6.46E-06,	-2.28E-06,	-1.31E-06,	-8.55E-07,
    -5.96E-07,	-4.34E-07,	-3.26E-07,	-2.51E-07,	-1.96E-07,
    -1.56E-07,	-1.26E-07,	-1.03E-07])
FVM_4_k= np.array([3.50934272698700e-06,2.00351227085717e-06,1.30167932187016e-06,
    9.04853109366566e-07,6.56971203988139e-07,4.92160075900438e-07,
    3.77695294165662e-07,2.95548783567419e-07,2.35049638898315e-07,
    1.89538244515712e-07,1.54684922612043e-07])

FVM_4_k=-FVM_4_k

plt.figure()
plt.plot(sep, MDM_96[:12]/Multipole_96[0], '-', label='Mutual Dipole Moment')
plt.plot(sep[1:], FVM_96[:11]/Multipole_96[0], '--', label='Finite Volume Method')
plt.plot(sep, Multipole_96[:12]/Multipole_96[0], '-.', label='Spherical Harmonic Approximation')
plt.legend()
plt.title(r'$\theta=0\ deg,\quad \chi=0.96$')
plt.xlabel('Separation Distance (Particle Radius)')
plt.ylabel('Normalized Force')
plt.grid(True)
plt.show()

plt.figure()
plt.plot(sep, MDM_4_k[:12]/Multipole_4_k[0], '-', label='Mutual Dipole Moment')
plt.plot(sep[1:], FVM_4_k[:11]/Multipole_4_k[0], '--', label='Finite Volume Method')
plt.plot(sep, Multipole_4_k[:12]/Multipole_4_k[0], '-.', label='Spherical Harmonic Approximation')
plt.legend()
plt.title(r'$\theta=0\ deg,\quad \chi=4$')
plt.xlabel('Separation Distance (Particle Radius)')
plt.ylabel('Normalized Force')
plt.grid(True)
plt.show()