def Cluster(G, label):
    cluster = [None] * len(G)
    cluster[0] = 0
    target = 1
    inter = 1
    for i in range(1, len(G)):
        if cluster[i] is None:
            if label[i] is "inter":
                DFS(cluster, G, i, inter, "inter")
                inter = inter + 1
            else:
                DFS(cluster, G, i, target, "target")
                target = target + 1
    return cluster

def get_total_target(label, cluster):
    return max(np.array(cluster)[np.array(label) == "target"])

def get_total_inter(label, cluster):
    return max(np.array(cluster)[np.array(label) == "inter"])

def get_target(label, cluster, index):
    res = []
    for i in range(1, len(label)):
        if label[i] == "target" and cluster[i] == index:
            res.append(i)
    return res

def get_inter(label, cluster, index):
    res = []
    for i in range(1, len(label)):
        if label[i] == "inter" and cluster[i] == index:
            res.append(i)
    return res

def Depot2Target(label, cluster, G):
    target = get_total_target(label, cluster)
    depot2target = []
    for i in range(target):
        temp = []
        targets = get_target(label, cluster, i + 1)
        for j in targets:
            if G[0][j] != -1:
                temp.append([0, j])
        depot2target.append(temp)
    return depot2target
    
def Depot2Inter(label, cluster, G):
    inter = get_total_inter(label, cluster)
    depot2inter = []
    for i in range(inter):
        temp = []
        inters = get_inter(label, cluster, i + 1)
        for j in inters:
            if G[0][j] != -1:
                temp.append([0, j])
        depot2inter.append(temp)
    return depot2inter

def Inter2Target(label, cluster, G):
    inter = get_total_inter(label, cluster)
    target = get_total_target(label, cluster)
    depot2inter = []
    for i in range(inter):
        for j in range(target):
            temp = []
            inters = get_inter(label, cluster, i + 1)
            targets = get_target(label, cluster, j + 1)
            for m in inters:
                for n in targets:
                    if G[m][n] != -1:
                        temp.append([m, n])
            depot2inter.append(temp)
    return np.array(depot2inter).reshape(inter, target)
