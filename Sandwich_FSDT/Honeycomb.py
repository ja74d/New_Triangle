import numpy as np
import math

#Section Properties
b = 15
l2 = 10
l = 10
t = 1
s = 1
teta = 30
teta = math.radians(teta)

Lx = 2*l*(math.cos(teta))
Ly = l2 + 2*l*(math.sin(teta))

#material properties

Es = 380e+9 #MPa
alphas = 0
nus = 0.3
Gs = Es/(2*(1+nus))

E, G, nu = Es, Gs, nus
#in-plane mechanical properties

###gibson
#in-plan
gE1 = E*((t/l)**3)*( (math.cos(teta))/((l2/l+math.sin(teta))*(math.sin(teta)**2)) )
gE2 = ((t/l)**3)*E*( ( l2/l + math.sin(teta) )/(math.cos(teta)**3) )
gG12 = E * ((t/l)**3) * ( ( l2/l + math.sin(teta) )/( ((l2/l)**2)*( 1 + 2*(l2/l) )*math.cos(teta) ) )
#tiny basterdes
gnu12 = ( (math.cos(teta)**2)/( (l2/l+math.sin(teta))*(math.sin(teta)) ) )
gnu21 = ( ((l2/l + math.sin(teta))*(math.sin(teta)))/(math.cos(teta)**2) )
galpha = alphas

#out of plan
gG13 = (t/l)*G*( (math.cos(teta))/(l2/l + math.sin(teta)) )
gG23 = (t/(2*l))*G*( ( l2/l + 2*(math.sin(teta))**2 )/((l2/l + math.sin(teta))*math.cos(teta)) )

Gibson = { 
    'E1': gE1,
    'E2': gE2,
    'G12': gG12,
    'G13': gG13,
    'G23': gG23,
    'nu12': gnu12,
    'nu21': gnu21,
    'alpha': galpha
         }

#Q_gibson = np.zeros((3,3))
t = 1
l = 10
h = 10
b = 15

#sorhan
k1 = 1/( 1 + (((t/l)**2)*(2.4 + 1.5*nus + (1/math.tan(teta))**2)) )
k2 = 1/( 1 + ((t/l)**2) * ( 2.4 + 1.5*nus + (math.tan(teta))**2 + ((2*h)/(l*((math.cos(teta))**2))) ) )
c12 = ( 1 + (t/l)**2 * ( 1.4 + 1.5*nus ) ) / ( 1 + (t/l)**2 * ( 2.4 + 1.5*nus + (1/math.tan(teta))**2 ) )
c21 = ( 1 + (t/l)**2 * ( 1.4 + 1.5*nus ) ) / ( 1 + (t/l)**2 * ( 2.4 + 1.5*nus + (math.tan(teta))**2 + ((2*h)/(l*((math.cos(teta))**2))) ) )
k12 = (1 + 2*(h/l)) / ( 1 + (2*h)/l + (t/l)**2 * ( ( (l/h)*(2.4 + 1.5*nus)*(2 + h/l + math.sin(teta)) ) + ( ( (h/l + math.sin(teta))/((h/l)**2) )*( (h/l + math.sin(teta))*(math.tan(teta))**2 + math.sin(teta) ) ) ) )
G23u = 1/2 * Gs * (t/l) * ( (h/l + 2*(math.sin(teta))**2)/((h/l + math.sin(teta))*math.cos(teta)) )
G23L = Gs * (t/l) * (( h/l + math.sin(teta) )/( ((2*h)/l + 1)*math.cos(teta) ))

sE1 = k1*Es*(t/l)**3 * ((math.cos(teta))/( ( h/l + math.sin(teta) )*(math.sin(teta))**2 ))
sE2 = k2*Es*(t/l)**3 * ((h/l + math.sin(teta))/(math.cos(teta)**3))
snu12 = c12 * ((math.cos(teta)**2)/((h/l + math.sin(teta))*(math.sin(teta))))
snu21 = c21 * ((h/l + math.sin(teta))*(math.sin(teta))/(math.cos(teta)**2))
sG12 = k12 * Es * (t/l)**3 * ( (h/l +math.sin(teta))/((h/l)**2 * (1+(2*h)/l)*math.cos(teta)) )
sG13 = (t/l)*Gs*(math.cos(teta)/(h/l + math.sin(teta)))
sG23 = G23L + (0.787/(b/l))*(G23u-G23L)

sorhan = {
    'E1': sE1,
    'E2': sE2,
    'G12': sG12,
    'G13': sG13,
    'G23': sG23,
    'nu12': snu12,
    'nu21': snu21,
    'alpha': 0
}


#print('Gibson: ',Gibson)
#print('sorhan:' ,sorhan)


Ec = 244.27e+09
alphac = 12.766e-6
nuc = 0.3
Gc = Ec/(2*(1+nuc))

Ceramic_only = {
    'E1': Ec,
    'E2': Ec,
    'G12': Gc,
    'G13': Gc,
    'G23': Gc,
    'nu12': nuc,
    'nu21': nuc,
    'alpha': alphac
}