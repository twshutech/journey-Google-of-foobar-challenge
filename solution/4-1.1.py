from bisect import bisect_left, bisect_right
rightnext = lambda l,s:l[bisect_right(sorted(l), s)]
leftnext = lambda l,s:l[bisect_left(sorted(l), s)]


class progression:
  def __init__(self):
    self.at = 0   # The current location.
    self.moves = 0  # Numbers of moves that the path took.
    self.progression = 0  # Numbers of bunnies which has been safed.
    self.bunnies = list([]) # List of bunnies which has been safed.

  def update_at(self, move_to):
    self.at = move_to

  def update_progression(self, shortcut):
    self.progression = shortcut

def own(bunny):
  return list([]) if bunny == None else bunnies.append(bunny)

def availables(progression, row):
  print 'progression.at',progression.at
  print 'Right',sorted(row),'available',rightnext(row, progression.at), bisect_right(row, progression.at, 5)
  print 'Left',sorted(row),'available',leftnext(row, progression.at), bisect_left(row, progression.at, 5)

def solution(times, time_limit):
  global bunnies, gatestate, safes
  bunnies = list([])
  gatestate = True
  safes = dict({})

  try:
    search = progression()
    availables(search, times[search.at])
  except IndexError:
    print 'IndexError'
  finally:
    for time in times:
      print time

  return bunnies


print solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1)