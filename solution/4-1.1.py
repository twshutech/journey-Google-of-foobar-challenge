# [
# [0,  1, 10, 10, 10],
# [10, 0,  1,  1,  2],
# [10, 1,  0, 10, 10],
# [10, 1,  10, 0, 10],
# [10, 10, 10, 10, 0]
# ]
# 7


# Start  End  Delta Time Status
#     -   0     -    7   Bulkhead initially open
#     0   1     1    6
#     1   2     1    5
#     2   1     1    4   Return to bunny 1, since bunny 2 does not have potential.
#     1   3     1    3
#     3   1     1    2   Return to bunny 1, since bunny 3 does not have potential.
#     1   4     2    0   The bunnies exit.

def getless(row, dajavu, graph):
  num = {'index':row.index(0), 'cost': float('inf'),'dajavu': dajavu}
  for i, node in enumerate(row):
    if 0 < i < graph.edge-1:
      if graph.distances[i-1][1] >= node and node != 0:
        graph.distances[i-1][1] = node
        graph.distances[i-1][0] = row.index(0)

    # if node != 0 and str(i) in dajavu:
    #   print('special case',i,node)
      # num['cost'] = node
      # num['index'] = i
    if (node < num['cost'] and node != 0) and str(i) not in dajavu and i != 0:
      # print('regular concern',i,node)
      num['cost'] = node
      num['index'] = i
  # print(num)
  print(graph.distances)
  print('')
  return num

class graphic:
  def __init__(self, times):
    self.graph = times
    self.distances = dict()
    self.edge = len(times)

  def initdis(self):
    for bunny in xrange(len(self.graph) - 2):
      self.distances[bunny] = [0, float('inf')] #from, min cost

def solution(times, time_limit):
  graph = graphic(times)
  graph.initdis()
  print(graph.distances)
  least = ''
  s = 0
  node = []
  budget = time_limit
  for row in times:
    item = getless(row, least, graph)
    try:
      print(graph.distances[s])
    except KeyError:
      return
    finally:


      print('now',s,'then',item['index'])
    least += str(item['index'])
    budget -= times[s][item['index']]
    s = item['index']
  for i in least:
    i = int(i)
    time_limit -= times[s][i]
    s = i
    if i != len(times)-1 and (times[s][i]>times[s][-1] or time_limit == times[s][-1]):
      time_limit -= times[s][-1]
    if time_limit >= 0 and i not in [0, len(times)-1]:
      node.append(i-1)
  return node


l1 = [[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]]
l2 = [[0,  1,  5,  5,  2],[10, 0,  2,  6,  10],[10, 10, 0,  1,  5],[10, 10, 10, 0,  1],[10, 10, 10, 10, 0]]
l3 = [[0, 1, 3, 4, 2],[10, 0, 2, 3, 4],[10, 10, 0, 1, 2],[10, 10, 10, 0, 1],[10, 10, 10, 10, 0]]
l4 = [[0, 2, 2, 2, -1],[9, 0, 2, 2, -1],[9, 3, 0, 2, -1],[9, 3, 2, 0, -1],[9, 3, 2, 2, 0]]
l5 = [[0,  1, 10, 10, 10],[10, 0,  1,  1,  2],[10, 1,  0, 10, 10],[10, 1,  10, 0, 10],[10, 10, 10, 10, 0]]
l6 = [[0, 1, 1, 1, 1],[1, 0, 1, 1, 1],[1, 1, 0, 1, 1],[1, 1, 1, 0, 1],[1, 1, 1, 1, 0]]
l7 = [[0, 5, 11, 11, 1],[10, 0, 1, 5, 1],[10, 1, 0, 4, 0],[10, 1, 5, 0, 1],[10, 10, 10, 10, 0]]
print('needs to check')
print('l5: ',solution(l5, 7), '[0, 1, 2]') #Check
# print('l3: ',solution(l3, 4), '[]') #Check
# print('l7: ',solution(l7, 10),'[0, 1]')#Check
# print('below are passed')
# print(solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3))
# print('l1: ',solution(l1, 1), )
# print('l2: ',solution(l2, 5), '[0, 1, 2]')
# print('l4: ',solution(l4, 1), '[1, 2]')
# print('l6: ',solution(l6, 3),'[0, 1]')
