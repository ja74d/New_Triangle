import time
import sys
import h5py
import os
import numpy as np
from interpolation_functions import *
from tqdm import tqdm
from sympy import Matrix
from input import *
from mesh import coordinations, odin
from code_table import code
from gaussian_quad import RIP_Gauss, apply_rip_gauss
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import spsolve
from scipy.linalg import eig
#from Single_FGM import A, D, S, db, S1
#from isotropic_A_B_D_S import A, B, D, S, db, S1
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import eigsh
#A, B, D, S Matrices
pwd = os.getcwd()
filepath = os.path.join(pwd, 'Sandwich_FSDT')
sys.path.append(filepath)
from Sandwich_FSDT.app import A, B, D, S, S1, db, Ec, Em

#elastic foundation
Kw = 100
Kp = 0

# Start the timer
start = time.perf_counter()

#S1 = ((np.pi**2)*db)/(Lx**2)
S1 = 1

Sigma = np.array([
    [S1, 0],
    [0, 0]
])

def DNx(i):
    return (J_inv[0,0])*( dNdk[i] ) + (J_inv[0,1])*( dNde[i] )

def DNy(i):
    return (J_inv[1,0])*( dNdk[i] ) + (J_inv[1,1])*( dNde[i] )

def Bm_function(i):
    return np.array([
        [0, 0, 0, DNx(i), 0],
        [0, 0, 0, 0, DNy(i)],
        [0, 0, 0, DNy(i), DNx(i)]])

def Bb_function(i):
    return np.array([
        [0, DNx(i), 0, 0, 0],
        [0, 0, DNy(i), 0, 0],
        [0,  DNy(i), DNx(i), 0, 0]])

def Bs_function(i):
    return np.array([
        [DNx(i), N[i], 0, 0, 0],
        [DNy(i), 0, N[i], 0, 0],])

def BGb_function(i):
    return  np.array([
            [DNx(i), 0, 0, 0, 0],
            [DNy(i), 0, 0, 0, 0]])

Jacob = []
Ke = []
Kge = []
Fe = []
count = 0

for elemc in tqdm(range(len(coordinations)),desc="Calculating elements"):
    # Start the timer
    #start_time = time.perf_counter()
    element_coordinates = coordinations[elemc]
    #count += 1
    n_elem = len(code)

    #x1, x2, x3 = coordinations[elemc][0][0], coordinations[elemc][1][0], coordinations[elemc][2][0]
    #y1, y2, y3 = coordinations[elemc][0][1], coordinations[elemc][1][1], coordinations[elemc][2][1]


    #Saving Private Jacobean
    #symbolic in jacobean
    J = Matrix([
        [0, 0],
        [0, 0]
    ])

    j00 = 0
    j01 = 0
    j10 = 0
    j11 = 0
    for i in range(6):
        j00 += dNdk[i] * float(element_coordinates[i][0])
        j01 += dNdk[i] * float(element_coordinates[i][1])
        j10 += dNde[i] * float(element_coordinates[i][0])
        j11 += dNde[i] * float(element_coordinates[i][1])
    J[0, 0] = j00
    J[0, 1] = j01
    J[1, 0] = j10
    J[1, 1] = j11

    #Det J
    det_J = (J[0,0])*(J[1,1]) - (J[0,1])*(J[1,0])

    if Jacob_cache == 1:
        pass
    #for ij in Jacob:
    #    J_check = apply_rip_gauss(J, 3)
    #    ij_check = apply_rip_gauss(ij, 3)
        
    #    if abs((np.linalg.norm(ij_check) - np.linalg.norm(J_check))) < tol:
    #        K_e = Ke[Jacob.index(ij)]
    #        K_eg = Kge[Jacob.index(ij)]
    #        Ke.append(K_e)
    #        Kge.append(K_eg)
    #        break
    else:
        Jacob.append(J)

        #inverse of Jacobean
        J_inv = (1/det_J)*np.array([
            [J[1,1], -J[0,1]],
            [-J[1,0], J[0,0]]
        ])

        #B
        #Bm matrix(membrane)
        Bm = [Bm_function(0), Bm_function(1), Bm_function(2), Bm_function(3), Bm_function(4), Bm_function(5)]
        #Bm = [(1/det_J)*Bm1, (1/det_J)*Bm2, (1/det_J)*Bm3]

        #Bb matrix(Bending)
        Bb = [Bb_function(0), Bb_function(1), Bb_function(2), Bb_function(3), Bb_function(4), Bb_function(5)]
        #Bb = [(1/det_J)*Bb1, (1/det_J)*Bb2, (1/det_J)*Bb3]

        #Bs matrix(Shearing)
        Bs = [Bs_function(0), Bs_function(1), Bs_function(2), Bs_function(3), Bs_function(4), Bs_function(5)]
        #Bs = [J_inv@Bs1, J_inv@Bs2, J_inv@Bs3]
        
        #Bg matrix(Geometric)
        Bgb = [BGb_function(0), BGb_function(1), BGb_function(2), BGb_function(3), BGb_function(4), BGb_function(5)]

        #Gaussian Integration Method *
        #Ke

        #K_em
        def compute_km(i, j):
            return Bm[i].T @ A @ Bm[j]
        
        Gm = np.block([[compute_km(i, j) for j in range(6)] for i in range(6)])

        K_em = np.zeros((30, 30))
        for o in range(0, 30):
            for p in range(0, 30):
                K_em[o, p] = RIP_Gauss(Gm[o, p]*det_J)

        #K_eb
        def compute_kb(i, j):
            return Bb[i].T @ D @ Bb[j]
        Gb = np.block([[compute_kb(i, j) for j in range(6)] for i in range(6)])

        K_eb = np.zeros((30, 30))
        for o in range(0, 30):
            for p in range(0, 30):
               K_eb[o, p] = RIP_Gauss(Gb[o, p]*det_J)
        
        #K_es
        def calculate_ks(i, j):
            return Bs[i].T @ S @ Bs[j]
        Gs = np.block([[calculate_ks(i, j) for j in range(6)] for i in range(6)])

        K_es = np.zeros((30, 30))
        for o in range(0, 30):
            for p in range(0, 30):
                K_es[o, p] = RIP_Gauss(Gs[o, p]*det_J)
    
        #winkler
        winkler = np.zeros((30, 30))
        for o in range(0, 30):
            for p in range(0, 30):
                winkler[o, p] = ((Kw*(db))/(Lx**4))*RIP_Gauss(wanker[o, p]*det_J)
                #winkler[o, p] = RIP_Gauss(wanker[o, p]*det_J, n=3)
        
        #pasternak
        Nwf_dk = np.array([DNx(0), 0, 0, 0, 0, DNx(1), 0, 0, 0, 0, DNx(2), 0, 0, 0, 0, DNx(3), 0, 0 ,0 , 0, DNx(4), 0, 0, 0 ,0 , DNx(5), 0, 0, 0, 0])
        Nwf_de = np.array([DNy(0), 0, 0, 0, 0, DNy(1), 0, 0, 0, 0, DNy(2), 0, 0, 0, 0, DNy(3), 0, 0 ,0 , 0, DNy(4), 0, 0, 0 ,0 , DNy(5), 0, 0, 0, 0])
        
        peter = sp.zeros(30, 30)
        for i in range(0, 30):
            for j in range(0, 30):
                peter[i, j]=(Nwf_dk[i]*Nwf_dk[j]) + (Nwf_de[i]*Nwf_de[j])

        paster = np.zeros((30, 30))
        for o in range(0, 30):
            for p in range(0, 30):
                paster[o, p] = ((Kp*(db))/(Lx**2))*RIP_Gauss((peter[o, p])*det_J)

        K_e = K_es + K_eb + K_em + winkler + paster
        Ke.append(K_e)

        #K_eg
        def calculate_kg(i, j):
            return ( Bgb[i].T @ Sigma @ Bgb[j] )
        Pg = np.block([[calculate_kg(i, j) for j in range(6)] for i in range(6)])

        k_eg = np.zeros((30, 30))
        for o in range(0, 30):
            for p in range(0, 30):
                k_eg[o, p] = RIP_Gauss(Pg[o, p]*det_J)
        Kge.append(k_eg)

        #Fe
    F_e = np.zeros((30, 1))
    for i in range(0, 30):
        F_e[i, 0] = RIP_Gauss(p0*(Nw[i])*det_J)
    Fe.append(F_e)

