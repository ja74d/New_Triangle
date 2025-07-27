import sympy as sp
import numpy as np

k, e = sp.symbols('k e')

def gaussian_quadrature(n):
    x = sp.Symbol('x')
    # Get the nth Legendre polynomial
    Pn = sp.legendre(n, x)
    
    # Compute the roots of the Legendre polynomial (abscissas)
    abscissas = sp.solvers.solve(Pn, x)
    
    # Compute the weights
    weights = []
    for xi in abscissas:
        wi = 2 / ((1 - xi**2) * (sp.diff(Pn, x).subs(x, xi))**2)
        weights.append(wi)
    
    # Evaluate the symbolic expressions numerically
    abscissas = [sp.N(xi) for xi in abscissas]
    weights = [sp.N(wi) for wi in weights]
    
    return abscissas, weights

def RIP_Gauss(fn, n=2):
    if fn == 0:
        integ = 0
    else:
        #abscissas, weights = [1/2, 0, 1/2], [1/3, 1/3, 1/3]#gaussian_quadrature(n)
        #integ = 0
        #for i in range(len(abscissas)):
        #   for j in range(len(abscissas)):
        #        f_val = fn.subs( {k:abscissas[i], e:abscissas[j]} )
        #        integ += weights[i]*weights[j]*f_val
        #integ = 1/3*(fn.subs({k:1/2, e:0})) + 1/3*(fn.subs({k:0, e:1/2})) + 1/3*fn.subs({k:1/2, e:1/2})
        integ = (-27/48)*(fn.subs({k:1/3, e:1/3})) + (25/48)*(fn.subs({k:0.2, e:0.6})) + (25/48)*(fn.subs({k:0.2, e:0.2})) + (25/48)*(fn.subs({k:0.6, e:0.2}))
        #integ = sp.integrate( sp.integrate(fn, (k, (0, 1-e))), (e, (0, 1)) )
    return integ

def apply_rip_gauss(matrix, n):
    result = np.zeros((2, 2))
    for i in range(2):
        for j in range(2):
            result[i, j] = RIP_Gauss(matrix[i, j], n)
    return result