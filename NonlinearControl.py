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
    def getRelativeDegree(self):
        ''' 
        Returns the relative degree (if it exists) for the given system
        '''
        for i in range(len(self.x)):
            self.getLieDerivative()
        return
    
    def getLieDerivative(self, f, g, order):
        '''
        Returns the Lie derivative L^nfg, where n = order
        '''
        coord = self.coord
        e_x1,e_x2,e_x3,e_x4,e_x5,e_x6,e_x7,e_x8 = coord.base_vectors()
        e = [e_x1,e_x2,e_x3,e_x4,e_x5,e_x6,e_x7,e_x8]
        return


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

