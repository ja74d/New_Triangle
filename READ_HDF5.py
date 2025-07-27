import h5py
import numpy as np
from input import file_name, tol, d, Lx, p0
from scipy.linalg import eig
from scipy.sparse.linalg import eigs, eigsh, LinearOperator  # Use eigsh for symmetric matrices
from scipy.sparse import csr_matrix
import scipy

with h5py.File('1010_plate_quarter_analysis_Saved at 2024-11-30 10:26:59.216927.h5', 'r') as hdf:
    # Access datasets
    K = hdf['Matrices/Stiffness_Matrix'][:]
    Kg = hdf['Matrices/Geometrical_Matrix'][:]
    F = hdf['Matrices/Force_Matrix'][:]
    Delta = hdf['Nodal_Data/Nodal_Displacement'][:]

#print(max(np.linalg.inv(K)@F) / (p0 * (Lx**4) / d))
