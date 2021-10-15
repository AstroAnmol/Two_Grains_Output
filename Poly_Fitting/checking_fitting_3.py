#Parallel Case (Cubic Polynomial)

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

susc_data=np.array([0.25,	0.5,	0.75,	1,	1.5,	2,	2.5,	3,	3.5,	4,	4.5,	5,	5.5,	6,	6.5,	7,	7.5,	8])
c_data = np.linspace(2,4.2,12)

susc_susc, c_c = np.meshgrid(susc_data,c_data)

## Suscpetibility based

# model function F = muo*(Fdm + p1/r^5 + p2/r^6 + p3/r^7)
def func_og(data, a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3):
    c=data[0]
    susc=data[1]
    mu0=4.0*np.pi*1e-7
    susc_eff=3*susc/(3+susc)
    p1=a1*(susc**3) + b1*(susc**2) + c1*(susc) + d1
    p2=a2*(susc**3) + b2*(susc**2) + c2*(susc) + d2
    p3=a3*(susc**3) + b3*(susc**2) + c3*(susc) + d3
    F_DM=4*np.pi*susc_eff**2/(3*c**4)
    return mu0*(F_DM + p1/(c**5) + p2/(c**6) + p3/(c**7))

# model function F = muo*(po/r^4 + p1/r^5 + p2/r^6 + p3/r^7)
def func_vary(data, a0, b0, c0, d0, a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3):
    c=data[0]
    susc=data[1]
    mu0=4.0*np.pi*1e-7
    susc_eff=3*susc/(3+susc)
    p0=a0*(susc**3) + b0*(susc**2) + c0*(susc) + d0
    p1=a1*(susc**3) + b1*(susc**2) + c1*(susc) + d1
    p2=a2*(susc**3) + b2*(susc**2) + c2*(susc) + d2
    p3=a3*(susc**3) + b3*(susc**2) + c3*(susc) + d3
    return mu0*(p0/(c**4) + p1/(c**5) + p2/(c**6) + p3/(c**7))

#Parameters
    #original
params=np.array([1.31198199, -82.14110991, 114.4557932, -39.79210857, -7.68819096, 449.9106508, -611.5820138, 210.3711939, \
    11.49729053, -610.1528645, 786.9320166, -264.7552372]) 
    #varied
params_vary=np.array([-0.70279873, 79.72887768, -129.4843025, 46.08305654, 6.83399346, -695.6784868, 1054.342322, -378.1589243, \
    -21.57297844, 1992.615126, -2974.872714, 1061.175141, 22.91004143, -1878.194582, 2729.463034, -964.0822822])

# ## Effective Suscpetibility based

# # model function F = muo*(Fdm + p1/r^5 + p2/r^6 + p3/r^7)
# def func_og(data, a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3):
#     c=data[0]
#     susc=data[1]
#     mu0=4.0*np.pi*1e-7
#     susc_eff=3*susc/(3+susc)
#     p1=a1*(susc_eff**3) + b1*(susc_eff**2) + c1*(susc_eff) + d1
#     p2=a2*(susc_eff**3) + b2*(susc_eff**2) + c2*(susc_eff) + d2
#     p3=a3*(susc_eff**3) + b3*(susc_eff**2) + c3*(susc_eff) + d3
#     F_DM=4*np.pi*susc_eff**2/(3*c**4)
#     return mu0*(F_DM + p1/(c**5) + p2/(c**6) + p3/(c**7))

# # model function F = muo*(po/r^4 + p1/r^5 + p2/r^6 + p3/r^7)
# def func_vary(data, a0, b0, c0, d0, a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3):
#     c=data[0]
#     susc=data[1]
#     mu0=4.0*np.pi*1e-7
#     susc_eff=3*susc/(3+susc)
#     p0=a0*(susc_eff**3) + b0*(susc_eff**2) + c0*(susc_eff) + d0
#     p1=a1*(susc_eff**3) + b1*(susc_eff**2) + c1*(susc_eff) + d1
#     p2=a2*(susc_eff**3) + b2*(susc_eff**2) + c2*(susc_eff) + d2
#     p3=a3*(susc_eff**3) + b3*(susc_eff**2) + c3*(susc_eff) + d3
#     return mu0*(p0/(c**4) + p1/(c**5) + p2/(c**6) + p3/(c**7))

