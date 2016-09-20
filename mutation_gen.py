def mutation_gen(indiv):
    rand1 = np.random.randint(0, len(indiv))
    rand2 = np.random.randint(0, len(indiv))
    indiv[rand1], indiv[rand2] = indiv[rand2], indiv[rand1]
