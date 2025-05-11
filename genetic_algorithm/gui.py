import tkinter as tk
from tkinter import ttk
from genetic_algorithm.algorithm import genetic_algorithm
from genetic_algorithm.evaluation import schwefel
from config import POP_SIZE, GENS, MUT_RATE, CROSS_RATE, DIM, X_MIN, X_MAX, ITERATION

# Importowanie funkcji mutacji, krzyżowania i selekcji
from genetic_algorithm.mutation import gaussian_mutation
from genetic_algorithm.crossover import one_point_crossover
from genetic_algorithm.selection import tournament_selection

# Mapowanie nazw funkcji na odpowiednie funkcje
mutation_functions = {
    "gaussian_mutation": gaussian_mutation,
}

crossover_functions = {
    "one_point_crossover": one_point_crossover,
}

selection_functions = {
    "tournament_selection": tournament_selection,
}

def run_genetic_algorithm(mutation_function, crossover_function, selection_function, mutation_rate, elitism_rate, pop_size, gens, x_min, x_max, dim):
    best_solution = genetic_algorithm(mutation_function, crossover_function, selection_function, mutation_rate, elitism_rate, pop_size, gens, x_min, x_max, dim)
    print("Best solution:", best_solution)
    print("Score:", schwefel(best_solution))

def create_gui():
    root = tk.Tk()
    root.title("Genetic Algorithm Configuration")
    root.geometry("450x550")
    root.resizable(False, False)
    
    style = ttk.Style(root)
    style.theme_use('clam')
    style.configure("TLabel", font=("Helvetica", 10))
    style.configure("TEntry", font=("Helvetica", 10))
    style.configure("TButton", font=("Helvetica", 10, "bold"))
    style.configure("TCombobox", font=("Helvetica", 10))
    
    container = ttk.Frame(root, padding="20 20 20 20")
    container.grid(row=0, column=0, sticky=(tk.N, tk.W, tk.E, tk.S))
    
    r = 0

    # Mutation function
    ttk.Label(container, text="Select Mutation Function:").grid(row=r, column=0, sticky=tk.W, pady=5)
    mutation_options = ["gaussian_mutation"]  # Zostawiamy tylko jedną opcję
    mutation_combobox = ttk.Combobox(container, values=mutation_options, state="readonly")
    mutation_combobox.grid(row=r, column=1, pady=5, sticky=tk.EW)
    mutation_combobox.set("gaussian_mutation")
    r += 1

    # Crossover function
    ttk.Label(container, text="Select Crossover Function:").grid(row=r, column=0, sticky=tk.W, pady=5)
    crossover_options = ["one_point_crossover"]  # Zostawiamy tylko jedną opcję
    crossover_combobox = ttk.Combobox(container, values=crossover_options, state="readonly")
    crossover_combobox.grid(row=r, column=1, pady=5, sticky=tk.EW)
    crossover_combobox.set("one_point_crossover")
    r += 1

    # Selection function
    ttk.Label(container, text="Select Selection Function:").grid(row=r, column=0, sticky=tk.W, pady=5)
    selection_options = ["tournament_selection"]  # Zostawiamy tylko jedną opcję
    selection_combobox = ttk.Combobox(container, values=selection_options, state="readonly")
    selection_combobox.grid(row=r, column=1, pady=5, sticky=tk.EW)
    selection_combobox.set("tournament_selection")
    r += 1

    # Mutation rate
    ttk.Label(container, text="Mutation Rate:").grid(row=r, column=0, sticky=tk.W, pady=5)
    mutation_rate_entry = ttk.Entry(container)
    mutation_rate_entry.grid(row=r, column=1, pady=5, sticky=tk.EW)
    mutation_rate_entry.insert(0, str(MUT_RATE))
    r += 1

    # Elitism rate
    ttk.Label(container, text="Elitism Rate (0 for none):").grid(row=r, column=0, sticky=tk.W, pady=5)
    elitism_rate_entry = ttk.Entry(container)
    elitism_rate_entry.grid(row=r, column=1, pady=5, sticky=tk.EW)
    elitism_rate_entry.insert(0, "1")
    r += 1

    # Population size
    ttk.Label(container, text="Population Size (POP_SIZE):").grid(row=r, column=0, sticky=tk.W, pady=5)
    pop_size_entry = ttk.Entry(container)
    pop_size_entry.grid(row=r, column=1, pady=5, sticky=tk.EW)
    pop_size_entry.insert(0, str(POP_SIZE))
    r += 1

    # Generations
    ttk.Label(container, text="Generations (GENS):").grid(row=r, column=0, sticky=tk.W, pady=5)
    gens_entry = ttk.Entry(container)
    gens_entry.grid(row=r, column=1, pady=5, sticky=tk.EW)
    gens_entry.insert(0, str(GENS))
    r += 1

    # X Min
    ttk.Label(container, text="X Min (X_MIN):").grid(row=r, column=0, sticky=tk.W, pady=5)
    x_min_entry = ttk.Entry(container)
    x_min_entry.grid(row=r, column=1, pady=5, sticky=tk.EW)
    x_min_entry.insert(0, str(X_MIN))
    r += 1

    # X Max
    ttk.Label(container, text="X Max (X_MAX):").grid(row=r, column=0, sticky=tk.W, pady=5)
    x_max_entry = ttk.Entry(container)
    x_max_entry.grid(row=r, column=1, pady=5, sticky=tk.EW)
    x_max_entry.insert(0, str(X_MAX))
    r += 1

    # Dimensions
    ttk.Label(container, text="Dimensions (DIM):").grid(row=r, column=0, sticky=tk.W, pady=5)
    dim_entry = ttk.Entry(container)
    dim_entry.grid(row=r, column=1, pady=5, sticky=tk.EW)
    dim_entry.insert(0, str(DIM))
    r += 1
    
    ttk.Label(container, text="Iteration (ITERATION):").grid(row=r, column=0, sticky=tk.W, pady=5)
    iteration_entry = ttk.Entry(container)
    iteration_entry.grid(row=r, column=1, pady=5, sticky=tk.EW)
    iteration_entry.insert(0, str(ITERATION))
    r += 1

    # Run button
    def on_run_button_click():
        mutation_function_name = mutation_combobox.get()
        crossover_function_name = crossover_combobox.get()
        selection_function_name = selection_combobox.get()

        # Przypisanie funkcji do zmiennych na podstawie nazw
        mutation_function = mutation_functions[mutation_function_name]
        crossover_function = crossover_functions[crossover_function_name]
        selection_function = selection_functions[selection_function_name]

        mutation_rate = float(mutation_rate_entry.get())
        elitism_rate = int(elitism_rate_entry.get())
        pop_size = int(pop_size_entry.get())
        gens = int(gens_entry.get())
        x_min = float(x_min_entry.get())
        x_max = float(x_max_entry.get())
        dim = int(dim_entry.get())
        iteration = int(iteration_entry.get())

        run_genetic_algorithm(mutation_function, crossover_function, selection_function, mutation_rate, elitism_rate, pop_size, gens, x_min, x_max, dim)

    run_button = ttk.Button(container, text="Run Genetic Algorithm", command=on_run_button_click)
    run_button.grid(row=r, column=0, columnspan=2, pady=20)

    for child in container.winfo_children():
        child.grid_configure(padx=5)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
