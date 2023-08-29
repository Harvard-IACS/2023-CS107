import numpy as np
from scipy.sparse.linalg import gmres

def func(x):
    # Define f as an array
    return f

def jac_vec_prod(xseed):
    fad = func(xseed)
    # Get Jacobian-vector product
    return fad.jacobian # something like this

def mc(xv):
    x = xv[0]
    y = xv[1]
    f = np.sin(x+y) + 2.0 * (x-y)**2.0 - 1.5 * x + 2.5 * y + 1
    return f

def exp_2d(xv, x0=1.0, y0=2.0):
    x = xv[0]
    y = xv[1]
    f = -(np.exp(-(x-x0)**2.0 - (y-y0)**2.0))**0.5
    return f

x = np.zeros(2.0)
dx0 = np.array([0.1, 0.2])
while True:

    fn = -func(x)
    dx = gmres(jac_vec_prod, fn, x0=dx0)

    t = np.linalg.norm(dx)
    if t < tol:
       roots = x + dx
       break

    x += dx

print("roots are: {}".format(roots))
