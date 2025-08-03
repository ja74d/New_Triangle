from datetime import datetime

date_time = datetime.now()

#B.C.
BCleft, BCright, BCtop, BCbottom = 'C', 'Sym', 'C', 'Sym'
BChole = 'F'
Jacob_cache = 0

#File name
file_name = '1010_plate_quarter_analysis'
file_name = f'{file_name}_Saved at {date_time}'

#volume fraction index "n"
n = 0

#Mechanincal Properties
#Ceramic-Aluminum
Ec = 380e+09
alpha_c = 7.4e-6
Em = 70e+09
alpha_m = 23e-6
nu = 0.3

E = 1
h = 1
alpha = 1

K_dictionary = {
    0: 5/6,
    1: 0.831,
    2: 0.7949,
    4: 0.76,
    8: 0.7619,
    10: 0.7694
}
ka = 5/6
#ka_FGM = K_dictionary[n]
#ka = ka_FGM
#Distributed Load
p0 = 1
po = 1
d = E*h**3/(12*(1-nu**2))

#Geometry
Lx = Ly = 10

#elastic foundation


#tolerance
tol = 1e-4