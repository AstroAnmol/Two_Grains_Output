import pandas as pd
import numpy as np

# Making Data frame for H0=1 A/m, a=1 m, theta=0 deg 

# Define the data 
c_data = np.linspace(2,4.2,12)
#susc=0.1
fz_data_0010=np.array([-6.44E-09,	-4.32E-09,	-3.02E-09,	-2.18E-09,	-1.62E-09,	-1.22E-09,	-9.44E-10,	-7.40E-10,	-5.88E-10,	-4.73E-10,	-3.85E-10,	-3.17E-10])
#susc=0.15
fz_data_0015=np.array([-1.44E-08,	-9.55E-09,	-6.65E-09,	-4.79E-09,	-3.54E-09,	-2.68E-09,	-2.06E-09,	-1.62E-09,	-1.28E-09,	-1.03E-09,	-8.41E-10,	-6.92E-10])
#susc=0.2
fz_data_0020=np.array([-2.53E-08,	-1.67E-08,	-1.16E-08,	-8.30E-09,	-6.13E-09,	-4.63E-09,	-3.57E-09,	-2.79E-09,	-2.22E-09,	-1.78E-09,	-1.45E-09,	-1.19E-09])
#susc=0.25
fz_data_0025=np.array([-3.92E-08,	-2.56E-08,	-1.77E-08,	-1.26E-08,	-9.32E-09,	-7.04E-09,	-5.41E-09,	-4.24E-09,	-3.36E-09,	-2.71E-09,	-2.20E-09,	-1.81E-09])
#susc=0.5
fz_data_0050=np.array([-1.51E-07,	-9.37E-08,	-6.33E-08,	-4.48E-08,	-3.28E-08,	-2.46E-08,	-1.89E-08,	-1.48E-08,	-1.17E-08,	-9.39E-09,	-7.63E-09,	-6.27E-09])
#susc=0.75
fz_data_0075=np.array([-3.26E-07,	-1.94E-07,	-1.28E-07,	-8.99E-08,	-6.54E-08,	-4.89E-08,	-3.74E-08,	-2.92E-08,	-2.31E-08,	-1.85E-08,	-1.50E-08,	-1.23E-08])
#susc=1
fz_data_0100=np.array([-5.57E-07,	-3.17E-07,	-2.07E-07,	-1.43E-07,	-1.04E-07,	-7.73E-08,	-5.90E-08,	-4.59E-08,	-3.63E-08,	-2.91E-08,	-2.36E-08,	-1.93E-08])
#susc=1.5
fz_data_0150=np.array([-1.17E-06,	-6.11E-07,	-3.86E-07,	-2.64E-07,	-1.89E-07,	-1.40E-07,	-1.06E-07,	-8.25E-08,	-6.51E-08,	-5.21E-08,	-4.22E-08,	-3.46E-08])
#susc=2
fz_data_0200=np.array([-1.97E-06,	-9.39E-07,	-5.79E-07,	-3.90E-07,	-2.78E-07,	-2.05E-07,	-1.55E-07,	-1.20E-07,	-9.44E-08,	-7.55E-08,	-6.11E-08,	-5.00E-08])
#susc=2.5
fz_data_0250=np.array([-2.91E-06,	-1.28E-06,	-7.72E-07,	-5.16E-07,	-3.64E-07,	-2.68E-07,	-2.02E-07,	-1.56E-07,	-1.23E-07,	-9.79E-08,	-7.92E-08,	-6.48E-08])
#susc=3
fz_data_0300=np.array([-3.98E-06,	-1.62E-06,	-9.60E-07,	-6.36E-07,	-4.47E-07,	-3.27E-07,	-2.46E-07,	-1.90E-07,	-1.49E-07,	-1.19E-07,	-9.62E-08,	-7.86E-08])
#susc=3.5
fz_data_0350=np.array([-5.17E-06,	-1.96E-06,	-1.14E-06,	-7.49E-07,	-5.24E-07,	-3.83E-07,	-2.88E-07,	-2.22E-07,	-1.74E-07,	-1.38E-07,	-1.12E-07,	-9.14E-08])
#susc=4
fz_data_0400=np.array([-6.46E-06,	-2.28E-06,	-1.31E-06,	-8.55E-07,	-5.96E-07,	-4.34E-07,	-3.26E-07,	-2.51E-07,	-1.96E-07,	-1.56E-07,	-1.26E-07,	-1.03E-07])
#susc=4.5
fz_data_0450=np.array([-7.84E-06,	-2.59E-06,	-1.47E-06,	-9.54E-07,	-6.63E-07,	-4.82E-07,	-3.61E-07,	-2.77E-07,	-2.17E-07,	-1.73E-07,	-1.40E-07,	-1.14E-07])
#susc=5.0
fz_data_0500=np.array([-9.30E-06,	-2.89E-06,	-1.62E-06,	-1.05E-06,	-7.25E-07,	-5.26E-07,	-3.94E-07,	-3.02E-07,	-2.36E-07,	-1.88E-07,	-1.52E-07,	-1.24E-07])
#susc=5.5
fz_data_0550=np.array([-1.08E-05,	-3.17E-06,	-1.76E-06,	-1.13E-06,	-7.82E-07,	-5.66E-07,	-4.23E-07,	-3.25E-07,	-2.54E-07,	-2.02E-07,	-1.63E-07,	-1.33E-07])
#susc=6.0
fz_data_0600=np.array([-1.24E-05,	-3.44E-06,	-1.89E-06,	-1.21E-06,	-8.35E-07,	-6.04E-07,	-4.51E-07,	-3.46E-07,	-2.70E-07,	-2.15E-07,	-1.73E-07,	-1.41E-07])
#susc=6.5
fz_data_0650=np.array([-1.41E-05,	-3.69E-06,	-2.01E-06,	-1.28E-06,	-8.84E-07,	-6.38E-07,	-4.77E-07,	-3.65E-07,	-2.85E-07,	-2.27E-07,	-1.83E-07,	-1.49E-07])
#susc=7.0
fz_data_0700=np.array([-1.58E-05,	-3.93E-06,	-2.13E-06,	-1.35E-06,	-9.30E-07,	-6.70E-07,	-5.00E-07,	-3.83E-07,	-2.99E-07,	-2.38E-07,	-1.91E-07,	-1.56E-07])
#susc=7.5
fz_data_0750=np.array([-1.76E-05,	-4.15E-06,	-2.24E-06,	-1.42E-06,	-9.72E-07,	-7.00E-07,	-5.22E-07,	-3.99E-07,	-3.12E-07,	-2.48E-07,	-2.00E-07,	-1.63E-07])
#susc=8.0
fz_data_0800=np.array([-1.94E-05,	-4.37E-06,	-2.34E-06,	-1.48E-06,	-1.01E-06,	-7.28E-07,	-5.42E-07,	-4.15E-07,	-3.24E-07,	-2.57E-07,	-2.07E-07,	-1.69E-07])
#susc=8.5
fz_data_0850=np.array([-2.18E-05,	-4.57E-06,	-2.43E-06,	-1.53E-06,	-1.05E-06,	-7.54E-07,	-5.61E-07,	-4.29E-07,	-3.35E-07,	-2.66E-07,	-2.14E-07,	-1.75E-07])
#susc=9.0
fz_data_0900=np.array([-2.38E-05,	-4.76E-06,	-2.52E-06,	-1.59E-06,	-1.08E-06,	-7.78E-07,	-5.79E-07,	-4.42E-07,	-3.45E-07,	-2.74E-07,	-2.21E-07,	-1.80E-07])
#susc=9.5
fz_data_0950=np.array([-2.59E-05,	-4.95E-06,	-2.61E-06,	-1.64E-06,	-1.12E-06,	-8.01E-07,	-5.96E-07,	-4.55E-07,	-3.55E-07,	-2.82E-07,	-2.27E-07,	-1.85E-07])
#susc=10.0
fz_data_1000=np.array([-2.80E-05,	-5.12E-06,	-2.69E-06,	-1.68E-06,	-1.15E-06,	-8.22E-07,	-6.11E-07,	-4.67E-07,	-3.64E-07,	-2.89E-07,	-2.32E-07,	-1.89E-07])
#susc=10.5
fz_data_1050=np.array([-3.01E-05,	-5.28E-06,	-2.76E-06,	-1.73E-06,	-1.17E-06,	-8.42E-07,	-6.26E-07,	-4.78E-07,	-3.72E-07,	-2.95E-07,	-2.38E-07,	-1.94E-07])
#susc=11.0
fz_data_1100=np.array([-3.23E-05,	-5.44E-06,	-2.83E-06,	-1.77E-06,	-1.20E-06,	-8.61E-07,	-6.40E-07,	-4.88E-07,	-3.80E-07,	-3.02E-07,	-2.43E-07,	-1.98E-07])
#susc=11.5
fz_data_1150=np.array([-3.45E-05,	-5.59E-06,	-2.90E-06,	-1.81E-06,	-1.23E-06,	-8.79E-07,	-6.52E-07,	-4.98E-07,	-3.88E-07,	-3.08E-07,	-2.48E-07,	-2.02E-07])
#susc=12.0
fz_data_1200=np.array([-3.67E-05,	-5.73E-06,	-2.96E-06,	-1.84E-06,	-1.25E-06,	-8.95E-07,	-6.65E-07,	-5.07E-07,	-3.95E-07,	-3.13E-07,	-2.52E-07,	-2.05E-07])
#########################
## Higher susc data
#susc=15.0
fz_data_1500=np.array([-5.22E-05,	-6.46E-06,	-3.28E-06,	-2.03E-06,	-1.37E-06,	-9.79E-07,	-7.25E-07,	-5.53E-07,	-4.30E-07,	-3.41E-07,	-2.74E-07,	-2.23E-07])
#susc=20.0
fz_data_2000=np.array([-7.99E-05,	-7.33E-06,	-3.66E-06,	-2.24E-06,	-1.51E-06,	-1.07E-06,	-7.95E-07,	-6.05E-07,	-4.70E-07,	-3.72E-07,	-2.99E-07,	-2.44E-07])
#susc=25.0
fz_data_2500=np.array([-1.09E-04,	-7.94E-06,	-3.91E-06,	-2.39E-06,	-1.60E-06,	-1.14E-06,	-8.41E-07,	-6.40E-07,	-4.97E-07,	-3.93E-07,	-3.16E-07,	-2.57E-07])
#susc=30.0
fz_data_3000=np.array([-1.38E-04,	-8.39E-06,	-4.10E-06,	-2.49E-06,	-1.67E-06,	-1.18E-06,	-8.75E-07,	-6.64E-07,	-5.16E-07,	-4.08E-07,	-3.28E-07,	-2.67E-07])
#susc=35.0
fz_data_3500=np.array([-1.73E-04,	-8.74E-06,	-4.24E-06,	-2.57E-06,	-1.72E-06,	-1.22E-06,	-9.00E-07,	-6.83E-07,	-5.31E-07,	-4.20E-07,	-3.37E-07,	-2.74E-07])
#susc=40.0
fz_data_4000=np.array([-2.03E-04,	-9.01E-06,	-4.35E-06,	-2.63E-06,	-1.76E-06,	-1.25E-06,	-9.19E-07,	-6.98E-07,	-5.42E-07,	-4.28E-07,	-3.44E-07,	-2.80E-07])
#susc=45.0
fz_data_4500=np.array([-2.33E-04,	-9.23E-06,	-4.44E-06,	-2.68E-06,	-1.79E-06,	-1.27E-06,	-9.35E-07,	-7.09E-07,	-5.51E-07,	-4.36E-07,	-3.50E-07,	-2.84E-07])
#susc=50.0
fz_data_5000=np.array([-2.63E-04,	-9.41E-06,	-4.51E-06,	-2.72E-06,	-1.82E-06,	-1.29E-06,	-9.47E-07,	-7.19E-07,	-5.58E-07,	-4.41E-07,	-3.54E-07,	-2.88E-07])
#susc=55.0
fz_data_5500=np.array([-3.35E-04,	-9.57E-06,	-4.57E-06,	-2.75E-06,	-1.84E-06,	-1.30E-06,	-9.58E-07,	-7.27E-07,	-5.64E-07,	-4.46E-07,	-3.58E-07,	-2.91E-07])
#susc=60.0
fz_data_6000=np.array([-3.73E-04,	-9.70E-06,	-4.63E-06,	-2.78E-06,	-1.86E-06,	-1.31E-06,	-9.67E-07,	-7.34E-07,	-5.69E-07,	-4.50E-07,	-3.61E-07,	-2.94E-07])
#susc=65.0
fz_data_6500=np.array([-4.09E-04,	-9.81E-06,	-4.67E-06,	-2.81E-06,	-1.87E-06,	-1.32E-06,	-9.75E-07,	-7.39E-07,	-5.74E-07,	-4.54E-07,	-3.64E-07,	-2.96E-07])
#susc=70.0
fz_data_7000=np.array([-4.46E-04,	-9.91E-06,	-4.71E-06,	-2.83E-06,	-1.88E-06,	-1.33E-06,	-9.82E-07,	-7.44E-07,	-5.78E-07,	-4.57E-07,	-3.66E-07,	-2.98E-07])
#susc=75.0
fz_data_7500=np.array([-4.93E-04,	-9.99E-06,	-4.74E-06,	-2.85E-06,	-1.90E-06,	-1.34E-06,	-9.87E-07,	-7.49E-07,	-5.81E-07,	-4.59E-07,	-3.69E-07,	-3.00E-07])
#susc=80.0
fz_data_8000=np.array([-5.29E-04,	-1.01E-05,	-4.77E-06,	-2.86E-06,	-1.91E-06,	-1.35E-06,	-9.93E-07,	-7.53E-07,	-5.84E-07,	-4.61E-07,	-3.70E-07,	-3.01E-07])
#susc=85.0
fz_data_8500=np.array([-5.64E-04,	-1.01E-05,	-4.80E-06,	-2.88E-06,	-1.92E-06,	-1.35E-06,	-9.97E-07,	-7.56E-07,	-5.86E-07,	-4.64E-07,	-3.72E-07,	-3.03E-07])
#susc=90.0
fz_data_9000=np.array([-5.99E-04,	-1.02E-05,	-4.82E-06,	-2.89E-06,	-1.92E-06,	-1.36E-06,	-1.00E-06,	-7.59E-07,	-5.89E-07,	-4.65E-07,	-3.73E-07,	-3.04E-07])
#susc=95.0
fz_data_9500=np.array([-6.33E-04,	-1.03E-05,	-4.85E-06,	-2.90E-06,	-1.93E-06,	-1.37E-06,	-1.00E-06,	-7.62E-07,	-5.91E-07,	-4.67E-07,	-3.75E-07,	-3.05E-07])
#susc=100.0
fz_data_10000=np.arrya([-6.66E-04,	-1.03E-05,	-4.87E-06,	-2.92E-06,	-1.94E-06,	-1.37E-06,	-1.01E-06,	-7.64E-07,	-5.93E-07,	-4.68E-07,	-3.76E-07,	-3.06E-07])


