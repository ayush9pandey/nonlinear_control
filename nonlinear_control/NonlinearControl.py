# Import required libraries and dependencies
from sympy import *
import numpy as np
from sympy.parsing.sympy_parser import parse_expr
import sympy
from sympy.abc import *
init_printing()
from sympy.diffgeom import *

class NonlinearControl(object):

    def __init__(self):
        self.x = None
        self.f = None
        self.g = None
        self.P = None
        self.coord = None
        return
    
    def getFeedbackLinearizingController(self):
        '''
        Returns u = B(x)^-1 (-A(x) + v)
        '''

        return
    def getControllabilityMatrix(self, f, g):
        '''
        Returns Lie bracket [f, g] = Lfg - Lgf
        '''
        return
    def getRelativeDegree(self, h):
        ''' 
        Returns the relative degree (if it exists) for the given system
        '''
        Lf_prev = self.f
        count = 0
        for _ in range(len(self.x)):
            count += 1
            update = self.getLieDerivative(Lf_prev, h, 1)
            if update == 0:
                Lf_prev = update
            else:
                r = count
            
        return r
    
    def getLieDerivative(self, f, g, order = 1):
        '''
        Returns the Lie derivative L^nfg, where n = order
        '''
        coord = self.coord
        e = coord.base_vectors()
        # Create the field now
        vec_field = 0
        for i in range(len(e)):
            vec = e[i]
            vec_field += f[i] * vec
        lie_derv = g 
        for _ in range(order):
            lie_derv = LieDerivative(vec_field, lie_derv)
        return lie_derv



def ode2sympy(odesize, ninputs, nparams = 0):
    '''
    Returns Sympy object for the given ODE function
    '''
    obj = NonlinearControl()
    M = Manifold('M',odesize)
    Pt = Patch('Pt',M)
    f = []
    g = []
    P = []
    str_g = []
    coord_list = []
    for i in range(odesize):
        str_var = 'x' + str(i)
        coord_list.append(str_var)
        str_f = 'f' + str(i)
        vars()[str_f] = symbols('f%d'%i)
        f.append(vars()[str_f])
    for j in range(ninputs):
        gi = [] 
        for i in range(odesize):
            str_g = 'g' + str(j+1) + str(i)
            vars()[str_g] = symbols('g' + str(j+1) + '%d'%i)
            gi.append(vars()[str_g])
        g.append(gi)
 
    for k in range(nparams):
        str_P = 'P' + str(k)
        vars()[str_P] = symbols('P' + '%d'%k)
        P.append(vars()[str_P])
    coord = CoordSystem('coord',Pt, coord_list)
    obj.x = coord.coord_functions()
    obj.f = f
    obj.g = g
    obj.P = P
    obj.coord = coord
    return obj

