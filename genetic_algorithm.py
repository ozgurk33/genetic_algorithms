'''
What is Genetic algorithm?

The genetic algorithm is a stochastic method for function optimization inspired by the process 
of natural evolution - select parents to create children using the crossover and mutation processes.

Coding it in python: The algorithm consists of the following key steps:
1. Initialize a population of binary bitstrings with random values.
2. Decode the binary bitstrings into numerical values and evaluate the fitness (the objective function)
for each individual in the population.
3. Select the best individuals from the population using tournament selection based on the fitness scores.
4.Create new offsprings from the selected individuals using the crossover operation.
5. Apply the mutation operation on the offsprings to maintain diversity in the population.
6. Repeat steps 2 to 5 until a stopping criterion is met.
'''

from numpy.random import randint
from numpy.random import rand
import random
import math

def objective(x):
    y = math.exp(((x[0]-7)**2) + (x[1]-9)**2)
    return y

def decode(bounds,n_bits, bitstring):
    decoded = []
    largest = 2**n_bits

    for i in range(len(bounds)):
        start, end = i * n_bits, (i * n_bits) + n_bits
        substring = bitstring[start:end]

        chars = ''.join([str(s) for s in substring])
        integer = int(chars, 2)

        value = bounds[i][0] + (integer/largest) * (bounds[i][1] - bounds[i][0])
        decoded.append(value)
    return decoded

def selection(pop, scores, k=3):
    selection_ix = randint(len(pop))
    for ix in randint(0, len(pop), k-1):
        if scores[ix] < scores[selection_ix]:
            selection_ix = ix
    
    return pop[selection_ix]

def crossover(p1, p2, r_cross):
    c1, c2 = p1.copy(), p2.copy()
    if rand() < r_cross:
        pt = randint(1, len(p1)-2)

        c1 = p1[:pt] + p2[pt:]
        c2 = p2[:pt] + p1[pt:]
    
    return [c1,c2]

def mutation(bitstring, r_mut):
    rand = random.random
    for i in range(len(bitstring)):
        if rand() < r_mut:
            bitstring[i] = 1 - bitstring[i]
    
    return bitstring

def genetic_algorithm(objective, bounds, n_bits, n_iter, n_pop, r_cross, r_mut):
    pop = [randint(0,2, n_bits * len(bounds)).tolist() for _ in range(n_pop)]

    best, best_eval = 0, objective(decode(bounds, n_bits, pop[0]))

    for gen in range(n_iter):
        decoded = [decode(bounds, n_bits, p) for p in pop]

        scores = [objective(d) for d in decoded]

        for i in range(n_pop):
            if scores[i] < best_eval:
                best, best_eval = pop[i], scores[i]
                print(">%d, new best f(%s) = %f" % (gen, decoded[i], scores[i]))
        
        selected = [selection(pop, scores) for _ in range(n_pop)]

        children = list()
        for i in range(0, n_pop, 2):
            p1,p2 = selected[i], selected[i+1]

            for c in crossover(p1,p2, r_cross):
                mutation(c,r_mut)
                children.append(c)
        pop = children

    return [best,best_eval] 


if __name__ == "__main__":
    
    bounds = [[-10.0, 10.0], [-10.0, 10.0]]
    n_iter = 100
    n_bits = 16
    n_pop = 100
    r_cross = 0.9
    r_mut = 1.0 / (float(n_bits) * len(bounds))
    best, score = genetic_algorithm(objective, bounds, n_bits, n_iter, n_pop, r_cross, r_mut)
    print('###########################################################')
    decoded = decode(bounds, n_bits, best)
    print('The result is (%s) with a score of %f' % (decoded, score))
