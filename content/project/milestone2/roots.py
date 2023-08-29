from autodiff import autodiff as ad
from autodiff import adnp as anp

# User-defined function
# Will vary depending on their implementation
def f(a):
    x = ad.grad(a, 1.0)
    #return anp.exp(anp.sin(x)) - anp.cos(anp.sqrt(x)) * anp.sin(anp.sqrt(anp.cos(x)**2.0 + x**2.0))
    return anp.exp(anp.sin(x)) - anp.cos(x**0.5) * anp.sin((anp.cos(x)**2.0 + x**2.0)**0.5)

# Prepare for nonlinear solver

x = 2.0 # Initial guess
tol = 1.0e-06 # Solver tolerance
nmax = 25 # Maximum number of nonlinear iterations

nli = 0 # Nonlinear iteration counter
print("nli        x           dx    ")
while True:
    evalf = f(x) # Get function value
    dx = -evalf.val / evalf.der # Update step
    x = x + dx # Update solution
    print("{0}    {1:8.6f}     {2:8.6e}".format(nli+1, x, dx))

    # Check for convergence
    if abs(dx) <= tol:
       print("Found solution after {} iterations.".format(nli+1))
       print("There is a root at x = {0:25.16f}.".format(x))
       break

    # Check iteration count
    if nli > nmax:
       print("Exceeded allowable max iterations without finding a root.")
       break

    nli += 1 # Increment nonlinear iteration count