fz_data=np.array([fz_data_0025,fz_data_0050,fz_data_0075,fz_data_0100,fz_data_0150,fz_data_0200,fz_data_0250,fz_data_0300,fz_data_0350,fz_data_0400,fz_data_0450,fz_data_0500,fz_data_0550,fz_data_0600,fz_data_0650,fz_data_0700,fz_data_0750,fz_data_0800])
data_H1_a1_th0=pd.DataFrame(fz_data.transpose(),columns=['0.25','0.5','0.75','1.0','1.5','2.0','2.5','3.0','3.5','4.0','4.5','5.0','5.5','6.0','6.5','7.0','7.5','8.0'])
#data_H1_a1_th0=pd.DataFrame()
data_H1_a1_th0['c']=c_data
data_H1_a1_th0.set_index('c', inplace=True)
data_H1_a1_th0.to_csv('Data/data_H1_a1_th0.csv')

extra_fz_data=np.array([fz_data_0010,fz_data_0015,fz_data_0020,fz_data_0850,fz_data_0900,fz_data_0950,fz_data_1000,fz_data_1050,fz_data_1100,fz_data_1150,fz_data_1200])
extra_data_H1_a1_th0=pd.DataFrame(extra_fz_data.transpose(),columns=['0.1','0.15','0.2','8.5','9.0','9.5','10.0','10.5','11.0','11.5','12.0'])
#data_H1_a1_th0=pd.DataFrame()
extra_data_H1_a1_th0['c']=c_data
extra_data_H1_a1_th0.set_index('c', inplace=True)
extra_data_H1_a1_th0.to_csv('Data/extra_data_H1_a1_th0.csv')

