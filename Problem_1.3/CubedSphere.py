import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_cubed_sphere_mesh():
    # Define the number of subdivisions
    subdivisions = 10

    # Generate the vertices of the cubed sphere
    vertices = []
    for x in range(-subdivisions, subdivisions + 1):
        for y in range(-subdivisions, subdivisions + 1):
            for z in range(-subdivisions, subdivisions + 1):
                vertices.append((x, y, z))
    vertices = np.array(vertices, dtype=np.float64)  # Store vertices as float

    # Normalize the vertices
    norm = np.linalg.norm(vertices, axis=1)
    vertices /= norm[:, None]

    # Create the figure and 3D axis
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the cubed sphere mesh
    ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], s=1)

    # Set axis limits and labels
    ax.set_xlim([-1.1, 1.1])
    ax.set_ylim([-1.1, 1.1])
    ax.set_zlim([-1.1, 1.1])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Show the plot
    plt.show()

# Generate and visualize the cubed sphere mesh
generate_cubed_sphere_mesh()
