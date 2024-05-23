import random

target_sentence = "Hello, how are you?"
gene_pool="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!?., "

population_size = 10

def calculate_fitness(chromosome):
    fitness = 0
    for i in range(len(chromosome)):
        if chromosome[i] == target_sentence[i]:
            fitness += 1
    return fitness


def generate_chromosome(length):
    return ''.join(random.choice(gene_pool) for _ in range(length))

def mutate(chromosome):
    gene = list(chromosome)
    index = random.randint(0, len(gene) - 1)
    gene[index] = random.choice(gene_pool)
    return ''.join(gene)

if __name__ == "__main__":
    population = []
    for _ in range(population_size):
        population.append(generate_chromosome(len(target_sentence)))

    population_fitness = []
    for chromosome in population:
        population_fitness.append(calculate_fitness(chromosome))

    for generation in range(10000):
        parent_index = population_fitness.index(max(population_fitness))
        parent = population[parent_index]
        child = mutate(parent)

        print(f"Generation {generation}: {parent} -> {child}")

        child_fitness = calculate_fitness(child)
        print(f"Child Fitness: {child_fitness}")

        index_to_replace = population_fitness.index(min(population_fitness))
        population[index_to_replace] = child
        population_fitness[index_to_replace] = child_fitness

        if child_fitness == len(target_sentence):
            print(f"Solution found in generation {generation}")
            break

    print(population)
    print(population_fitness)