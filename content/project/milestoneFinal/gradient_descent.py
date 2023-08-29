import numpy as np

def rosen(xv, a=1.0, b=100.0):
    x = xv[0]
    y = xv[1]
    f = (a - x)**2.0 + b * (y - x**2.0)**2.0
    return f

def grad_rosen(xv, a=1.0, b=100.0):
    x = xv[0]
    y = xv[1]
    df_dx = -2.0 * (a - x) - 4.0 * b * x * (y - x**2.0)
    df_dy = 2.0 * b * (y - x**2.0)
    return np.array([df_dx, df_dy])

def mc(xv):
    x = xv[0]
    y = xv[1]
    f = np.sin(x+y) + 2.0 * (x-y)**2.0 - 1.5 * x + 2.5 * y + 1
    return f

def mc_grad(xv):
    x = xv[0]
    y = xv[1]
    df_dx = np.cos(x+y) + 2.0 * (x-y) - 1.5
    df_dy = np.cos(x+y) - 2.0 * (x-y) + 2.5
    return np.array([df_dx, df_dy])

def gd_mc(step_size=0.1, x=np.array([0, 0]), tol=1.0e-06, max_it=1000):
    x_old = x
    it = 0
    while True:
        #x = x_old - step_size * grad_rosen(x)
        x = x_old - step_size * mc_grad(x)
        dx = np.linalg.norm(x-x_old)
        print(it, dx, x)
        if dx < tol:
           return x
        if it > max_it:
           print("Failed to find minimum.")
           return x
        x_old = x
        it += 1

def exp_2d(xv, x0=0.0, y0=0.0):
    x = xv[0]
    y = xv[1]
    f = np.exp(-(x-x0)**2.0 - (y-y0)**2.0)
    return f

def exp_grad(xv, x0=0.0, y0=0.0):
    x = xv[0]
    y = xv[1]
    df_dx = 2.0 * (x - x0) * exp_2d(xv, x0, y0)
    df_dy = 2.0 * (y - y0) * exp_2d(xv, x0, y0)
    return np.array([df_dx, df_dy])

def gd_exp(step_size=0.1, x=np.array([1, 2]), tol=1.0e-06, max_it=1000):
    x_old = x
    it = 0
    while True:
        x = x_old - step_size * exp_grad(x, 2.0, 1.0)
        dx = np.linalg.norm(x-x_old)
        print(it, dx, x)
        if dx < tol:
           return x
        if it > max_it:
           print("Failed to find minimum.")
           return x
        x_old = x
        it += 1

if __name__=="__main__":
   xmin = gd_exp()
   print(xmin) 
