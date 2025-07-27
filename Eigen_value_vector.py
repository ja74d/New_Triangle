import numpy as np
from input import Lx, Ly, d, po
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata
from code_table import code, coordinations
from mesh import Nex, Ney
from app import Delta, K, Kg
from scipy.linalg import eig
#from READ_HDF5 import K, Kg, F

eigenvalues, eigenvectors = eig(K, Kg)

index = np.where(eigenvalues == min(eigenvalues))[0][0]
Buckling_load = eigenvalues[index]
Buckling_mode = eigenvectors[index]

#Displaying Eigenvalue and shape of plate at buckling mode in aa graph

D = Buckling_mode
#print(Buckling_mode)
print(Buckling_load)
D_z = []

for i in range(len(code)):
    for j in range(4):
        if code[i][5*j]!=0:
            D_z.append(D[code[i][5*j]-1])
        else:
            D_z.append(0)
x = []
y = []

for i in range(len(coordinations)):
    for j in range(4):
        x.append(coordinations[i][j][0])
        y.append(coordinations[i][j][1])

z = np.array(D_z)
x = np.array(x)
y = np.array(y)


# Define grid limits for consistent scaling
grid_min = 0

# Create a grid for x and y coordinates
grid_x, grid_y = np.mgrid[grid_min:Ly:33j, grid_min:Ly:33j]

# Interpolate displacement data onto the grid
grid_z = griddata((x, y), z, (grid_x, grid_y), method='cubic')

# Plot the surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot with uniform scaling for each axis
ax.set_box_aspect([1, 1, 1])  # Equal scaling for x, y, z

surf = ax.plot_surface(grid_x, grid_y, grid_z, cmap='rainbow')
#fig.colorbar(surf, shrink=0.5, aspect= 5)
cbar = fig.colorbar(surf, shrink=0.5, aspect=5)

# Define the min and max values for colorbar normalization
z_min, z_max = np.min(grid_z), np.max(grid_z)

# Normalize the color scale to the desired range
from matplotlib.colors import Normalize
norm = Normalize(vmin=z_min, vmax=z_max)

# Update the colorbar with specific ticks: Min, Max, and some intermediate values
cbar.set_ticks([z_max, (z_min + z_max)/7, 2*(z_min + z_max)/7, 3*(z_min + z_max)/7, 4*(z_min + z_max)/7,5*(z_min + z_max)/7, 6*(z_min + z_max)/7 ,z_min])  # Set ticks at min, middle, and max
cbar.set_label("Displacement (Z)")

# Set labels and title
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.title("Deflection of SSSS Plate under Uniformly Distributed Load")

# Set limits to keep axes uniform
#ax.set_xlim(grid_min, Lx)
#ax.set_ylim(grid_min, Ly)
#ax.set_zlim(-1, 1)

ax.view_init(elev=45, azim=45)

#plt.show()