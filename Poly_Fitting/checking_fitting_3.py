#Parallel Case (Cubic Polynomial)

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

susc_data=np.array([0.1,0.15,0.2,0.25,0.5,0.75,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,\
    7.5,8.0,8.5,9.0,9.5,10.0,10.5,11.0,11.5,12.0,15.0,20.0,25.0,30.0,35.0,40.0,45.0,50.0,55.0,60.0,65.0,70.0,75.0,80.0,85.0,90.0,95.0,100.0])
c_data = np.linspace(2.2,4.2,11)

susc_susc, c_c = np.meshgrid(susc_data,c_data)

# ## Suscpetibility based

# # model function F = muo*(Fdm + p1/r^5 + p2/r^6 + p3/r^7)
# def func_og(data, a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3):
#     c=data[0]
#     susc=data[1]
#     mu0=4.0*np.pi*1e-7
#     susc_eff=3*susc/(3+susc)
#     p1=a1*(susc**3) + b1*(susc**2) + c1*(susc) + d1
#     p2=a2*(susc**3) + b2*(susc**2) + c2*(susc) + d2
#     p3=a3*(susc**3) + b3*(susc**2) + c3*(susc) + d3
#     F_DM=4*np.pi*susc_eff**2/(3*c**4)
#     return mu0*(F_DM + p1/(c**5) + p2/(c**6) + p3/(c**7))

# # model function F = muo*(po/r^4 + p1/r^5 + p2/r^6 + p3/r^7)
# def func_vary(data, a0, b0, c0, d0, a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3):
#     c=data[0]
#     susc=data[1]
#     mu0=4.0*np.pi*1e-7
#     susc_eff=3*susc/(3+susc)
#     p0=a0*(susc**3) + b0*(susc**2) + c0*(susc) + d0
#     p1=a1*(susc**3) + b1*(susc**2) + c1*(susc) + d1
#     p2=a2*(susc**3) + b2*(susc**2) + c2*(susc) + d2
#     p3=a3*(susc**3) + b3*(susc**2) + c3*(susc) + d3
#     return mu0*(p0/(c**4) + p1/(c**5) + p2/(c**6) + p3/(c**7))

# #Parameters
#     #original
# params=np.array([-0.03562863, 0.61172073, -2.70956668, 0.63888614, 0.16353389, -3.0435703, 16.17696363, -4.3861996, \
#     0.16353389, -3.0435703, 16.17696363, -4.3861996]) 
#     #varied
# params_vary=np.array([0.01786655, -0.47992324, 4.22817664, -1.26463416, -0.22357326, 3.54618869, -5.81412107, 1.82313041, \
#     0.63610746, -10.4220993, 23.98314026, -7.36389373, -0.47999317, 8.78829318, -34.29359611, 11.49288475])

## Effective Suscpetibility based

# model function F = muo*(Fdm + p1/r^5 + p2/r^6 + p3/r^7)
def func_og(data, a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3):
    c=data[0]
    susc=data[1]
    mu0=4.0*np.pi*1e-7
    susc_eff=3*susc/(3+susc)
    p1=a1*(susc_eff**3) + b1*(susc_eff**2) + c1*(susc_eff) + d1
    p2=a2*(susc_eff**3) + b2*(susc_eff**2) + c2*(susc_eff) + d2
    p3=a3*(susc_eff**3) + b3*(susc_eff**2) + c3*(susc_eff) + d3
    F_DM=4*np.pi*susc_eff**2/(3*c**4)
    return mu0*(F_DM + p1/(c**5) + p2/(c**6) + p3/(c**7))

# model function F = muo*(po/r^4 + p1/r^5 + p2/r^6 + p3/r^7)
def func_vary(data, a0, b0, c0, d0, a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3):
    c=data[0]
    susc=data[1]
    mu0=4.0*np.pi*1e-7
    susc_eff=3*susc/(3+susc)
    p0=a0*(susc_eff**3) + b0*(susc_eff**2) + c0*(susc_eff) + d0
    p1=a1*(susc_eff**3) + b1*(susc_eff**2) + c1*(susc_eff) + d1
    p2=a2*(susc_eff**3) + b2*(susc_eff**2) + c2*(susc_eff) + d2
    p3=a3*(susc_eff**3) + b3*(susc_eff**2) + c3*(susc_eff) + d3
    return mu0*(p0/(c**4) + p1/(c**5) + p2/(c**6) + p3/(c**7))

