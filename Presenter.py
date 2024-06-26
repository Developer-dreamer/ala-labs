import matplotlib.pyplot as plt

def showResults2D(transformed_vector, origin_vector):
    # Plot the standard coordinate lines
    plt.axhline(0, color='green', linewidth=0.5)
    plt.axvline(0, color='green', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)

    # Plot the new space defined by the vectors
    plt.quiver(*[1, 0],  color=['blue'], scale=10)
    plt.quiver(*[0, 1],  color=['blue'], scale=10)

    plt.plot(*zip(*transformed_vector), 'go-')
    plt.plot(*zip(*origin_vector), 'ro-')


    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def showResults3D(transposed_vector, origin_vector):
    fig = plt.figure()

    # Create a 3D axes
    ax = fig.add_subplot(111, projection='3d')

    # Set the limits
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_zlim([-10, 10])

    plt.plot(*zip(*transposed_vector), 'go-')
    plt.plot(*zip(*origin_vector), 'ro-')

    # Set the labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()