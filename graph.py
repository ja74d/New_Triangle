import numpy as np
from input import Lx, Ly, d, po
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from code_table import code, coordinations
from mesh import Nex, Ney
from app import Delta

ax = plt.axes(projection='3d')

Delta = Delta / (po * Lx**4 / d)
D = -Delta

#D = [ 1.42871531e+02, -1.42871531e+02, -1.42871531e+02,  1.42871531e+02, 3.98707348e+02,  3.09391738e-14, -9.85579493e-15, -1.27970898e-13]

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

#
#x = np.arange(-5, 5, 0.1)
#y = np.arange(-5, 5, 0.1)
#x, y = np.meshgrid(x, y)
#z = np.sin(x) * np.sin(y)
ax.plot_surface(x, y, z, cmap="plasma")
ax.view_init(azim=45, elev=45)
plt.show()
