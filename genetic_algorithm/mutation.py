import numpy as np
import sys
sys.path.append('../')
from config import X_MIN, X_MAX
def uniform_mutation(individual, rate):
    for i in range(len(individual)):
        if np.random.rand() < rate:
            individual[i] = np.random.uniform(X_MIN, X_MAX)
    return individual

def gaussian_mutation(individual, rate, sigma=1.0):
    for i in range(len(individual)):
        if np.random.rand() < rate:
            individual[i] += np.random.normal(0, sigma)
            individual[i] = np.clip(individual[i], X_MIN, X_MAX)
    return individual
