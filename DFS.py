def DFS(cluster, G, index, number, s):
    cluster[index] = number
    for i in range(1, len(G)):
        if G[index][i] != -1:
            if cluster[i] is None and label[i] == s:
                DFS(cluster, G, i, number, s)
