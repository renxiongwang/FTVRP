def prob_generator(G, D):
    p = np.zeros((len(G), len(D)))
    s = np.zeros((len(G), len(D)))
    for i in range(len(D)):
        BFS(G, D, p, s, i, D[i])
    return [p, s]

def BFS(G, D, p, s, i, node):
    if node == D[i]:
        queue = []
        s[node][i] = node
        for j in range(len(G)):
            if G[node][j] != float("inf"):
                if p[j][i] < math.exp(-G[node][j]):
                    p[j][i] = math.exp(-G[node][j])
                    s[j][i] = node
                    queue.append(j)
        for k in queue:
            BFS(G, D, p, s, i, k)
    else:
        queue = []
        for j in range(len(G)):
            if G[node][j] != float("inf") and j != D[i]:
                if p[j][i] < math.exp(-G[node][j]) * p[node][i]:
                    p[j][i] = math.exp(-G[node][j]) * p[node][i]
                    s[j][i] = node
                    queue.append(j)
        for k in queue:
            BFS(G, D, p, s, i, k)
