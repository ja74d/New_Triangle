import numpy as np
import sympy as sp
from scipy.linalg import eig
#from READ_HDF5 import K, Kg
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import inv
from app import K, Kg
from input import Lx, Em

#eigenvalues, eigenvectors = eig(K, Kg)
#print(min(eigenvalues))

K = csr_matrix(K)
K = K.tocsc()
Kg = csr_matrix(Kg)
Kg = Kg.tocsc()

rw = K.shape[0]

xk = []
xk_ = []
yk = []
yk_ = []

#A_inv = np.linalg.inv(K)
A_inv = inv(K)

def x(A, B, x):    
    xi_ = A_inv @ B @ x
    yk.append(A@xi_)
    yk_.append(B@xi_)
    xk_.append(xi_)
    weight = xi_.T @ B @ xi_
    xi = (1/(abs(weight)**0.5))*xi_
    return xi

for i in range(15):
    if i == 0:
        xi = np.ones(rw).T
        #xi = np.random.rand(rw)
    else:
        xi = x(K, Kg, xi)
        xk.append(xi)
#print(xi[0])
rho = ( xk_[i-1].T @ yk[i-1] )/( xk_[i-1].T @ yk_[i-1] )

#thermal buckling
#print(rho*1e-3)

#mechanical buckling
#print(rho*1e-9)
print( (rho *Lx**2)/(100*1e+9) )

#print(rho)
#print(rho*((Lx**2)/(Em)))


#check results
#x1 = np.array([1, 1, 1, 1]).T
#print('=============================================')
##x1 = xi.T @ B @ xi
#x2 = np.linalg.inv(A) @ B @ x1
#weight = x2.T @ B @ x2
#x2 = (1/(weight**0.5))*x2
#print(x2)

#x3 = np.linalg.inv(A) @ B @ x2
#weight = x3.T @ B @ x3
#x3 = (1/(weight**0.5)) * x3
#print(x3)

