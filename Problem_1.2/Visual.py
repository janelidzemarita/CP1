import numpy as np
import matplotlib.pyplot as plt
import Derivatives
# Assuming you have arrays or matrices: error_first_order_fd_double, error_second_order_fd_double
error_first_order_fd_double = np.abs(np.subtract(Derivatives.first_order_fd_double, Derivatives.analytical_derivative))
error_second_order_fd_double = np.abs(np.subtract(Derivatives.second_order_fd_double, Derivatives.analytical_second_derivative))
# Generate x values for plotting
x = np.arange(0, len(error_first_order_fd_double))

# Plotting the errors
plt.plot(x, error_first_order_fd_double, label='First Order FD Error')
plt.plot(x, error_second_order_fd_double, label='Second Order FD Error')

# Add labels and title
plt.xlabel('Index')
plt.ylabel('Error')
plt.title('Errors between Finite Difference and Analytical Derivatives')

# Show legend
plt.legend()

# Show the plot
plt.show()
