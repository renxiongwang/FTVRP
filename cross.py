def cross(pop1, pop2):
    rand1 = np.random.randint(0, len(pop1))
    rand2 = np.random.randint(0, len(pop2))
    if rand2 < rand1:
        rand1, rand2 = rand2, rand1
    seg1 = pop1[rand1:rand2+1]
    seg2 = pop2[rand1:rand2+1]
    j = 0
    for i in range(len(pop1)):
        if j == rand1:
            j = rand2+1
        if pop2[i] not in seg1:
            pop1[j] = pop2[i]
            j = j+1
    res = pop1[:]
    return res
