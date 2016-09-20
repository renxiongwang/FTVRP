def getpath(s, D):
    path = [[[]]*len(G)]*len(G)
    for i in range(len(D)):
        path[0][D[i]] = path[0][D[i]] + [0]
        j = s[0][i]
        while  j != D[i]:
            path[0][D[i]] = path[0][D[i]] + [j]
            j = s[j][i]
        path[0][D[i]] = path[0][D[i]] + [j]
    for i in range(len(D)):
        path[D[i]][0] = reversed(path[0][D[i]])
    for i in range(len(D)):
        for j in range(len(D)):
            if D[i] != D[j]:
                path[D[i]][D[j]] = path[D[i]][D[j]] + [D[i]]
                k = s[D[i]][j]
                while  k != D[j]:
                    path[D[i]][D[j]] = path[D[i]][D[j]] + [k]
                    k = s[k][j]
                path[D[i]][D[j]] = path[D[i]][D[j]] + [k]
    return path
