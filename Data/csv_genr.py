import pandas as pd
import numpy as np

# Making Data frame for H0=1 A/m, a=1 m, theta=0 deg 

# Define the data 
c_data = np.linspace(2,4.2,12)

#susc=1
fz_data_0010=np.array([-5.57E-07,	-3.17E-07,	-2.07E-07,	-1.43E-07,	-1.04E-07,	-7.73E-08,	-5.90E-08,	-4.59E-08,	-3.63E-08,	-2.91E-08,	-2.36E-08,	-1.93E-08])
#susc=1.5
fz_data_0015=np.array([-1.17E-06,	-6.11E-07,	-3.86E-07,	-2.64E-07,	-1.89E-07,	-1.40E-07,	-1.06E-07,	-8.25E-08,	-6.51E-08,	-5.21E-08,	-4.22E-08,	-3.46E-08])
#susc=2
fz_data_0020=np.array([-1.97E-06,	-9.39E-07,	-5.79E-07,	-3.90E-07,	-2.78E-07,	-2.05E-07,	-1.55E-07,	-1.20E-07,	-9.44E-08,	-7.55E-08,	-6.11E-08,	-5.00E-08])
#susc=2.5
fz_data_0025=np.array([-2.91E-06,	-1.28E-06,	-7.72E-07,	-5.16E-07,	-3.64E-07,	-2.68E-07,	-2.02E-07,	-1.56E-07,	-1.23E-07,	-9.79E-08,	-7.92E-08,	-6.48E-08])
#susc=3
fz_data_0030=np.array([-3.98E-06,	-1.62E-06,	-9.60E-07,	-6.36E-07,	-4.47E-07,	-3.27E-07,	-2.46E-07,	-1.90E-07,	-1.49E-07,	-1.19E-07,	-9.62E-08,	-7.86E-08])
#susc=3.5
fz_data_0035=np.array([-5.17E-06,	-1.96E-06,	-1.14E-06,	-7.49E-07,	-5.24E-07,	-3.83E-07,	-2.88E-07,	-2.22E-07,	-1.74E-07,	-1.38E-07,	-1.12E-07,	-9.14E-08])
#susc=4
fz_data_0040=np.array([-6.46E-06,	-2.28E-06,	-1.31E-06,	-8.55E-07,	-5.96E-07,	-4.34E-07,	-3.26E-07,	-2.51E-07,	-1.96E-07,	-1.56E-07,	-1.26E-07,	-1.03E-07])
#susc=4.5
fz_data_0045=np.array([-7.84E-06,	-2.59E-06,	-1.47E-06,	-9.54E-07,	-6.63E-07,	-4.82E-07,	-3.61E-07,	-2.77E-07,	-2.17E-07,	-1.73E-07,	-1.40E-07,	-1.14E-07])

fz_data=np.array([fz_data_0010,fz_data_0015,fz_data_0020,fz_data_0025,fz_data_0030,fz_data_0035,fz_data_0040,fz_data_0045])
data_H1_a1_th0=pd.DataFrame(fz_data.transpose(),columns=['1.0','1.5','2.0','2.5','3.0','3.5','4.0','4.5'])
#data_H1_a1_th0=pd.DataFrame()
data_H1_a1_th0['c']=c_data
data_H1_a1_th0.set_index('c', inplace=True)
data_H1_a1_th0.to_csv('Data/data_H1_a1_th0.csv')