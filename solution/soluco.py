from copy import deepcopy
from itertools import permutations

# I am not happy with this implementation, due to a realization I have recently had:
#   My Bellman-Ford implementation is completely unnecessary. The Floyd algorithm can detect negative cycles, and
#   negative cycles are all I used Bellman-Ford for. Thus, with some refactoring, I could easily make this more
#   efficient.


def powerset(list):
    """
    :param list: The list to generate subsets of.
    :return: A generator that produces all subsets of this set.
    """
    x = len(list)
    masks = [1 << i for i in xrange(x)]
    for i in xrange(1 << x):
        yield [ss for mask, ss in zip(masks, list) if i & mask]


def getneighbourindex(neighbour, graphsize):
    if neighbour == "Bulkhead":
        return graphsize - 1
    elif neighbour == "Start":
        return 0
    else:
        return int(neighbour)+1

def matrix2graph(matrix):
    keys = ["Start"]
    for num in xrange(1, len(matrix)-1):
        keys.append(num-1)
    keys.append("Bulkhead")
    graph = dict(zip(keys, matrix))
    return graph

def initialize(graph, source):
    distance = {}
    predecessor = {}
    for node in graph:
        distance[node] = float('inf')
        predecessor[node] = None
    distance[source] = 0
    return distance, predecessor


def relax(node, neighbour, graph, distance, predecessor):
    nidx = getneighbourindex(neighbour, len(graph))
    if distance[node] + graph[node][nidx] < distance[neighbour]:
        distance[neighbour] = distance[node] + graph[node][nidx]
        predecessor[neighbour] = node

def bellman_ford(matrix, graph, time_limit, source):
    dist, pred = initialize(graph, source)
    for num in xrange(len(graph)-1):
        for node in graph:
            temp = dict(graph)
            del temp[node]
            for neighbour in temp:
                relax(node, neighbour, graph, dist, pred)

    for node in graph:
        for neighbour in graph:
            nidx = getneighbourindex(neighbour, len(graph))
            if dist[node] + graph[node][nidx] < dist[neighbour]:
                return [num for num in xrange(0, len(graph)-2)]

    spaths = floyd(matrix)
    # print 'spaths',spaths
    return find_most_bunnies(matrix, spaths, time_limit)


def floyd(matrix):
    n = len(matrix)
    spaths = deepcopy(matrix)
    for k in xrange(n):
        for i in xrange(n):
            for j in xrange(n):
                if spaths[i][k] + spaths[k][j] < spaths[i][j]:
                    spaths[i][j] = spaths[i][k] + spaths[k][j]
    return spaths


def find_most_bunnies(matrix, spaths, time_limit):
    n = len(matrix)-2
    bunnyids = []
    for num in xrange(n):
        bunnyids.append(num)
    pset = powerset(bunnyids)
    pset = sorted(pset)

    optimal_bunnies = []
    for sub in pset:
        for permutation in permutations(sub):
            # print(permutation)
            subsum = 0
            prev = 0
            next = len(matrix)-1
            for bunnyid in permutation:
                next = bunnyid+1
                subsum += spaths[prev][next]
                prev = next
            subsum += spaths[prev][len(matrix)-1]
            if subsum <= time_limit and len(sub) > len(optimal_bunnies):
                optimal_bunnies = sub
                if len(optimal_bunnies) == n:
                    break
            else:
                pass
    return optimal_bunnies


def solution(times, time_limit):
    if len(times) <= 2:
        return []
    graph = matrix2graph(times)
    return bellman_ford(times, graph, time_limit, "Start")



l1 = [[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]]
l2 = [[0,  1,  5,  5,  2],[10, 0,  2,  6,  10],[10, 10, 0,  1,  5],[10, 10, 10, 0,  1],[10, 10, 10, 10, 0]]
l3 = [[0, 1, 3, 4, 2],[10, 0, 2, 3, 4],[10, 10, 0, 1, 2],[10, 10, 10, 0, 1],[10, 10, 10, 10, 0]]
l4 = [[0, 2, 2, 2, -1],[9, 0, 2, 2, -1],[9, 3, 0, 2, -1],[9, 3, 2, 0, -1],[9, 3, 2, 2, 0]]
l5 = [[0,  1, 10, 10, 10],[10, 0,  1,  1,  2],[10, 1,  0, 10, 10],[10, 1,  10, 0, 10],[10, 10, 10, 10, 0]]
l6 = [[0, 1, 1, 1, 1],[1, 0, 1, 1, 1],[1, 1, 0, 1, 1],[1, 1, 1, 0, 1],[1, 1, 1, 1, 0]]
l7 = [[0, 5, 11, 11, 1],[10, 0, 1, 5, 1],[10, 1, 0, 4, 0],[10, 1, 5, 0, 1],[10, 10, 10, 10, 0]]
print('needs to check')
print('l5: ',solution(l5, 7), '[0, 1, 2]') #Check
print('l3: ',solution(l3, 4), '[]') #Check
print('l7: ',solution(l7, 10),'[0, 1]')#Check
print('below are passed')
print(solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3))
print('l1: ',solution(l1, 1), )
print('l2: ',solution(l2, 5), '[0, 1, 2]')
print('l4: ',solution(l4, 1), '[1, 2]')
print('l6: ',solution(l6, 3),'[0, 1]')
