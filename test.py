for k in range(1, m+1) :
    r2 = k*dr+r1
    x.append(r2)
    ans = {
        "Y" : 1e9,
        "r1" : 0,
        "r2" : 0,
        "dr" : 0,
        "k" : 0,
        "t1" : 0,
        "t2" : 0,
        "t3" : 0,
    }
    for t1 in range(0, 46):
        for t2 in range(60, 81):
            for t3 in range(120, 161):
                # for line in lines:
                #     try:
                #         exec(line)
                #     except:
                #         print("error")
                AB = sqrt(r1**2 + r2**2 - (2*r1*r2*cos(radians(Pi-t3))))
                CD = sqrt(r1**2 + r2**2 - (2*r1*r2*cos(radians(t2-t1))))
                BC = sqrt(r1**2 + r2**2 - (2*r1*r2*cos(radians(t3-t2))))
                sin_ABO = (r2/AB)*sin(radians(Pi-t3))
                sin_CBO = (r2/BC)*sin(radians(t3-t2))
                cos_ABO = (((AB**2)+(r1**2))- (r2**2))/(2*AB*r1)
                cos_CBO = (((BC**2)+(r1**2))- (r2**2))/(2*BC*r1)
                sin_IBC = (sin_ABO*cos_CBO)+(cos_ABO*sin_CBO)  #!
                sin_BCO = (r1/BC)*sin(radians(t3-t2))
                sin_OCD = (r1)*sin(radians(t2-t1))/CD
                cos_BCO = (((BC**2)+(r2**2))- (r1**2))/(2*BC*r2) #!
                cos_OCD = (((CD**2)+(r2**2))- (r1**2))/(2*CD*r2) #!
                #print(cos_OCD)
                sin_ICB = sin_OCD*cos_BCO+cos_OCD*sin_BCO
                cos_IBC= cos(asin(sin_IBC))
                cos_ICB = ((-1)*cos_OCD*cos_BCO)+((sin_OCD)*(sin_BCO)) #!
                sin_BIC = sin_IBC*cos_ICB+cos_IBC*sin_ICB
                #print(sin_BIC)
                IB = BC*(sin_ICB/sin_BIC)
                IC = BC*(sin_IBC/sin_BIC)  #?????????????????
                #print(IC) #true
                am = (Pi-t3)/2
                rm =(2*sin(radians(am))*(r2**3-r1**3)) / (3*radians(am)*(r2**2-r1**2)) #???????????
                #print(rm)
                sm = radians(am)*(r2**2-r1**2)
                Am = sqrt(rm**2+r2**2-(2*rm*r2*cos(radians(am))))
                ap = (t2-t1)/2
                rp = (2*sin(radians(ap))*(r2**3-r1**3)) / (3*radians(ap)*(r2**2-r1**2))
                #print(rp)
                sp = radians(ap)*(r2**2-r1**2)
                #print(sp)
                dp = sqrt(rp**2+r1**2-(2*rp*r1*cos(radians(t2-t1)/2)))  #+++
                an = (t3-t2)/2
                rn = (2*sin(radians(an))*(r2**3-r1**3)) / (3*radians(an)*(r2**2-r1**2))
                #print(rn)
                sn = radians(an)*(r2**2-r1**2)
                #print(sn)
                nc = sqrt(rn**2+r2**2-(2*rn*r2*cos(radians((t3-t2)/2))))
                nb = sqrt(rn**2+r1**2-(2*rn*r1*cos(radians((t3-t2)/2))))
                #print(nb)
                cos_NCB = (nc**2+BC**2-nb**2) / (2*nc*BC)
                sin_NCB = sqrt(1-cos_NCB**2)
                sin_OCB = (r1/BC)*sin(radians(t3-t2))
                #print(sin_OCB)
                cos_OCB = (((BC**2)+(r2**2))- (r1**2))/(2*BC*r2)
                v = (2)*degrees((asin(sin_OCD)+asin(sin_OCB)+asin(sin_NCB)))
                sin_BAO= (r1*sin_ABO)/r2
                IA= AB + IB
                IO= sqrt(IA**2+r2**2-2*IA*r2*abs(cos(asin(sin_BAO))))
                if IO>r2:
                    NCI =Pi-degrees((asin(sin_OCD)+asin(sin_BCO)+asin(sin_NCB)))
                else :
                    NCI =degrees(asin(sin_OCD)+asin(sin_BCO)+asin(sin_NCB))
                #cos_NCI =((-1)*cos_OCD*cos_OCB*cos_NCB+sin_OCD*sin_OCB*cos_NCB+sin_OCD*cos_OCB*sin_NCB+cos_OCD*sin_OCB*sin_NCB)*pi/3.14
                #else:

                #print(cos_NCI)
                In = sqrt((IC**2+nc**2)-(2*abs(IC)*nc*(cos(radians(NCI)))))
                #print(In)
                cos_MAO = (Am**2+r2**2-rm**2) / (2*Am*r2)
                sin_MAO = sqrt(1-cos_MAO**2) #**2?
                sin_POX = sin(radians((t1+t2)/2))
                cos_POX = cos(radians((t1+t2)/2))
                #print(cos_POX)
                cos_NIC = (In**2+IC**2-nc**2) / (2*In*IC)
                sin_NIC = sqrt(1-(cos_NIC)**2)
                sin_INC = (abs(IC) * sin_NIC) / nc 
                f = degrees(asin(sin_INC))
                sin_CNO =(r2 / nc) * sin(radians((t3-t2)/2))
                g = abs(degrees(asin(sin_CNO)))
                if IO>r2:
                    NKX = f+g+((-1)*Pi)+(((t2+t3))/2)
                else :
                    NKX = -f+g+((-1)*Pi)+(((t2+t3))/2)

                Wm = ((-1*sm)*Am*abs(cos_MAO))
                Wn = ((-1*sn)*(In/IB)*AB*abs(cos(radians((NKX)))))
                Wp = (sp*AB*((abs(IC))/IB)*(dp/CD)*abs(cos_POX))
                Wt = (Wm)+(Wn)+(Wp) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                WY_me = sm*Am*abs(sin_MAO)
                WY_ne = (sn)*(In/IB)*AB*abs(sin(radians(NKX)))
                WY_pe = sp*AB*(abs(IC)/IB)*(dp/CD)*abs(sin_POX)
                WY_t = WY_me+WY_ne+WY_pe
                Y = abs(Wt/WY_t)

                # print(t1, t2, t3)
                if Y < ans["Y"]:
                    # print(Y)
                    ans = {
                        "Y" : Y,
                        "r1" : r1,
                        "r2" : r2,
                        "dr" : dr,
                        "k" : k,
                        "t1" : t1,
                        "t2" : t2,
                        "t3" : t3,
                    }
    y.append(ans["Y"])
    output.append(ans)
    print(ans)