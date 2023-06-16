from production_line_simulator.optimization import Optimization

if __name__ == "__main__":
    initial_layout = [1, 2, 3, 4, 5]  # Example: Machines represented by integers

    optimizer = Optimization(initial_layout)

    # Simulate and evaluate the initial layout
    initial_fitness = optimizer.evaluate_layout(initial_layout)
    print("Initial Layout:", initial_layout)
    print("Initial Fitness:", initial_fitness)

    # Optimize the layout using genetic algorithm
    optimized_layout = optimizer.optimize_layout()
    optimized_fitness = optimizer.evaluate_layout(optimized_layout)

    print("Optimized Layout:", optimized_layout)
    print("Optimized Fitness:", optimized_fitness)
