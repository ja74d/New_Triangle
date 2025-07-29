import numpy as np
from sympy import symbols, integrate

#Geometrical Properties

t1, t2, t3 = 1, 2, 1

###FGM

#volume fraction index
n = 2


#Ceramic-Aluminum
Ec = 380e+09
alphac = 7.4e-6
Em = 70e+09
alpham = 23e-6
nu = 0.3
h_ = t1 + t2 + t3

t1 = t1/h_
t2 = t2/h_
t3 = t3/h_

h0 = -(t1+t2+t3)/2
h1 = h0 + t1
h2 = h1 + t2
h3 = h2 + t3

h = h0 + h1 + h2 + h3

#==========bottom--1.5-metal
#                                                  |-z
#++++++++++core             -----------------------|
#                                                  |+z
#========== top-1.5-metal

#Linear Temperature Change Through the Thickness
def T(T0, deltaT):
    #return (Tbottom + ( (Ttop - Tbottom)/h )*z)
    return T0+deltaT
#Temperature at top
T = T(300, 600)

#Tempreture Dependent Material Properties
def TDP(P0, P_1, P1, P2, P3, T):
    P = P0*( P_1*(T**-1) +1 + P1*T + P2*(T**2) +P3*(T**3) )
    return P

z = symbols('z')

#Simple Power Law
#if h0<h<h1 ===> Vn = ((z-h0)/(h1-h0))^n
#if h2<h<h3 ===> Vn = ((z-h3)/(h2-h3))^n

def powerlaw_bottom(n, pc, pm, h0, h1):
    Vbottom = ((z-h0)/(h1-h0))**n
    return (pc-pm)*Vbottom + pm

E_z_bottom = powerlaw_bottom(n, Ec, Em, h0, h1)
alpha_z_bottom = powerlaw_bottom(n, alphac, alpham, h0, h1)

def powerlaw_top(n, pc, pm, h2, h3):
    Vtop = ((z-h3)/(h2-h3))**n
    return (pc-pm)*Vtop + pm

E_z_top = powerlaw_top(n, Ec, Em, h2, h3)
alpha_z_top = powerlaw_top(n, alphac, alpham, h2, h3)

def powerlaw(n, pc, pm):
    return (pc-pm)*((z/h + 0.5)**n) + pm

alpha_top = powerlaw(n, alphac, alpham)
alpha_bottom = powerlaw(n, alphac, alpham)

E_top = powerlaw(n, Ec, Em)
E_bottom = powerlaw(n, Ec, Em)