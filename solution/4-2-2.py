import numpy as np

isntfar = lambda m, max_distance: True if np.hypot(m[0], m[1]) <= max_distance else False

class vectors:
  def __init__(self, dimensions, your_position, trainer_position, distance):
    self.dimensions = dimensions
    self.your_position = np.array(your_position)
    self.trainer_position = np.array(trainer_position)
    self.distance = distance
    self.vectors_list = np.array([(i,j) for j in range(distance) for i in range(distance)])
    self.directions = set([])
    self.d = np.array([(1,1), (-1,1), (1, -1), (-1, -1)])

  def direction(self):
    l = np.where(isntfar(self.vectors_list, self.distance))
    print l
    for delta in self.vectors_list:
      for trans in self.d:
        print delta * trans

def solution(dimensions, your_position, trainer_position, distance):
  v = vectors(dimensions, your_position, trainer_position, distance)
  v.direction()

solution([3,2], [1,1], [2,1], 4)
