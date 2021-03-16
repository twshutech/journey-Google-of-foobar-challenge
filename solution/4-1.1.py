class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'

  def disable(self):
    self.HEADER = ''
    self.OKBLUE = ''
    self.OKGREEN = ''
    self.WARNING = ''
    self.FAIL = ''
    self.ENDC = ''

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
getmin = lambda item:item[1]
iteminside = lambda item,l: True if item in l else False

class graphic:
  def __init__(self, times, time_limit, fromto):
    self.graph = times
    self.budget = time_limit
    self.fromto = fromto
    self.distances = [set()]*len(times)
    self.edge = len(times)
    self.dajavu = set([])
    self.costs = [float('inf')] * len(times)
    self.tokens = [0] * len(times)
    self.generatorlen = 0

  def validator(self):
    return False if len(self.dajavu) == self.edge-2 or self.fromto == self.edge-1 and self.budget >= 0 else True

  def getless(self, row):
    for i in xrange(self.edge):
      node = row[i]
      if self.edge >= i >0 and node != 0:
        if self.costs[i] > node:
          self.costs[i] = node
          self.distances[i] = set([row.index(0)])
        elif self.costs[i] == node:
          self.distances[i].add(row.index(0))

  def indexof(self):
    i = float('inf')
    for node in [index for index in xrange(len(self.distances)) if self.fromto in self.distances[index]]:
      yield node

  def hasbulkhead(self):
    return True if self.edge-1 in self.distances[self.fromto] else False

  def g(self, gen):
    try:
      n = gen.next()
      if n not in self.dajavu:
        return n
      elif n in self.dajavu:
        self.tokens[n] -= 1
        if self.tokens[n] != 0:
          return g(gen)
    except Exception as exception:
      gen.close()
      return n

  def relationtree(self):
    print 'distances',self.distances
    print 'tokens',self.tokens
    print 'cost',self.costs
    while self.validator():
      try:
        gen = self.indexof()
        for n in gen:
          if self.tokens[n] > 0:
            if self.hasbulkhead and self.costs[self.edge-1] == self.budget:
              print 'has'
              self.fromto = self.edge-1
              break
          if self.edge-1>n>0:
            self.dajavu.add(n-1)
        self.budget -= self.costs[self.fromto]
        print self.budget
        # if self.budget == 0 and self.fromto == self.edge-1:
      except KeyError:
        return sorted(list(self.dajavu))
      except RuntimeError:
        return sorted(list(self.dajavu))
      except TypeError:
        return sorted(list(self.dajavu))
    return sorted(list(self.dajavu))

  # def shuttlefun(self):




def solution(times, time_limit):
  graph = graphic(times, time_limit, 0)

  # getless(times[graph.fromto], graph)
  # graph.relationtree()
  # try:
  # except RuntimeError:
  #   return graph.costs
  # finally:
  #   return graph.distances

  for edge in xrange(graph.edge):
    row = times[edge]
    graph.getless(row)

  graph.tokens = [len(item) for item in graph.distances]
  return graph.relationtree()

l1 = [[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]]
l2 = [[0,  1,  5,  5,  2],[10, 0,  2,  6,  10],[10, 10, 0,  1,  5],[10, 10, 10, 0,  1],[10, 10, 10, 10, 0]]
l3 = [[0, 1, 3, 4, 2],[10, 0, 2, 3, 4],[10, 10, 0, 1, 2],[10, 10, 10, 0, 1],[10, 10, 10, 10, 0]]
l4 = [[0, 2, 2, 2, -1],[9, 0, 2, 2, -1],[9, 3, 0, 2, -1],[9, 3, 2, 0, -1],[9, 3, 2, 2, 0]]
l5 = [[0,  1, 10, 10, 10],[10, 0,  1,  1,  2],[10, 1,  0, 10, 10],[10, 1,  10, 0, 10],[10, 10, 10, 10, 0]]
l6 = [[0, 1, 1, 1, 1],[1, 0, 1, 1, 1],[1, 1, 0, 1, 1],[1, 1, 1, 0, 1],[1, 1, 1, 1, 0]]
l7 = [[0, 5, 11, 11, 1],[10, 0, 1, 5, 1],[10, 1, 0, 4, 0],[10, 1, 5, 0, 1],[10, 10, 10, 10, 0]]
# print('l5: ',solution(l5, 7), '[0, 1, 2]') #Check
# print('l3: ',solution(l3, 4), '[]') #Check
# print('l7: ',solution(l7, 10),'[0, 1]')#Check
# print('below are passed')
# print(solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3))
# print('l1: ',solution(l1, 1), )
# print('l2: ',solution(l2, 5), '[0, 1, 2]')
# print('l4: ',solution(l4, 1), '[1, 2]')
print('l6: ',solution(l6, 3),'[0, 1]')