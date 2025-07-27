using HDF5
using SparseArrays
using LinearAlgebra

file = h5open("testfile_Saved at 2024-11-16 14:56:47.118512.h5", "r")

K = read(file["Matrices/Stiffness_Matrix"])   # Reads the matrix stored as 'K'
Kg = read(file["Matrices/Geometrical_Matrix"]) # Reads the matrix stored as 'Kg'

close(file)

eigvals = eigen(K, Kg).values

finite_eigenvalues = filter(isfinite, eigvals)

buckling_load = minimum(finite_eigenvalues)

println("Smallest non-infinite eigenvalue (buckling load): ", buckling_load)

