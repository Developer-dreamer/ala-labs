import matplotlib.pyplot as plt

def showResults2D(transformed_vector, origin_vector):
    # Plot the standard coordinate lines
    plt.axhline(0, color='green', linewidth=0.5)
    plt.axvline(0, color='green', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)

    # Plot the new space defined by the vectors
    plt.quiver(*[1, 0],  color=['r'], scale=10)
    plt.quiver(*[0, 1],  color=['b'], scale=10)
    for i in range(len(transformed_vector)):
        plt.scatter(transformed_vector[i][0], transformed_vector[i][1], color='red')
        plt.scatter(origin_vector[i][0], origin_vector[i][1], color='blue')

    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

