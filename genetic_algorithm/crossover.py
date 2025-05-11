import numpy as np

def arithmetic_crossover(parent1, parent2):
    alpha = np.random.rand()
    child1 = alpha * parent1 + (1 - alpha) * parent2
    child2 = alpha * parent2 + (1 - alpha) * parent1
    return child1, child2

def linear_crossover(parent1, parent2, x_min=-5, x_max=5):
    child1 = 0.5 * parent1 + 0.5 * parent2
    child2 = 1.5 * parent1 - 0.5 * parent2
    return np.clip(child1, x_min, x_max), np.clip(child2, x_min, x_max)

def blend_crossover_alpha(parent1, parent2, alpha=0.5, x_min=-5, x_max=5):
    gamma = np.random.uniform(-alpha, 1 + alpha, parent1.shape)
    child1 = gamma * parent1 + (1 - gamma) * parent2
    child2 = gamma * parent2 + (1 - gamma) * parent1
    return np.clip(child1, x_min, x_max), np.clip(child2, x_min, x_max)

def blend_crossover_alpha_beta(parent1, parent2, alpha=0.4, beta=0.6, x_min=-5, x_max=5):
    gamma = np.random.uniform(-alpha, 1 + beta, parent1.shape)
    child1 = gamma * parent1 + (1 - gamma) * parent2
    child2 = gamma * parent2 + (1 - gamma) * parent1
    return np.clip(child1, x_min, x_max), np.clip(child2, x_min, x_max)

def average_crossover(parent1, parent2, x_min=-5, x_max=5):
    child = (parent1 + parent2) / 2.0
    return np.clip(child, x_min, x_max), np.clip(child.copy(), x_min, x_max)