## Making Data frame for H0=1 A/m, a=1 m, theta=90 deg 

## Perpedicular case data 
#susc=0.1
perp_fz_data_0010=np.array([2.95E-09,	2.03E-09,	1.44E-09,	1.04E-09,	7.69E-10,	5.78E-10,	4.41E-10,	3.41E-10,	2.66E-10,	2.09E-10,	1.66E-10,	1.32E-10])
#susc=0.15
perp_fz_data_0015=np.array([6.37E-09,	4.42E-09,	3.14E-09,	2.28E-09,	1.69E-09,	1.28E-09,	9.79E-10,	7.61E-10,	5.98E-10,	4.75E-10,	3.80E-10,	3.06E-10])
#susc=0.2
perp_fz_data_0020=np.array([1.09E-08,	7.57E-09,	5.40E-09,	3.93E-09,	2.92E-09,	2.21E-09,	1.70E-09,	1.33E-09,	1.05E-09,	8.33E-10,	6.70E-10,	5.42E-10])
#susc=0.25
perp_fz_data_0025=np.array([1.63E-08,	1.14E-08,	8.15E-09,	5.95E-09,	4.43E-09,	3.36E-09,	2.59E-09,	2.02E-09,	1.60E-09,	1.28E-09,	1.03E-09,	8.35E-10])
#susc=0.5
perp_fz_data_0050=np.array([5.34E-08,	3.82E-08,	2.76E-08,	2.03E-08,	1.52E-08,	1.16E-08,	8.97E-09,	7.04E-09,	5.59E-09,	4.49E-09,	3.64E-09,	2.97E-09])
#susc=0.75
perp_fz_data_0075=np.array([1.00E-07,	7.29E-08,	5.32E-08,	3.94E-08,	2.96E-08,	2.26E-08,	1.76E-08,	1.38E-08,	1.10E-08,	8.83E-09,	7.18E-09,	5.88E-09])
#susc=1
perp_fz_data_0100=np.array([1.51E-07,	1.11E-07,	8.19E-08,	6.10E-08,	4.60E-08,	3.52E-08,	2.74E-08,	2.15E-08,	1.72E-08,	1.38E-08,	1.12E-08,	9.23E-09])
#susc=1.5
perp_fz_data_0150=np.array([2.55E-07,	1.91E-07,	1.42E-07,	1.07E-07,	8.08E-08,	6.21E-08,	4.83E-08,	3.81E-08,	3.04E-08,	2.46E-08,	2.00E-08,	1.64E-08])
#susc=2
perp_fz_data_0200=np.array([3.52E-07,	2.67E-07,	2.01E-07,	1.51E-07,	1.15E-07,	8.88E-08,	6.93E-08,	5.47E-08,	4.37E-08,	3.53E-08,	2.88E-08,	2.37E-08])
#susc=2.5
perp_fz_data_0250=np.array([4.41E-07,	3.37E-07,	2.55E-07,	1.93E-07,	1.48E-07,	1.14E-07,	8.90E-08,	7.04E-08,	5.63E-08,	4.55E-08,	3.72E-08,	3.06E-08])
#susc=3
perp_fz_data_0300=np.array([5.20E-07,	4.01E-07,	3.05E-07,	2.32E-07,	1.77E-07,	1.37E-07,	1.07E-07,	8.50E-08,	6.80E-08,	5.50E-08,	4.49E-08,	3.70E-08])
#susc=3.5
perp_fz_data_0350=np.array([5.90E-07,	4.58E-07,	3.50E-07,	2.67E-07,	2.05E-07,	1.58E-07,	1.24E-07,	9.83E-08,	7.87E-08,	6.37E-08,	5.20E-08,	4.29E-08])
#susc=4
perp_fz_data_0400=np.array([6.53E-07,	5.09E-07,	3.91E-07,	2.98E-07,	2.29E-07,	1.78E-07,	1.39E-07,	1.10E-07,	8.85E-08,	7.17E-08,	5.86E-08,	4.83E-08])
#susc=4.5
perp_fz_data_0450=np.array([7.10E-07,	5.55E-07,	4.27E-07,	3.27E-07,	2.52E-07,	1.95E-07,	1.53E-07,	1.22E-07,	9.75E-08,	7.89E-08,	6.45E-08,	5.32E-08])
#susc=5.0
perp_fz_data_0500=np.array([7.60E-07,	5.97E-07,	4.61E-07,	3.53E-07,	2.72E-07,	2.11E-07,	1.66E-07,	1.32E-07,	1.06E-07,	8.56E-08,	7.00E-08,	5.77E-08])
#susc=5.5
perp_fz_data_0550=np.array([8.06E-07,	6.35E-07,	4.91E-07,	3.77E-07,	2.91E-07,	2.26E-07,	1.78E-07,	1.41E-07,	1.13E-07,	9.16E-08,	7.49E-08,	6.18E-08])
#susc=6.0
perp_fz_data_0600=np.array([8.47E-07,	6.69E-07,	5.18E-07,	3.99E-07,	3.08E-07,	2.40E-07,	1.88E-07,	1.49E-07,	1.20E-07,	9.72E-08,	7.95E-08,	6.56E-08])
#susc=6.5
perp_fz_data_0650=np.array([8.85E-07,	7.00E-07,	5.43E-07,	4.19E-07,	3.23E-07,	2.52E-07,	1.98E-07,	1.57E-07,	1.26E-07,	1.02E-07,	8.37E-08,	6.91E-08])
#susc=7.0
perp_fz_data_0700=np.array([9.19E-07,	7.29E-07,	5.66E-07,	4.37E-07,	3.38E-07,	2.63E-07,	2.07E-07,	1.64E-07,	1.32E-07,	1.07E-07,	8.76E-08,	7.23E-08])
#susc=7.5
perp_fz_data_0750=np.array([9.51E-07,	7.55E-07,	5.88E-07,	4.54E-07,	3.51E-07,	2.74E-07,	2.15E-07,	1.71E-07,	1.37E-07,	1.11E-07,	9.11E-08,	7.52E-08])
#susc=8.0
perp_fz_data_0800=np.array([9.79E-07,	7.79E-07,	6.07E-07,	4.69E-07,	3.63E-07,	2.83E-07,	2.23E-07,	1.77E-07,	1.42E-07,	1.15E-07,	9.44E-08,	7.80E-08])
#susc=8.5
perp_fz_data_0850=np.array([1.01E-06,	8.01E-07,	6.25E-07,	4.84E-07,	3.75E-07,	2.92E-07,	2.30E-07,	1.83E-07,	1.47E-07,	1.19E-07,	9.75E-08,	8.05E-08])
#susc=9.0
perp_fz_data_0900=np.array([1.03E-06,	8.22E-07,	6.42E-07,	4.97E-07,	3.85E-07,	3.00E-07,	2.37E-07,	1.88E-07,	1.51E-07,	1.23E-07,	1.00E-07,	8.29E-08])
#susc=9.5
perp_fz_data_0950=np.array([1.05E-06,	8.41E-07,	6.58E-07,	5.09E-07,	3.95E-07,	3.08E-07,	2.43E-07,	1.93E-07,	1.55E-07,	1.26E-07,	1.03E-07,	8.51E-08])
#susc=10.0
perp_fz_data_1000=np.array([1.07E-06,	8.59E-07,	6.72E-07,	5.21E-07,	4.04E-07,	3.15E-07,	2.48E-07,	1.98E-07,	1.59E-07,	1.29E-07,	1.06E-07,	8.71E-08])
#susc=10.5
perp_fz_data_1050=np.array([1.09E-06,	8.75E-07,	6.86E-07,	5.32E-07,	4.13E-07,	3.22E-07,	2.54E-07,	2.02E-07,	1.62E-07,	1.32E-07,	1.08E-07,	8.91E-08])
#susc=11.0
perp_fz_data_1100=np.array([1.11E-06,	8.91E-07,	6.98E-07,	5.42E-07,	4.21E-07,	3.29E-07,	2.59E-07,	2.06E-07,	1.66E-07,	1.34E-07,	1.10E-07,	9.09E-08])
#susc=11.5
perp_fz_data_1150=np.array([1.13E-06,	9.05E-07,	7.10E-07,	5.51E-07,	4.28E-07,	3.34E-07,	2.64E-07,	2.10E-07,	1.69E-07,	1.37E-07,	1.12E-07,	9.26E-08])
#susc=12.0
perp_fz_data_1200=np.array([1.15E-06,	9.19E-07,	7.21E-07,	5.60E-07,	4.35E-07,	3.40E-07,	2.68E-07,	2.13E-07,	1.72E-07,	1.39E-07,	1.14E-07,	9.42E-08])

