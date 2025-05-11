import numpy as np
import time
from config import *
from genetic_algorithm.evaluation import schwefel
from genetic_algorithm.selection import *
from genetic_algorithm.visualization import plot_3d_result, plot_heatmap, plot_results

def genetic_algorithm(
    mutation_func, crossover_func, selection_func,
    mutation_rate, elitism_rate=1,
    pop_size=POP_SIZE, gens=GENS,
    x_min=X_MIN, x_max=X_MAX, dim=DIM
):
    start_time = time.time()

    pop = np.random.uniform(x_min, x_max, (pop_size, dim))
    history = []

    for iteration in range(gens):
        scores = np.array([schwefel(ind) for ind in pop])
        best_score = np.min(scores)
        history.append(best_score)

        best_individual_idx = np.argmin(scores)
        best_individual = pop[best_individual_idx]

        new_pop = [best_individual]

        for _ in range(pop_size // 2 - elitism_rate):
            p1, p2 = selection_func(pop, scores), selection_func(pop, scores)
            c1, c2 = crossover_func(p1, p2)
            new_pop.extend([
                mutation_func(c1.copy(), mutation_rate),
                mutation_func(c2.copy(), mutation_rate)
            ])

        pop = np.array(new_pop)

    best_solution = pop[np.argmin([schwefel(ind) for ind in pop])]
    end_time = time.time()
    print(f"Czas wykonania algorytmu: {end_time - start_time:.2f} sekundy")

    plot_results(history)
    plot_3d_result(best_solution)
    plot_heatmap(best_solution)

    return best_solution
