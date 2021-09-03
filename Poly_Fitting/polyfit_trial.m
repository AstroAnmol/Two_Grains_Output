% Trial for polyfit and polyval
c=2:0.2:4.2; % Separation Distance (in terms of a)

% fz (e-13 N) for 6G, 1.4 micrometer and susc 0.96.
fz=[-2.30930	-1.32304	-0.86401	-0.60076	-0.43492...
    -0.32432	-0.24752	-0.19255	-0.15222	-0.12202...
    -0.09902	-0.08122]; 
c_inv=1./c;
p=polyfit(c_inv,fz,7)
