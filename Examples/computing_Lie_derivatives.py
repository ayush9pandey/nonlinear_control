from nonlinear_control import * 

# Get xdot = f + g u, with parameters if needed. 
system = ode2sympy(odesize = 2, ninputs = 1)
x = system.x
f = system.f
g = system.g


# System dynamics x_dot = f(x) + g(x) u
f[0] = x[1] - 0.01 * x[0]
f[1] = -sin(x[0]) + 2

g[0][0] = 0
g[0][1] = 1
# Define output 
h = x[0]**2 + x[1]

Lfh = system.getLieDerivative(f,h,1)
print(Lfh)
L3fh = system.getLieDerivative(f,h,3)
print(L3fh)
Lg1h = system.getLieDerivative(g[0],h,1)
print(Lg1h)
