import numpy as np
from sympy import integrate, symbols, Matrix
from Single_FGM import E_z, e

z = symbols('z')

E = integrate(E_z, (z, -1/2, 1/2))
nu = 0.3

Q = Matrix([
    [0,0,0],
    [0,0,0],
    [0,0,0]
])

Q[0,0] = Q[1,1] = E/(1-nu**2)
Q[0,1] = Q[1,0] = (nu*E)/(1-nu**2)
Q[2,2] = E/(2*(1+nu))

B = np.zeros((3, 3))
for i in range(3):
    for j in range(3):
        B[i,j] = integrate(Q[i,j]*z, (z, -1/2, 1/2))

if (B[0,0] == 0):
    B11 = 0
else:
    B11 = np.linalg.inv(B)[0,0]
#B11 = 0

D = np.zeros((3, 3))
for ii in range(3):
    for jj in range(3):
        D[ii,jj] = integrate((Q[ii,jj]*((z)**2)), (z, -1/2, 1/2))
D11 = np.linalg.inv(D)[0,0]

m1111 = -integrate( ( (E)*( B11 + (z)*D11) ), (z, -0.5, z) )
s55 = (2*(1+nu))/(E)

H55 = ( integrate( (s55*(m1111**2)), (z, -0.5, 0.5) ) )**-1

k55 = integrate(s55, (z, -0.5, 0.5))*H55
print(k55)

k = (1/12)**2/( 1*(integrate( integrate( z, (z, -0.5, z) )**2, (z, -0.5, 0.5) )) )
print(k)
