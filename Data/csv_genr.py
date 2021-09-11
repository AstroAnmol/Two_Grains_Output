import pandas as pd
import numpy as np

# Making Data frame for H0=1 A/m, a=1 m, theta=0 deg 

# Define the data 
c_data = np.linspace(2,4.2,12)
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

fz_data=np.array([fz_data_0025,fz_data_0050,fz_data_0075,fz_data_0100,fz_data_0150,fz_data_0200,fz_data_0250,fz_data_0300,fz_data_0350,fz_data_0400,fz_data_0450,fz_data_0500,fz_data_0550,fz_data_0600])
data_H1_a1_th0=pd.DataFrame(fz_data.transpose(),columns=['0.25','0.5','0.75','1.0','1.5','2.0','2.5','3.0','3.5','4.0','4.5','5.0','5.5','6.0'])
#data_H1_a1_th0=pd.DataFrame()
data_H1_a1_th0['c']=c_data
data_H1_a1_th0.set_index('c', inplace=True)
data_H1_a1_th0.to_csv('Data/data_H1_a1_th0.csv')