#Assembling
num_dofs = np.max(code)
K = np.zeros((num_dofs, num_dofs))
Kg = np.zeros((num_dofs, num_dofs))
F = np.zeros(num_dofs)

num_elements = code.shape[0]

for elem in range(num_elements):
    for i in range(30):
        if code[elem, i] != 0:
            for j in range(30):
                if code[elem, j] != 0:
                    K[code[elem, i] - 1, code[elem, j] - 1] += Ke[elem][i, j]
                    Kg[code[elem, i] - 1, code[elem, j] - 1] += Kge[elem][i, j]
            F[code[elem, i] - 1] += Fe[elem][i, 0]

db = (E*h**3)/(12*(1-(nu**2)))

K_sparse = csc_matrix(K)
Delta = spsolve(K_sparse, F)

#Delta = np.linalg.pinv(K) @ F

#Delta = np.linalg.inv(K) @ F

Wmid = max(Delta)
wmidND = Wmid / (p0 * (Lx**4) / db)

# Output the result
print(f"number of elements: {num_elements}")
print(f"displacement at midpoint: {Wmid}")
print(f"Non-dimensional displacement at midpoint: {100*wmidND}")

# End the timer
end = time.perf_counter()

# Calculate elapsed time
elapsed_time = end - start
print(f"Time taken: {elapsed_time} seconds")

#with h5py.File(f'{file_name}.h5', 'w') as hdf:

#    # Create a group for matrices
#    matrices_group = hdf.create_group('Matrices')
#    matrices_group.create_dataset('Stiffness_Matrix', data=K)
#    matrices_group.create_dataset('Force_Matrix', data=F)
#    matrices_group.create_dataset('Geometrical_Matrix', data=Kg)

    # Create a group for nodal data
#    nodal_group = hdf.create_group('Nodal_Data')
#   nodal_group.create_dataset('Nodal_Displacement', data=Delta)

#    # You can also add attributes for metadata
#    hdf.attrs['Description'] = 'Finite Element Analysis Results'
#    hdf.attrs['Version'] = '1.0'
#print(f"Data has been saved in '{file_name}.h5'")
