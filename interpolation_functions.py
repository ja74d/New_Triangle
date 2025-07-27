import sympy as sp
import numpy as np

#Symboles
k, e = sp.symbols('k e')
#k for kesi
#e for eta

#Lagrangian Interpolation Functions

N1 = k*(2*k-1)
N2 = e*(2*e-1)
N3 = (1-k-e)*(1-(2*k)-(2*e))
N4 = 4*k*e
N5 = 4*e*(1-k-e)
N6 = 4*k*(1-k-e)

N = np.array([N1, N2, N3, N4, N5, N6])
Nw = np.array([N[0], 0, 0, 0, 0, N[1], 0, 0, 0, 0, N[2], 0, 0, 0, 0, N[3], 0, 0, 0, 0, N[4], 0, 0, 0, 0, N[5], 0, 0, 0, 0])

dNdk = [sp.diff(N[0], k), sp.diff(N[1], k), sp.diff(N[2], k), sp.diff(N[3], k), sp.diff(N[4], k), sp.diff(N[5], k)]
dNde = [sp.diff(N[0], e), sp.diff(N[1], e), sp.diff(N[2], e), sp.diff(N[3], e), sp.diff(N[4], e), sp.diff(N[5], e)]

#Nwf_dk = np.array([dNdk[0], 0, 0, 0, 0, dNdk[1], 0, 0, 0, 0, dNdk[2], 0, 0, 0, 0, dNdk[3], 0, 0 ,0 , 0, dNdk[4], 0, 0, 0 ,0 , dNdk[5], 0, 0, 0, 0])
#Nwf_de = np.array([dNde[0], 0, 0, 0, 0, dNde[1], 0, 0, 0, 0, dNde[2], 0, 0, 0, 0, dNde[3], 0, 0 ,0 , 0, dNde[4], 0, 0, 0 ,0 , dNde[5], 0, 0, 0, 0])

wanker = sp.zeros(30, 30)
for i in range(0, 30):
    for j in range(0, 30):
        wanker[i, j]=Nw[i]*Nw[j]