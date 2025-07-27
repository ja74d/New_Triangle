import numpy as np
from sympy import Matrix, integrate, symbols
from Honeycomb import Gibson, Ceramic_only, sorhan
from FGM import E_z_top, E_z_bottom, h0, h1, h2, h3, nu, E_top, E_bottom, alpha_top, alpha_bottom, alpha_z_top, alpha_z_bottom, Ec, Em

z = symbols('z')

#E1, E2, G12, G13, G23, nu12, nu21, alpha = Gibson['E1'], Gibson['E2'], Gibson['G12'], Gibson['G13'], Gibson['G23'], Gibson['nu12'], Gibson['nu21'], Gibson['alpha']

E1, E2, G12, G13, G23, nu12, nu21, alpha = sorhan['E1'], sorhan['E2'], sorhan['G12'], sorhan['G13'], sorhan['G23'], sorhan['nu12'], sorhan['nu21'], sorhan['alpha']

#Locations of top and bottom of each layer of the laminate

ka = 5/6
ka_FGM = 5/6

#E1, E2, G12, G13, G23, nu12, nu21, alpha = Ceramic_only['E1'], Ceramic_only['E2'], Ceramic_only['G12'], Ceramic_only['G13'], Ceramic_only['G23'], Ceramic_only['nu12'], Ceramic_only['nu21'], Ceramic_only['alpha']

#Reduced stiffness matrix
def Q_(E_z, nu):
    Q = Matrix([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ])
    Q[0,0] = Q[1,1] = E_z/(1-nu**2)
    Q[0,1] = Q[1,0] = (nu*E_z)/(1-nu**2)
    Q[2,2] = E_z/(2*(1+nu))
    return Q

def Q_orth(E1, E2, G12, nu12, nu21):
    Qorth = Matrix([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ])
    Qorth[0, 0] = E1/(1-(nu12*nu21))
    Qorth[1, 1] = E2/(1-(nu12*nu21))
    Qorth[0, 1] = Qorth[1, 0] = (nu12*E2)/(1-(nu12*nu21))
    Qorth[2, 2] = G12
    return Qorth


def Qs_(E_z, nu):
    Qs = Matrix([
        [Q_(E_z, nu)[2,2], 0],
        [0, Q_(E_z, nu)[2,2]]
    ])
    return Qs

def Qs_orth(G23, G13):
    Qsorth = Matrix([
        [G23, 0],
        [0, G13]
    ])
    return Qsorth

#print(Q(Sandwich[0]))

#A
A = np.zeros((3, 3))
A2 = np.zeros((3, 3))

for i in range(3):
    for j in range(3):
        A[i,j] = ( integrate( Q_(E_z_bottom, nu)[i, j], (z, h0, h1) ) + integrate( Q_orth(E1, E2, G12, nu12, nu21)[i, j], (z, h1, h2) ) + integrate( Q_(E_z_top, nu)[i, j], (z, h2, h3) ) )
        #A[i,j] = ( integrate( Q_(E_z_bottom, nu)[i, j], (z, h0, h1) ) + integrate( Q_(Ec, nu)[i, j], (z, h1, h2) ) + integrate( Q_(E_z_top, nu)[i, j], (z, h2, h3) ) )
        #A2[i,j] = integrate( Q_(Ec, nu)[i, j], (z, h0, h1) ) + integrate( Q_(Ec, nu)[i, j], (z, h1, h2) ) + integrate( Q_(Ec, nu)[i, j], (z, h2, h3) )
#A_prime = np.linalg.inv(A)

#B
B = np.zeros((3, 3))
for i in range(3):
    for j in range(3):
        B[i,j] = integrate( Q_(E_z_bottom, nu)[i, j]*z, (z, h0, h1) ) + integrate( Q_orth(E1, E2, G12, nu12, nu21)[i, j]*z, (z, h1, h2) ) + integrate( Q_(E_z_top, nu)[i, j]*z, (z, h2, h3) )
        #B[i,j] = integrate( Q_(E_z_bottom, nu)[i, j]*z, (z, h0, h1) ) + integrate( Q_(Ec, nu)[i, j]*z, (z, h1, h2) ) + integrate( Q_(E_z_top, nu)[i, j]*z, (z, h2, h3) )

#D
D = np.zeros((3, 3))
D2 = np.zeros((3, 3))
for i in range(3):
    for j in range(3):
        D[i,j] = ( integrate( Q_(E_z_bottom, nu)[i, j]*(z)**2, (z, h0, h1) ) + integrate( Q_orth(E1, E2, G12, nu12, nu21)[i, j]*z**2, (z, h1, h2) ) + integrate( Q_(E_z_top, nu)[i, j]*(z)**2, (z, h2, h3) ) )
        #D[i,j] = ( integrate( Q_(E_z_bottom, nu)[i, j]*(z)**2, (z, h0, h1) ) + integrate( Q_(Ec, nu)[i, j]*z**2, (z, h1, h2) ) + integrate( Q_(E_z_top, nu)[i, j]*(z)**2, (z, h2, h3) ) )
        #D2[i,j] = integrate( Q_(Ec, nu)[i, j]*z**2, (z, h0, h1) ) + integrate( Q_(Ec, nu)[i, j]*z**2, (z, h1, h2) ) + integrate( Q_(Ec, nu)[i, j]*z**2, (z, h2, h3) )

#D_prime = np.linalg.inv(D)
#print(D)

#S
S = np.zeros((2, 2))
S2 = np.zeros((2, 2))
for i in range(2):
    for j in range(2):
        S[i,j] = (ka_FGM * integrate( Qs_(E_z_bottom, nu)[i,j], (z, h0, h1) ) + ka * integrate( Qs_orth(G23, G13)[i,j], (z, h1, h2) ) + ka_FGM * integrate( Qs_(E_z_top, nu)[i,j], (z, h2, h3) ) )
        #S[i,j] = (ka_FGM * integrate( Qs_(E_z_bottom, nu)[i,j], (z, h0, h1) ) + ka * integrate( Qs_(Ec, nu)[i,j], (z, h1, h2) ) + ka_FGM * integrate( Qs_(E_z_top, nu)[i,j], (z, h2, h3) ) )
        #S2[i,j] = ka * ( integrate( Qs_(Ec, nu)[i,j], (z, h0, h1) ) + integrate( Qs_(Ec, nu)[i,j], (z, h1, h2) ) + integrate( Qs_(Ec, nu)[i,j], (z, h2, h3) ) )

db = (Em*(1))/(12*(1-nu**2))

#uniform temperature change
S1 = 1*(integrate( ((alpha_z_top*E_z_top)/(1-nu)), (z, h2, h3) ) + integrate(((E1*0)/(1-nu)), (z, h1, h2)) + integrate( ((alpha_z_bottom*E_z_bottom)/(1-nu)), (z, h0, h1) ))
#print(alpha)
#linear temperature change
T_z = 1#must be replaced with proper function
#S1 = -1*(integrate( ((alpha_z_top*E_z_top*T_z)/(1-nu)), (z, h2, h3) ) + integrate(((E1*alpha*T_z)/(1-nu)), (z, h1, h2)) + integrate( ((alpha_z_bottom*E_z_bottom*T_z)/(1-nu)), (z, h0, h1) ))

#Tests

#print('A:\b',A)
#print()
#print('A2\b', A2)
#print('B:\b', B)
#print()
#print('D:\b',D)
#print()
#print('D2\b', D2)
#print('S:\b',S)
#print()
#print('S2\b', S2)