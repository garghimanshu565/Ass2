from sys import maxsize
from itertools import permutations
V = 4

def tsp(G, start):
    vertex = []
    for i in range(V):
        if i != start:
            vertex.append(i)

    min_path_weight = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:
        pathweight = 0
        j = start
        for k in i:
            pathweight += G[j][k]
            j = k
        pathweight += G[j][start]
        min_path_weight = min(min_path_weight, pathweight)

    return min_path_weight
G = [[0, 10, 15, 20], [10, 0, 35, 25],[15, 35, 0, 30], [20, 25, 30, 0]]
start = int(input("Enter starting point "))
print(tsp(G, start))
