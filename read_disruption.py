def read_disruption(path):
    disruption = []
    file = open(path)
    line = file.readline()
    while line:
        disruption.append(map(int, line.split(',')))
        line = file.readline()
    file.close()
    return disruption
