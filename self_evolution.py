def self_evolution(D, G, N, m, depot):
    G = G*1.0
    G[G==-1] = float("inf")
    [p, s] = prob_generator(G, D)
    optimal_length = 0
    optimal_path = []
    record_length = []
    record_optimal = []
    for i in range(N):
        cur = []
        for j in range(m):
            cur.append(depot[j])
        length = []
        for j in range(m):
            length.append(1)
        targets = range(len(D))
        path = []
        for j in range(m):
            path.append([depot[j]])
        while len(targets) != 0:
            veilcles = range(m)
            for k in range(m):
                index = np.random.choice(veilcles)
                veilcles.remove(index)
                if len(targets) == 0:
                    break
                random_num = np.random.uniform(0,1)
                prob = p[cur[index]][targets]/sum(p[cur[index]][targets])
                cum_prob = 0
                j = 0
                while cum_prob < random_num:
                    cum_prob = cum_prob + prob[j]
                    j = j + 1
                path[index].append(D[targets[j - 1]])
                length[index] = length[index] * p[cur[index]][targets[j - 1]]
                cur[index] = D[targets[j-1]]
                targets.remove(targets[j - 1])
        if optimal_length < min(length):
            optimal_length = min(length)
            optimal_path = path
        record_length.append(-math.log(min(length)))
        record_optimal.append(-math.log(optimal_length))
    return [optimal_path, -math.log(optimal_length), record_length, record_optimal]


def target2path(nodes, path):
    result = []
    for i in range(len(nodes)-1):
        result = result + path[nodes[i]][nodes[i+1]]
    return result
