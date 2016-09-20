def mutation(pop, pm):
    for i in range(len(pop)):
        rand = np.random.uniform(0,1)
        if rand < pm:
            mutation_gen(pop[i])
