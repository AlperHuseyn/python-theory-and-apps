""" My approach to practice question #6.7 """
import itertools


# Travel salesman problem: tsp
def tsp(cities, distances, starting_point):
    shortest_path = None
    shortest_distance = float('inf')
    for path in itertools.permutations(cities):
        path += (starting_point, )
        if path[0] != starting_point:
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


c = ['Istanbul', 'Bursa', 'Corum', 'Denizli', 'Edirne', 'Ordu', 'Giresun']
sp = 'Istanbul'
d = {'Istanbul': {'Bursa': 5, 'Corum': 7, 'Denizli': 10},
     'Bursa': {'Istanbul': 5, 'Denizli': 4, 'Edirne': 17, 'Giresun': 20},
     'Corum': {'Istanbul': 7, 'Denizli': 6, 'Ordu': 9},
     'Denizli': {'Istanbul': 10, 'Bursa': 4, 'Corum': 6, 'Edirne': 3, 'Ordu': 12},
     'Edirne': {'Bursa': 17, 'Denizli': 3, 'Ordu': 14, 'Giresun': 6},
     'Ordu': {'Corum': 9, 'Denizli': 12, 'Edirne': 14, 'Giresun': 10},
     'Giresun': {'Bursa': 20, 'Edirne': 6, 'Ordu': 10}}

s_path, s_distance = tsp(c, d, sp)
print(f'Shortest path: {s_path}')
print(f'Shortest distance: {s_distance}')
