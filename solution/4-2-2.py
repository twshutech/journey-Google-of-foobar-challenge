import numpy as np
import math

unit_vector = lambda vector:vector / np.linalg.norm(vector)
vector_magnitude = lambda m: math.hypot(m[0], m[1])
vector_angle = lambda m: np.arctan2(m[0], m[1]) * 180 / np.pi
# scalar = lambda
isntfar = lambda m, scalar: True if vector_magnitude(m) <= scalar else False
# collision = lambda
rounds_bouncing = lambda s, r: s//r
# return the least one.
closest = lambda s1, s2: np.less([s1, s2])

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
    self.angle_dict = ({})

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
          # self.update_angle(angle, dot)
          if angle not in angles:
            angles.add(angle)
            # print ('dot', dot,self.towall)
            # self.bounce(dot, )
            # self.bounce()
          # print angles, len(angles),'\n'
          #   print dot[0],dot[1], dot
          # temp.add(list(dot))
    print( len(angles))

  def getrelation(self, dot):
    self.towall = np.array([-1 * dot[1], self.dimensions[1]-dot[1], -1 * dot[0], self.dimensions[0]-dot[0]], dtype=float)

  def update_angle(self, angle, dot):
    # print( 'close',closest(, ))
    if angle in self.angle_dict.keys():
      # scalar = self.angle_dict[angle]
      self.angle_dict.update({angle: dot})

      print(dot,vector_magnitude(dot), vector_magnitude(self.angle_dict[angle]))

  def quadrant(self, angle):
    if 90 > angle >= 0:
      return  np.take(self.towall, [1,4])
    elif 180 > angle >= 90:
      return  np.take(self.towall, [0,4])
    elif 270 > angle >= 180:
      return  np.take(self.towall, [1,3])
    elif 360 > angle >= 270:
      return  np.take(self.towall, [0,3])

  def vector_destination(self, v, angle):
    sx = abs(v[0])
    sy = abs(v[1])
    direction = self.quadrant(angle)


  def bounce(self, s, d):
    c = 0
    while (s % d)>=d:
      s /= d
      c += 1
    print('s',s,'c',c)

def solution(dimensions, your_position, trainer_position, distance):
  v = vectors(dimensions, your_position, trainer_position, distance)
  v.direction()

solution([3,2], [1,1], [2,1], 4)