# #Parameters
#     #original
# params=np.array([-1680.964425, 4341.955037, -3389.482164, 700.6027091, 9068.105659, -23362.69492, 18226.74997, -3766.233961, \
#     -12010.89806, 30801.03636, -24012.0366, 4959.73752]) 
#     #varied
# params_vary=np.array([1785.59961, -4677.810955, 3658.944886, -757.9334926, -15456.07901, 40364.57653, -31616.62959, 6547.725445, \
#     43704.83787, -113939.502, 89202.28688, -18468.48752, -40480.91228, 105251.5642, -82351.10161, 17044.40468])
#     #initial
# params=np.array([2.1679403, -5.10571752, 0.91979498, -0.14520514, -11.99291281, 32.60814942, -8.5414691, 1.26892871, \
#     12.57083862, -53.1809105, 17.62267505, -2.66077834]) 

fz_og=func_og((c_c,susc_susc), *params)
fz_vary=func_vary((c_c,susc_susc), *params_vary)

# print(func_og(2,0.25))

for ind in range(18):
    susc_strings=np.array(['0.25','0.5','0.75','1.0','1.5','2.0','2.5','3.0','3.5','4.0','4.5','5.0','5.5','6.0','6.5','7.0','7.5','8.0'])
    data_H1_a1_th00=pd.read_csv('Data/data_H1_a1_th0.csv')
    fz_data=data_H1_a1_th00[susc_strings[ind]]
    fz_og_data=fz_og[:,ind]
    fz_vary_data=fz_vary[:,ind]

    #
    squaresum = np.sum((fz_data-np.mean(fz_data))**2)
    l_sq_err_og=np.sum(fz_og_data-fz_data)**2
    R2_og = 1 - (l_sq_err_og/squaresum)
    l_sq_err_vary=np.sum(fz_vary_data-fz_data)**2
    R2_vary = 1 - (l_sq_err_vary/squaresum)
    # print('Least squares error (FDM)',l_sq_err_og)
    # print('R^2 value (FDM)',R2_og)
    # print('Least squares error (vary)',l_sq_err_vary)
    # print('R^2 value (vary)',R2_vary)

    # plot
    plt.figure()
    plt.plot(c_data,fz_data,'b+',label="multipole data")
    plt.plot(c_data,fz_og_data,'r-',label=("fitting with F_DM ($R^2$ %% =%5.3f)" %(R2_og*100)))
    plt.plot(c_data,fz_vary_data,'g--',label=("fitting with p0 ($R^2$ %% =%5.3f)" %(R2_vary*100)))
    plt.xlabel('c')
    plt.ylabel('fz (N)')
    plt.title(r"a=1 m, H0=1 A/m, $\theta$=0, $\chi=$"+susc_strings[ind])
    # plt.title(r"a=1 m, H0=1 A/m, $\theta$=0, $\chi=$"+susc_strings[ind]+ "(based on $\chi_{eff}$)")
    # plt.title("a=1 m, H0=1 A/m, $\theta$=0, $\chi=$"+susc_strings[ind]+ "(based on $\chi_{eff}$ and initial guess)")
    plt.grid('on')
    plt.legend()
    # plt.show()
    susc_strings=np.array(['0,25','0,50','0,75','1,0','1,5','2,0','2,5','3,0','3,5','4,0','4,5','5,0','5,5','6,0','6,5','7,0','7,5','8,0'])
    plt.savefig('Plots/Fitting/Parallel_Case/Cubic_Poly/Complete_Model_Function/Susceptibility_Based/a_1_H0_1_th_0_chi_'+susc_strings[ind]+'.png')
    # plt.savefig('Plots/Fitting/Parallel_Case/Cubic_Poly/Complete_Model_Function/Effective_Susceptibility_Based/a_1_H0_1_th_0_chi_'+susc_strings[ind]+'_chi_eff'+'.png')
    # plt.savefig('Plots/Fitting/Parallel_Case/Cubic_Poly/Complete_Model_Function/Effective_Susceptibility_Initial/a_1_H0_1_th_0_chi_'+susc_strings[ind]+'_chi_eff'+'.png')
