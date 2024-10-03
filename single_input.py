from math import sqrt, cos, sin, radians

r1 = 5
r2 = 5.01
t1 = 18
t2 = 50
t3 = 62
pi = 180

AB = sqrt(r1**2 + r2**2 - (2*r1*r2*cos(radians(pi-t3))))
CD = sqrt(r1**2 + r2**2 - (2*r1*r2*cos(radians(t2-t1))))
BC = sqrt(r1**2 + r2**2 - (2*r1*r2*cos(radians(t3-t2))))
# print(BC)
sin_ABO = (r2/AB)*sin(radians(pi-t3))
sin_CBO = (r2/BC)*sin(radians(t3-t2))
# print(sin_ABO**2)
cos_ABO = sqrt(1-sin_ABO**2)
cos_CBO = sqrt(1-sin_CBO**2)
sin_IBC = sin_ABO*cos_CBO+cos_ABO*sin_CBO
sin_BCO = (r1/BC)*sin(radians(t3-t2))
sin_OCD = (r1/CD)*sin(radians(t2-t1))
cos_BCO = sqrt(1-sin_BCO**2)
cos_OCD = sqrt(1-sin_OCD**2)
sin_ICB = sin_OCD*cos_BCO+cos_OCD*sin_BCO
cos_IBC = sqrt(1-sin_IBC**2)
cos_ICB = sqrt(1-sin_ICB**2)
sin_BIC = sin_IBC*cos_ICB+cos_IBC*sin_ICB
IB = BC*(sin_ICB/sin_BIC)
IC = BC*(sin_IBC/sin_BIC)
am = (pi-t3)/2
rm = (2*sin(radians(am))*(r2**3-r1**3)) / (3*am*(r2**2-r1**2)) #sin?
sm = am*(r2**2-r1**2)
Am = sqrt(rm**2+r2**2-(2*rm*r2*cos(radians(am))))
ap = (t2-t1)/2
rp = (2*sin(radians(ap))*(r2**3-r1**3)) / (3*ap*(r2**2-r1**2)) #sin?
sp = ap*(r2**2-r1**2)
dp = sqrt(rp**2+r1**2-(2*rp*r1*cos(radians(t2-t1))))
an = (t3-t2)/2
rn = (2*sin(radians(an))*(r2**3-r1**3)) / (3*an*(r2**2-r1**2))
sn = an*(r2**2-r1**2)
nc = sqrt(rn**2+r2**2-(2*rn*r2*cos(radians((t3-t2)/2))))
nb = sqrt(rn**2+r1**2-(2*rn*r1*cos(radians((t3-t2)/2))))
cos_NCB = (nc**2+BC**2-nb**2) / (2*nc*BC)
sin_NCB = sqrt(1-cos_NCB**2)
sin_OCB = (r1/BC)*sin(radians(t3-t2))
cos_OCB = sqrt(1-sin_OCB**2)
cos_NCI = -1*(cos_OCD*cos_OCB*cos_NCB)+sin_OCD*sin_OCB*cos_NCB+sin_OCD*cos_OCB*sin_NCB+cos_OCD*sin_OCB*sin_NCB #cos_OCB -?
In = sqrt(IC**2+nc**2-(2*IC*nc*cos_NCI))
# rm = sqrt(Am**2+r2**2-(2*Am*r2*cos_AMO)) #cos_MAO?
cos_MAO = (Am**2+r2**2-rm**2) / (2*Am*r2)
sin_MAO = sqrt(1-cos_MAO**2) #**2?
sin_POX = sin(radians((t1+t2)/2))
cos_POX = cos(radians((t1+t2)/2))

Wm = (-1*sm)*Am*cos_MAO
Wn = (-1*sn)*(In/IB)*AB*cos(radians((t2+t3)/2))
Wp = sp*AB*(IC/IB)*(dp/CD)*cos_POX
Wt = Wm+Wn+Wp
WY_me = sm*Am*sin_MAO
WY_ne = (-1*sn)*(In/IB)*AB*sin(radians((t2+t3)/2))
WY_pe = sp*AB*(IC/IB)*(dp/CD)*cos_POX
WY_t = WY_me+WY_ne+WY_pe
Y = Wt/WY_t

print(Y)