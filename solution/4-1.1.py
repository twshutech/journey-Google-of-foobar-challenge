def getless(row, dajavu):
  num = {'index':row.index(min(row)), 'cost': min(row),'dajavu': dajavu}
  print(num)
  for i, node in enumerate(row):
    if num['cost'] == 0:
      num['cost'] = node
    if node < num['cost'] and node != 0 and str(i) not in dajavu:
      print(node, i)
    if (node < num['cost'] and node != 0) and str(i) not in dajavu and i != 0:
      num['cost'] = node
      num['index'] = i
  return num

def solution(times, time_limit):
  least = ''
  s = 0
  node = []
  for row in times:
    item = getless(row, least)
    least += str(item['index'])
  print(least)
  for i in least:
    i = int(i)
    time_limit -= times[s][i]
    s = i
    if i != len(times)-1 and (times[s][i]>times[s][-1] or time_limit == times[s][-1]):
      time_limit -= times[s][-1]
    if time_limit >= 0 and i not in [0, len(times)-1]:
      node.append(i-1)
  return node

l = [[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]]

# for row in [[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]]:
#   d = ''
#   print(getless(row, d))
print(solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3))
print(solution(l, 1))