from matplotlib import pyplot as plt
import numpy as np
from genetic_algorithm.evaluation import schwefel

plt.style.use('ggplot')

def plot_results(history, filename="results.jpg"):
    plt.figure(figsize=(10, 7))
    plt.plot(history, label="Best Score", color="#007acc", linewidth=2.5)
    plt.xlabel("Generations", fontsize=14)
    plt.ylabel("Best Score", fontsize=14)
    plt.title("Genetic Algorithm Optimization", fontsize=16)
    plt.legend(fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.savefig(filename, format="jpg", dpi=300)
    plt.close()


def plot_3d_result(best_solution, filename="best_solution_3d.jpg"):
    x, y = best_solution
    z = schwefel(best_solution)
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    X = np.linspace(-500, 500, 100)
    Y = np.linspace(-500, 500, 100)
    X, Y = np.meshgrid(X, Y)
    Z = schwefel([X, Y])
    ax.plot_surface(X, Y, Z, cmap='plasma', alpha=0.8)
    ax.scatter(x, y, z, color='red', s=150, label='Best Solution')
    ax.set_title("Best Solution on Schwefel Function", fontsize=16)
    ax.set_xlabel("X", fontsize=14)
    ax.set_ylabel("Y", fontsize=14)
    ax.set_zlabel("Z", fontsize=14)
    ax.legend(fontsize=12)
    plt.savefig(filename, format="jpg", dpi=300)
    plt.close()

def plot_heatmap(best_solution, filename="heatmap.jpg"):
    x, y = best_solution
    X = np.linspace(-500, 500, 200)
    Y = np.linspace(-500, 500, 200)
    X, Y = np.meshgrid(X, Y)
    Z = schwefel([X, Y])
    plt.figure(figsize=(10, 7))
    contour = plt.contourf(X, Y, Z, levels=60, cmap='inferno')
    plt.colorbar(contour, label="Schwefel Value")
    plt.scatter(x, y, color='red', s=150, label='Best Solution')
    plt.title("Heatmap of Schwefel Function with Best Solution", fontsize=16)
    plt.xlabel("X", fontsize=14)
    plt.ylabel("Y", fontsize=14)
    plt.legend(fontsize=12)
    plt.savefig(filename, format="jpg", dpi=300)
    plt.close()