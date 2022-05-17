import pandas as pd
import numpy as np
import tikzplotlib as tpl

import matplotlib.pyplot as plt


plt.rcParams['text.usetex'] = True

#Data
sep=np.arange(2.0, 4.3, 0.2)

sep_FVM=np.array([2.1,2.2,	2.4,	2.6,	2.8,	3,	3.2,	3.4,	3.6,	3.8,	4,	4.2])

##### Parallel Case
# MDM_1=np.array([-4.21E-07, -2.78E-07,	-1.92E-07,	-1.37E-07,	-1.01E-07,	-7.59E-08,	-5.82E-08,	-4.55E-08,	-3.60E-08,	-2.89E-08,	-2.35E-08,	-1.93E-08])

# FVM_1=np.array([-4.01E-07,	-3.31E-07,	-2.16E-07,	-1.50E-07,	-1.08E-07,	-8.06E-08,	-6.15E-08,	-4.78E-08,	-3.78E-08,	-3.02E-08,	-2.45E-08,	-2.01E-08])

# Multipole_1=np.array([-5.57E-07,	-3.17E-07,	-2.07E-07,	-1.43E-07,	-1.04E-07,	-7.73E-08,	-5.90E-08,	-4.59E-08,	-3.63E-08,	-2.91E-08,	-2.36E-08,	-1.93E-08])

# MDM_4=np.array([-2.63E-06,	-1.66E-06,	-1.11E-06,	-7.74E-07,	-5.60E-07,	-4.16E-07,	-3.17E-07,	-2.46E-07,	-1.94E-07,	-1.55E-07,	-1.25E-07,	-1.03E-07])

# FVM_4=np.array([-4.29E-06,	-3.11E-06,	-1.79E-06,	-1.16E-06,	-8.11E-07,	-5.89E-07,	-4.42E-07,	-3.39E-07,	-2.66E-07,	-2.11E-07,	-1.71E-07,	-1.39E-07])

# Multipole_4=np.array([-6.46E-06,	-2.28E-06,	-1.31E-06,	-8.55E-07,	-5.96E-07,	-4.34E-07,	-3.26E-07,	-2.51E-07,	-1.96E-07,	-1.56E-07,	-1.26E-07,	-1.03E-07])


##### Perpendicular Case
# MDM_1=np.array([1.74E-07,	1.21E-07,	8.61E-08,	6.30E-08,	4.71E-08,	3.59E-08,	2.78E-08,	2.19E-08,	1.74E-08,	1.41E-08,	1.15E-08,	9.45E-09])

# Multipole_1=np.array([1.51E-07,	1.11E-07,	8.19E-08,	6.10E-08,	4.60E-08,	3.52E-08,	2.74E-08,	2.15E-08,	1.72E-08,	1.38E-08,	1.12E-08,	9.23E-09])

MDM_4=np.array([8.42E-07,	5.95E-07,	4.30E-07,	3.18E-07,	2.39E-07,	1.83E-07,	1.43E-07,	1.12E-07,	8.99E-08,	7.27E-08,	5.94E-08,	4.90E-08])

Multipole_4=np.array([6.53E-07,	5.09E-07,	3.91E-07,	2.98E-07,	2.29E-07,	1.78E-07,	1.39E-07,	1.10E-07,	8.85E-08,	7.17E-08,	5.86E-08,	4.83E-08])


MDM=MDM_4
# FVM=FVM_4
Multipole=Multipole_4

# fig, ax = plt.subplots(figsize=set_size(513.1174))

plt.style.use("ggplot")

plt.plot(sep, MDM[:12]/Multipole[0], ':', label='Mutual Dipole Moment')
# plt.plot(sep_FVM, FVM[:12]/Multipole[0], '--', label='Finite Volume Method')
plt.plot(sep, Multipole[:12]/Multipole[0], '-', label='Spherical Harmonic Approximation')
plt.legend()
plt.title(r'$\theta=90\ deg,\quad \chi=4$')
plt.xlabel('Separation Distance (Particle Radius)')
plt.ylabel('Normalized Force')
plt.grid(True)


# a=np.arange(1, 10.1, 0.5)
# a=a*1e-6

# # fmag=np.array([-2.18E-15,	-4.90E-15,	-8.72E-15,	-1.36E-14,	-1.96E-14,	-2.67E-14,
# # 	-3.49E-14,	-4.41E-14,	-5.45E-14,	-6.59E-14,	-7.85E-14,	-9.21E-14,	-1.07E-13,	
# #     -1.23E-13,	-1.39E-13,	-1.57E-13,	-1.77E-13,	-1.97E-13,	-2.18E-13]) #parallel chi 1
# fmag=np.array([1.45133419e-15, 3.26472485e-15, 5.80533678e-15, 9.06991228e-15,
#  1.30627405e-14, 1.77746185e-14, 2.32213471e-14, 2.93749097e-14,
#  3.62796491e-14, 4.39023058e-14, 5.22355976e-14, 6.13157536e-14,
#  7.10984742e-14, 8.16218491e-14, 9.28853884e-14, 1.04827977e-13,
#  1.17499639e-13, 1.31012522e-13, 1.45118597e-13]) #parallel chi 1
# fmag=fmag

# def square(a):
#     return 0.00145133419*(a**2)

# print(a, fmag)

# plt.plot(a, fmag, '.', label='Spherical Harmonic Solver Results')
# plt.plot(a, square(a), '--', label='Quadratic Fit')
# # plt.plot(sep, Multipole[:12]/Multipole[0], '-', label='Spherical Harmonic Approximation')
# plt.legend()
# plt.title(r'$\theta=90\ deg,\quad \chi=1, B_0=6 G, c=5$')
# plt.xlabel('Separation Distance (Particle Radius)')
# plt.ylabel('Normalized Force')
# plt.grid(True)

# tpl.clean_figure()

# a=np.geomspace(1e-7, 1e-2, num=10)

# def square_sep_2(a):
#     return -1.4719332E+00*(a**2)

# def square_sep_4(a):
#     return -5.3757407E-03*(a**2)

# fmag_sep_2=np.array([-1.4719E-14	-1.9013E-13	-2.4556E-12	-3.1712E-11	-4.0956E-10	-5.2900E-09	-6.8320E-08	-8.8239E-07	-1.1397E-05	-1.4719E-04])
# fmag_sep_4=np.array([-5.3757E-17,	-6.9430E-16,	-8.9673E-15,	-1.1582E-13,	-1.4958E-12,	-1.9319E-11,	-2.4952E-10,	-3.2227E-09,	-4.1622E-08,	-5.3757E-07])


# plt.plot(a, -fmag_sep_2, '.', label='Spherical Harmonic Solver Results ($c=2$)')
# plt.plot(a, -square_sep_2(a), '--', label='Quadratic Fit ($c=2$)')
# plt.plot(a, -fmag_sep_4, '+', label='Spherical Harmonic Solver Results ($c=4$)')
# plt.plot(a, -square_sep_4(a), '-.', label='Quadratic Fit ($c=4$)')

# plt.legend()
# plt.title(r'$\theta=0\ deg, B_0=6 G, \chi=1$')
# plt.xscale('log')
# plt.yscale('log')
# plt.xlabel('Particle Radius (m)')
# plt.ylabel('Force (N)')
# plt.grid(True)

tpl.save("/home/aerospacenerd/Research/Planetary_Science_Journal/Tikz/test.tex")


plt.show()