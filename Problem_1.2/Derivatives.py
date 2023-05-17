import numpy as np
import matplotlib.pyplot as plt

def forward_difference(x, h):
    return (f(x + h) - f(x)) / h


def backward_difference(x, h):
    return (f(x) - f(x - h)) / h


def central_difference(x, h):
    return (f(x + h) - f(x - h)) / (2 * h)


def second_order_difference(x, h):
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h ** 2)


def f(x):
    return np.sin(x) + np.random.normal(0, 0.001)


# Parameters
precision = np.float32
spacing = 0.1

# Compute derivatives using different formulas
x = np.arange(0, 10, spacing, dtype=precision)

first_order_fd = forward_difference(x, spacing)
second_order_fd = second_order_difference(x, spacing)

# Compute derivatives using double precision
x_double = np.arange(0, 10, spacing, dtype=np.float64)

first_order_fd_double = central_difference(x_double, spacing)
second_order_fd_double = second_order_difference(x_double, spacing)

# Compare computed derivatives with analytical solution
analytical_derivative = np.cos(x)
analytical_second_derivative = -np.sin(x)

error_first_order_fd = np.abs(first_order_fd - analytical_derivative)
error_second_order_fd = np.abs(second_order_fd - analytical_derivative)

error_first_order_fd_double = np.abs(np.subtract(first_order_fd_double, analytical_derivative))
error_second_order_fd_double = np.abs(np.subtract(second_order_fd_double, analytical_second_derivative))

# print("Errors for first-order derivative (single precision):", error_first_order_fd)
# print("Errors for second-order derivative (single precision):", error_second_order_fd)
#
# print("Errors for first-order derivative (double precision):", error_first_order_fd_double)
# print("Errors for second-order derivative (double precision):", error_second_order_fd_double)
# Generate x values for plotting
x2 = np.arange(0, len(error_first_order_fd_double))

# Plotting the errors
plt.plot(x2, error_first_order_fd_double, label='First Order FD Error')
plt.plot(x2, error_second_order_fd_double, label='Second Order FD Error')

# Add labels and title
plt.xlabel('Index')
plt.ylabel('Error')
plt.title('Errors between Finite Difference and Analytical Derivatives')

# Show legend
plt.legend()

# Show the plot
plt.show()

data = error_second_order_fd_double
window_size = 5  # Adjust the window size based on your requirements

# Applying moving average filter
smooth_data = np.convolve(data, np.ones(window_size)/window_size, mode='valid')

# Plotting original data and smoothed data
plt.plot(data, label='Original Data')
plt.plot(smooth_data, label='Smoothed Data')

# Add labels and title
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Smoothing Filter')

# Show legend
plt.legend()

# Show the plot
plt.show()