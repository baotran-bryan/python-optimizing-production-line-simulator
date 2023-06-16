import random
from time import sleep

NUM_MACHINES = 5
NUM_PRODUCTS = 3

class Optimization:
    def __init__(self, initial_layout):
        self.initial_layout = initial_layout

    def simulate_production_line(self, layout):
        # Initialize machine states
        machine_states = [0] * NUM_MACHINES

        # Simulate production line
        for product in range(NUM_PRODUCTS):
            print(f"Product {product} is being processing...")
            for machine_idx, machine_id in enumerate(layout):
                # Perform operation on the machine
                print(f"Machine {machine_id} is processing product {product}")
                machine_states[machine_idx] += machine_id
            print(f"{product} finished processing")

        return machine_states

    def evaluate_layout(self, layout):
        # Simulate production line
        machine_states = self.simulate_production_line(layout)

        # Calculate fitness based on the total machine states
        fitness = sum(machine_states)

        return fitness

    def optimize_layout(self, generations=100, population_size=100, mutation_rate=0.1):
        population = [self.initial_layout[:] for _ in range(population_size)]

        for _ in range(generations):
            # Evaluate fitness for each layout in the population
            fitness_scores = [self.evaluate_layout(layout) for layout in population]

            # Select parents for reproduction (tournament selection)
            parents = []
            for _ in range(population_size):
                idx1, idx2 = random.sample(range(population_size), 2)
                parent1 = population[idx1]
                parent2 = population[idx2]
                if fitness_scores[idx1] > fitness_scores[idx2]:
                    parents.append(parent1)
                else:
                    parents.append(parent2)

            # Create offspring through crossover (single-point crossover)
            offspring = []
            for i in range(0, population_size, 2):
                parent1 = parents[i]
                parent2 = parents[i + 1]
                crossover_point = random.randint(1, len(self.initial_layout) - 1)
                child1 = parent1[:crossover_point] + parent2[crossover_point:]
                child2 = parent2[:crossover_point] + parent1[crossover_point:]
                offspring.extend([child1, child2])

            # Apply mutation (swap mutation)
            for i in range(population_size):
                if random.random() < mutation_rate:
                    idx1, idx2 = random.sample(range(len(self.initial_layout)), 2)
                    offspring[i][idx1], offspring[i][idx2] = offspring[i][idx2], offspring[i][idx1]

            # Replace the old population with the offspring
            population = offspring

        # Evaluate final fitness scores
        fitness_scores = [self.evaluate_layout(layout) for layout in population]

        # Return the best layout (highest fitness score)
        best_layout = population[fitness_scores.index(max(fitness_scores))]
        return best_layout

