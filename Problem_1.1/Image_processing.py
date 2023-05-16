import numpy as np
import matplotlib.pyplot as plt

# Function to calculate the derivative using finite differences
def finite_differences_derivative(f, x, h):
    return (f(x + h) - f(x)) / h

# Example function
def example_function(x):
    return np.sin(x)

# Define the interval and step size
x = np.linspace(0, 2*np.pi, 100)
h = x[1] - x[0]

# Calculate the derivative using finite differences
derivative = finite_differences_derivative(example_function, x, h)

# Plot the original function and its derivative
plt.plot(x, example_function(x), label='Original Function')
plt.plot(x, derivative, label='Derivative')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Function and its Derivative')
plt.grid(True)
plt.show()