#Parameters
#     #original
# params=np.array([2.1679403, -5.10571752, 0.91979498, -0.14520514, -11.99291281, 32.60814942, -8.5414691, 1.26892871, \
#     12.57083862, -53.1809105, 17.62267505, -2.66077834]) 
#     #varied
# params_vary=np.array([-2.35006285, 8.70658619, -2.96749461, 0.51760021, 20.29772718, -39.95880704, 23.81296509, -4.13832093, \
#     -57.57941163, 120.244874, -66.10561194, 11.3095235, 50.04124488, -125.2151948, 64.93845222, -10.91382394])
    #initial
params=np.array([-497.95224865,   2671.56697629,  -5718.94770409,   4061.8828376,
   2944.52379528, -16054.0668261,   33639.65154115, -23897.55494789,
  -4317.45216271,  23490.26719675, -48875.99378488,  34745.55102049]) 

fz_og=func_og((c_c,susc_susc), *params)
# fz_vary=func_vary((c_c,susc_susc), *params_vary)

# print(func_og(2,0.25))

for ind in range(susc_data.size):
    susc_strings=np.array(['0.1','0.15','0.2','0.25','0.5','0.75','1.0','1.5','2.0','2.5','3.0','3.5','4.0','4.5','5.0','5.5','6.0','6.5','7.0',\
    '7.5','8.0','8.5','9.0','9.5','10.0','10.5','11.0','11.5','12.0','15.0','20.0','25.0','30.0','35.0','40.0','45.0','50.0','55.0','60.0','65.0','70.0','75.0','80.0','85.0','90.0','95.0','100.0'])
    data_H1_a1_th00=pd.read_csv('Data/csv_files/data_H1_a1_th0.csv')
    data_H1_a1_th00=data_H1_a1_th00.iloc[1:]
    fz_data=data_H1_a1_th00[susc_strings[ind]]
    fz_og_data=fz_og[:,ind]
    # fz_vary_data=fz_vary[:,ind]

    #
    squaresum = np.sum((fz_data-np.mean(fz_data))**2)
    l_sq_err_og=np.sum(fz_og_data-fz_data)**2
    R2_og = 1 - (l_sq_err_og/squaresum)
    # l_sq_err_vary=np.sum(fz_vary_data-fz_data)**2
    # R2_vary = 1 - (l_sq_err_vary/squaresum)
    # print('Least squares error (FDM)',l_sq_err_og)
    # print('R^2 value (FDM)',R2_og)
    # print('Least squares error (vary)',l_sq_err_vary)
    # print('R^2 value (vary)',R2_vary)

    # plot
    plt.figure()
    plt.plot(c_data,fz_data,'b+',label="multipole data")
    plt.plot(c_data,fz_og_data,'r-',label=("fitting with F_DM ($R^2$ %% =%5.3f)" %(R2_og*100)))
    # plt.plot(c_data,fz_vary_data,'g--',label=("fitting with p0 ($R^2$ %% =%5.3f)" %(R2_vary*100)))
    plt.xlabel('c')
    plt.ylabel('fz (N)')
    # plt.title(r"a=1 m, H0=1 A/m, $\theta$=0, $\chi=$"+susc_strings[ind])
    # plt.title(r"a=1 m, H0=1 A/m, $\theta$=0, $\chi=$"+susc_strings[ind]+ "(based on $\chi_{eff}$)")
    plt.title(r"a=1 m, H0=1 A/m, $\theta$=0 deg, $\chi=$"+susc_strings[ind])#+ "(based on $\chi_{eff}$ and initial guess)")
    plt.grid('on')
    plt.legend()
    # plt.show()
    susc_strings=np.array(['0.1','0.15','0.2','0.25','0.5','0.75','1.0','1.5','2.0','2.5','3.0','3.5','4.0','4.5','5.0','5.5','6.0','6.5','7.0',\
    '7.5','8.0','8.5','9.0','9.5','10.0','10.5','11.0','11.5','12.0','15.0','20.0','25.0','30.0','35.0','40.0','45.0','50.0','55.0','60.0','65.0','70.0','75.0','80.0','85.0','90.0','95.0','100.0'])
    # plt.savefig('Plots/Fitting/Parallel_Case/Complete_Model_Function/Susceptibility_Based/a_1_H0_1_th_00_chi_'+susc_strings[ind]+'.png')
    # plt.savefig('Plots/Fitting/Parallel_Case/Complete_Model_Function/Effective_Susceptibility_Based/a_1_H0_1_th_00_chi_'+susc_strings[ind]+'_chi_eff'+'.png')
    plt.savefig('Plots/Fitting/Parallel_Case/Cubic_Poly/Complete_Model_Function/Effective_Susceptibility_Initial/a_1_H0_1_th_00_chi_'+susc_strings[ind]+'_chi_eff'+'.png', bbox_inches='tight')
    plt.close()