def Label(G, D):
    label = [None] * len(G)
    label[0] = "depot"
    for i in D:
        label[i] = "target"
    for i in range(len(G)):
        if label[i] is None:
            label[i] = "inter"
    return label
