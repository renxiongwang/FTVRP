def readdata(path):
    file = open(path)
    N = int(file.readline())
    G = []
    for i in range(N):
        G.append(map(int, file.readline().split(',')))
    G = np.array(G)
    D = np.array(map(int, file.readline().split(','))) - 1
    R = []
    for i in range(N):
        R.append(map(float, file.readline().split(',')))
    R = np.array(R)
    M = int(file.readline())
    m = int(file.readline())
    d = int(file.readline()) - 1
    file.close()
    return [N, G, D, R, M, m, d]
