import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# model function F = muo*(F_DM + p1/r^5 + p2/r^6 + p3/r^7)
def func_og(c, susc):
    mu0=4.0*np.pi*1e-7
    susc_eff=3*susc/(3+susc)
    F_DM=-8*np.pi*susc_eff**2/(3*c**4)
    p1=-39.06*(susc**2.195)
    p2=219.869*(susc**2.179)
    p3=-314.819*(susc**2.149)
    return mu0*(F_DM + p1/(c**5) + p2/(c**6) + p3/(c**7))

# model function F = mu0*(p0/r^4 + p1/r^5 + p2/r^6 + p3/r^7)
def func_vary(c, susc):
    mu0=4.0*np.pi*1e-7
    p0= 31.406*(susc**2.306)	
    p1=-298.676*(susc**2.267)
    p2=	871.245*(susc**2.255)
    p3=-847.429*(susc**2.236)
    return mu0*(p0/(c**4) + p1/(c**5) + p2/(c**6) + p3/(c**7))

susc_data=np.array([0.25,	0.5,	0.75,	1,	1.5,	2,	2.5,	3,	3.5,	4,	4.5,	5,	5.5,	6,	6.5,	7,	7.5,	8])
c_data = np.linspace(2,4.2,12)

susc_susc, c_c = np.meshgrid(susc_data,c_data)

fz_og=func_og(c_c,susc_susc)
fz_vary=func_vary(c_c,susc_susc)

# print(func_og(2,0.25))

for ind in range(18):
    susc_strings=np.array(['0.25','0.5','0.75','1.0','1.5','2.0','2.5','3.0','3.5','4.0','4.5','5.0','5.5','6.0','6.5','7.0','7.5','8.0'])
    data_H1_a1_th0=pd.read_csv('Data/data_H1_a1_th0.csv')
    fz_data=data_H1_a1_th0[susc_strings[ind]]
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
    plt.plot(c_data,fz_data,'r-',label="multipole data")
    plt.plot(c_data,fz_og_data,'b+',label=("fitting with F_DM ($R^2$ %% =%5.3f)" %(R2_og*100)))
    plt.plot(c_data,fz_vary_data,'go',label=("fitting with p0 ($R^2$ %% =%5.3f)" %(R2_vary*100)))
    plt.xlabel('c')
    plt.ylabel('fz (N)')
    plt.title("a=1 m, H0=1 A/m, $\theta$=0, $\chi=$"+susc_strings[ind])
    plt.grid('on')
    plt.legend()
    # plt.show()
    susc_strings=np.array(['0,25','0,50','0,75','1,0','1,5','2,0','2,5','3,0','3,5','4,0','4,5','5,0','5,5','6,0','6,5','7,0','7,5','8,0'])
    plt.savefig('Plots/Fitting/Complete_Model_Function/a_1_H0_1_th_0_chi_'+susc_strings[ind]+'.png')
