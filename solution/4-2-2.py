import numpy as np

unit_vector = lambda vector:vector / np.linalg.norm(vector)
vector_magnitude = lambda m: np.hypot(m[0], m[1])
vector_angle = lambda m: np.arctan2(m[0], m[1]) * 180 / np.pi
scalar = lambda
isntfar = lambda m, max_distance: True if vector_magnitude(m) <= max_distance else False
collision = lambda
class vectors:
  def __init__(self, dimensions, your_position, trainer_position, distance):
    self.dimensions = dimensions
    self.your_position = np.array(your_position)
    self.trainer_position = np.array(trainer_position)
    self.distance = distance
    self.vectors_list = np.array([(i,j) for j in range(distance + 1) for i in range(distance + 1)])
    self.directions = set([])
    self.d = np.array([(1,1), (-1,1), (1, -1), (-1, -1)])
    self.towall = np.array([])

  def direction(self):
    self.getrelation(self.your_position)
    # l = np.where(isntfar(self.vectors_list, self.distance))
    # print l
    angles = set([])
    temp = set([])
    for delta in self.vectors_list:
      for trans in self.d:
        dot = delta * trans
        # print isntfar(dot, self.distance)
        if isntfar(dot, self.distance):
          angle = vector_angle(dot)
          if angle not in angles:
            tempdot = []
            angles.add(angle)
            print 'dot',dot,self.towall
            tempdot[0] = collision(dot[0], )
          # print angles, len(angles),'\n'
          #   print dot[0],dot[1], dot
          # temp.add(list(dot))
    print len(angles)

  def getrelation(self, dot):
    self.towall = np.array([-1 * dot[1], self.dimensions[1]-dot[1], -1 * dot[0], self.dimensions[0]-dot[0]])

  def bounce(self):



def solution(dimensions, your_position, trainer_position, distance):
  v = vectors(dimensions, your_position, trainer_position, distance)
  v.direction()

solution([3,2], [1,1], [2,1], 4)
