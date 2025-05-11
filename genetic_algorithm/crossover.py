import numpy as np

def arithmetic_crossover(parent1, parent2):
    alpha = np.random.rand()
    child1 = alpha * parent1 + (1 - alpha) * parent2
    child2 = alpha * parent2 + (1 - alpha) * parent1
    return child1, child2

def linear_crossover(parent1, parent2):
    child1 = 0.5 * parent1 + 0.5 * parent2
    child2 = 1.5 * parent1 - 0.5 * parent2
    return child1, child2

def blend_crossover_alpha(parent1, parent2, alpha=0.5):
    gamma = np.random.uniform(-alpha, 1 + alpha, parent1.shape)
    child1 = gamma * parent1 + (1 - gamma) * parent2
    child2 = gamma * parent2 + (1 - gamma) * parent1
    return child1, child2

def blend_crossover_alpha_beta(parent1, parent2, alpha=0.4, beta=0.6):
    gamma = np.random.uniform(-alpha, 1 + beta, parent1.shape)
    child1 = gamma * parent1 + (1 - gamma) * parent2
    child2 = gamma * parent2 + (1 - gamma) * parent1
    return child1, child2

def average_crossover(parent1, parent2):
    child = (parent1 + parent2) / 2.0
    return child, child.copy()


def one_point_crossover(parent1, parent2):
    point = np.random.randint(1, len(parent1))
    child1 = np.concatenate((parent1[:point], parent2[point:]))
    child2 = np.concatenate((parent2[:point], parent1[point:]))
    return child1, child2
