import random

target_sentence = "I found what I was looking for!"
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

def mutate(chromosome, prob):
    gene = list(chromosome)
    sum_prob = sum(prob)
    choosen = random.randint(0, sum_prob-1)
    for i in range(len(prob)):
        choosen -= prob[i]
        if choosen < 0:
            index = i
            break
    # index is given ramdomly, proportional to each index's probability.
    gene[index] = random.choice(gene_pool)
    return ''.join(gene), index

if __name__ == "__main__":
    population = [generate_chromosome(len(target_sentence)) for _ in range(population_size)]
    population_fitness = [calculate_fitness(chromosome) for chromosome in population]
    probability_limit = 100
    probability_penalty = 100
    probability = [[probability_limit for _ in range(len(target_sentence))] for _ in range(population_size)]

    for generation in range(10000):
        parent_index = population_fitness.index(max(population_fitness))
        parent = population[parent_index]
        child, changed_index = mutate(parent, probability[parent_index])


        child_fitness = calculate_fitness(child)
        print(f"Generation {generation}: {parent} -> {child}, Child Fitness: {child_fitness}")

        child_probability = probability[parent_index]
        if child_fitness < population_fitness[parent_index]:
            # If child is worce than parent, that change at the index is not good.
            probability[parent_index][changed_index] = max(child_probability[changed_index]-probability_penalty, 0)
        else:
            if child_fitness > population_fitness[parent_index]:
                # If child is better than parent, there is less chance of improvement.
                child_probability[changed_index] = max(child_probability[changed_index]-probability_penalty, 0)
            index_to_replace = population_fitness.index(min(population_fitness))
            population[index_to_replace] = child
            population_fitness[index_to_replace] = child_fitness
            probability[index_to_replace] = child_probability
            # Make the limitation of probability milder if there is no improvement.
            probability = [[min(x+1, probability_limit) for x in y] for y in probability]
        print(f"Current Population: {population}")
        print(f"Current Population Fitness: {population_fitness}")
        #print(f"Current Probability: {probability}")

        if child_fitness == len(target_sentence):
            print(f"Solution found in generation {generation}")
            break

    print(population)
    print(population_fitness)