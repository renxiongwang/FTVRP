def getlength(path, p, D, depot):
    length = p[depot][path[0]]
    for i in range(len(path) - 1):
        length = length * p[D[path[i]]][path[i+1]]
    return length
