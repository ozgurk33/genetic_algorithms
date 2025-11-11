import random

def roulette_selection(population, fitness_scores):
    
    sum_fitness = sum(fitness_scores)

    selection_point = random.uniform(0, sum_fitness)
    
    curr_sum = 0
    for i in range(len(population)):

        curr_sum += fitness_scores[i]
        
        if curr_sum > selection_point:
            return population[i]
            
    return population[-1]


population = ["Chromosome A", "Chromosome B", "Chromosome C", "Chromosome D"]


scores = [20, 50, 5, 25]


print(f"Population: {population}")
print(f"Scores: {scores}\n")

selected_chromosome = roulette_selection(population, scores)
print(f"Selected chromosome is: {selected_chromosome}\n")


print("--- 1000 Selection Simulation ---")
selection_counter = {chromosome: 0 for chromosome in population} 

for _ in range(1000):
    selected = roulette_selection(population, scores)
    
    selection_counter[selected] += 1

print("Selection results (approximate values are expected):")
for chromosome, counter in selection_counter.items():
    
    print(f"{chromosome}: {counter} times selected (Expected ~{scores[population.index(chromosome)] * 10})")