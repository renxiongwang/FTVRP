def crossover(pop, pc):
    res = []
    for i in range(len(pop)):
        rand = np.random.uniform(0, 1)
        if rand < pc:
            res.append(cross(pop[i], pop[(i+1)%len(pop)]))
        else:
            res.append(pop[i])
    return res
            
