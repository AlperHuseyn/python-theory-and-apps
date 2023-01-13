""" Instructor solution for practice question #6.7 """
import sys
import itertools

d = {'A': {'B': 5, 'C': 7, 'D': 10},
     'B': {'A': 5, 'D': 4, 'E': 17, 'G': 20},
     'C': {'A': 7, 'D': 6, 'F': 9},
     'D': {'A': 10, 'B': 4, 'C': 6, 'E': 3, 'F': 12},
     'E': {'B': 17, 'D': 3, 'F': 14, 'G': 6},
     'F': {'C': 9, 'D': 12, 'E': 14, 'G': 10},
     'G': {'B': 20, 'E': 6, 'F': 10}}


def is_valid_tour(permu):
    total = 0
    for i in range(len(permu) - 1):
        lngth = d[permu[i]].get(permu[i + 1])
        if not lngth:
            return 0
        total += lngth

    return total


s_distance = sys.float_info.max
s_path = None

for pe in itertools.permutations('BCDEFG'):
    pe = ('A',) + pe + ('A',)
    length = is_valid_tour(pe)
    if length:
        if length < s_distance:
            s_distance = length
            s_path = pe

print(f'Shortest path: {s_path}')
print(f'Shortest distance: {s_distance}')

#######################################################################################################################
#######################################################################################################################

# No need to import sys for assigning the max value to s_distance
import itertools

d = {'A': {'B': 5, 'C': 7, 'D': 10},
     'B': {'A': 5, 'D': 4, 'E': 17, 'G': 20},
     'C': {'A': 7, 'D': 6, 'F': 9},
     'D': {'A': 10, 'B': 4, 'C': 6, 'E': 3, 'F': 12},
     'E': {'B': 17, 'D': 3, 'F': 14, 'G': 6},
     'F': {'C': 9, 'D': 12, 'E': 14, 'G': 10},
     'G': {'B': 20, 'E': 6, 'F': 10}}


def is_valid_tour(t):
    total = 0
    for i in range(len(t) - 1):
        length = d[t[i]].get(t[i + 1])
        if not length:
            return 0
        total += length

    return total


s_path = None
s_distance = None

for t in itertools.permutations('BCDEFG'):
    t = ('A', ) + t + ('A', )
    length = is_valid_tour(t)
    if not length:
        s_distance = length
        s_path = t
    elif length < s_distance:
        s_distance = length
        s_path = t