perp_fz_data=np.array([perp_fz_data_0025,perp_fz_data_0050,perp_fz_data_0075,perp_fz_data_0100,perp_fz_data_0150,perp_fz_data_0200,perp_fz_data_0250,perp_fz_data_0300,perp_fz_data_0350,perp_fz_data_0400,perp_fz_data_0450,perp_fz_data_0500,perp_fz_data_0550,perp_fz_data_0600,perp_fz_data_0650,perp_fz_data_0700,perp_fz_data_0750,perp_fz_data_0800])
data_H1_a1_th90=pd.DataFrame(perp_fz_data.transpose(),columns=['0.25','0.5','0.75','1.0','1.5','2.0','2.5','3.0','3.5','4.0','4.5','5.0','5.5','6.0','6.5','7.0','7.5','8.0'])
#data_H1_a1_th0=pd.DataFrame()
data_H1_a1_th90['c']=c_data
data_H1_a1_th90.set_index('c', inplace=True)
data_H1_a1_th90.to_csv('Data/data_H1_a1_th90.csv')

extra_perp_fz_data=np.array([perp_fz_data_0010,perp_fz_data_0015,perp_fz_data_0020,perp_fz_data_0850,perp_fz_data_0900,perp_fz_data_0950,perp_fz_data_1000,perp_fz_data_1050,perp_fz_data_1100,perp_fz_data_1150,perp_fz_data_1200])
extra_data_H1_a1_th90=pd.DataFrame(extra_perp_fz_data.transpose(),columns=['0.1','0.15','0.2','8.5','9.0','9.5','10.0','10.5','11.0','11.5','12.0'])
#data_H1_a1_th0=pd.DataFrame()
extra_data_H1_a1_th90['c']=c_data
extra_data_H1_a1_th90.set_index('c', inplace=True)
extra_data_H1_a1_th90.to_csv('Data/extra_data_H1_a1_th90.csv')