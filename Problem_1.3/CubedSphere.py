import numpy as np
import matplotlib.pyplot as plt

def compute_derivatives(f, dx):
    # Compute derivatives using finite difference approximation
    dfdx = (f[2, 1, :] - f[0, 1, :]) / (2 * dx)
    dfdy = (f[1, 2, :] - f[1, 0, :]) / (2 * dx)
    dfdz = (f[1, 1, 1] - f[1, 1, 0]) / (dx)  # Assumes 2-layer grid in the z-direction
    return dfdx, dfdy, dfdz

def test_convergence():
    # Define a test function on a sphere
    def f(x, y, z):
        return np.sin(x) * np.cos(y) * np.exp(z)

    # Parameters
    num_samples = 5
    grid_spacings = np.logspace(-2, -6, num_samples)  # Varying grid spacings
    errors = np.zeros(num_samples)

    for i, dx in enumerate(grid_spacings):
        # Compute derivatives using finite differences
        x = np.linspace(-np.pi/2, np.pi/2, 3)
        y = np.linspace(-np.pi/2, np.pi/2, 3)
        z = np.linspace(-np.pi/2, np.pi/2, 2)
        X, Y, Z = np.meshgrid(x, y, z, indexing='ij')
        F = f(X, Y, Z)
        derivatives = compute_derivatives(F, dx)

        # Compute exact derivatives
        exact_derivatives = (np.cos(X) * np.cos(Y) * np.exp(Z),
                             -np.sin(X) * np.sin(Y) * np.exp(Z),
                             np.sin(X) * np.cos(Y) * np.exp(Z))

        # Compute error
        errors[i] = np.sqrt(np.mean((np.array(derivatives) - np.array(exact_derivatives))**2))

    return grid_spacings, errors

# Perform convergence test
grid_spacings, errors = test_convergence()

# Plot results
plt.loglog(grid_spacings, errors, '-o')
plt.xlabel('Grid Spacing (dx)')
plt.ylabel('Error')
plt.title('Convergence of Derivative Approximation')
plt.show()
