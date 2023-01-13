""" My approach to practice question #6.7 """
import itertools


# Travel salesman problem: tsp
def tsp(cities, distances):
    shortest_path = None
    shortest_distance = float('inf')
    for path in itertools.permutations(cities):
        if path[0] != 'A':
            continue
        valid = True
        distance = 0
        for i in range(len(path) - 1):
            if path[i + 1] not in distances[path[i]]:
                valid = False
                break
            distance += distances[path[i]][path[i + 1]]
        if valid and distance < shortest_distance:
            shortest_path = path
            shortest_distance = distance
    return shortest_path, shortest_distance


c = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
d = {'A': {'B': 5, 'C': 7, 'D': 10},
     'B': {'A': 5, 'D': 4, 'E': 17, 'G': 20},
     'C': {'A': 7, 'D': 6, 'F': 9},
     'D': {'A': 10, 'B': 4, 'C': 6, 'E': 3, 'F': 12},
     'E': {'B': 17, 'D': 3, 'F': 14, 'G': 6},
     'F': {'C': 9, 'D': 12, 'E': 14, 'G': 10},
     'G': {'B': 20, 'E': 6, 'F': 10}}

s_path, s_distance = tsp(c, d)
print(f'Shortest path: {s_path}')
print(f'Shortest distance: {s_distance}')
