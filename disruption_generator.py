def disruption_generator(R, T):
    disruption = []
    for i in range(T):
        random_matrix = np.random.sample([R.shape[0], R.shape[1]]) < R
        indexs = np.where(random_matrix)
        for j in range(len(indexs[0])):
            if (indexs[0][j] < indexs[1][j]):
                disruption.append([indexs[0][j], indexs[1][j], i])
    return disruption
