import numpy as np
import colourtheme, math
from operator import itemgetter, attrgetter

class c:
  def __init__(self):
    self.HEADER = '\033[95m'
    self.OKBLUE = '\033[94m'
    self.OKGREEN = '\033[92m'
    self.WARNING = '\033[93m'
    self.FAIL = '\033[91m'
    self.ENDC = '\033[0m'
c = c()
unit_vector = lambda vector:vector / np.linalg.norm(vector)
vector_magnitude = lambda m: math.hypot(m[0], m[1])
vector_angle = lambda m: np.arctan2(m[1], m[0]) * 180 / np.pi
# scalar = lambda
isntfar = lambda m, max_distance: True if vector_magnitude(m) <= max_distance else False
# get vectors from your location to top, bottom or left, right.
collisions = lambda i, l: [l[2], l[3]] if i == 0 else [l[0], l[1]]
# get scalar with direction for the vector.
compare = lambda axis, l: l[0] if axis < 0 else l[1]
# remain.
remaining = lambda n, b, t: pow(b, t) + n
# times of bouncing.
bouncing_times = lambda n, b: math.floor(math.log(abs(n),b))
# prefix.
prefix = lambda n: 1 if n>=0 else -1
# remain distance and direction.
actual_vector = lambda v, i, d: v if abs(v+i) < d else -1 * (abs(v+i) % d)
# check if vector bounce back.
will_bounce = lambda v, d, i: v if abs(v) <= abs(i) else actual_vector(v, i, d)
# abs sum
abs_sum =   lambda arr: sum()
# vector prefix
ceiling_prefix = lambda your_scalar, vector_scalar, ceiling: pow(-1, math.ceil(your_scalar/ceiling)) if abs(your_scalar) > abs(ceiling) else your_scalar


class vectors:
  def __init__(self, dimensions, your_position, trainer_position, distance):
    self.dimensions = dimensions
    self.your_position = your_position
    self.trainer_position = trainer_position
    self.distance = distance
    self.vectors_list = [(i,j) for j in range(distance + 1) for i in range(distance + 1)]
    self.directions = set([])
    self.d = [[1,1], [-1,1], [1, -1], [-1, -1]]
    self.towall = []
    self.angle_dict = dict({})

  def quadrant(self, angle):
    if 90 >= angle >= 0:
      return  np.take(self.towall, [3,1])
    elif 180 >= angle > 90:
      return  np.take(self.towall, [2,0])
    elif -90 >= angle > -180:
      return  np.take(self.towall, [2,0])
    elif -180 >= angle > 0:
      return  np.take(self.towall, [3,1])

  def direction(self):
    self.getrelation(self.your_position)
    angles = set([])
    temp = set([])
    for delta in self.vectors_list:
      for trans in self.d:
        dot = [delta[0]*trans[1], delta[1] * trans[1]]
        # print isntfar(dot, self.distance)
        if isntfar(dot, self.distance):
          angle = vector_angle(dot)

          self.make_angle_list(angle, dot)
          if angle not in angles:
            # if np.array_equal(self.your_position + dot, self.trainer_position):
            #   print dot,self.your_position + dot == self.trainer_position
            # print  self.your_position + dot,dot,self.your_position + dot == self.trainer_position
            self.collect(dot)
            angles.add(angle)
          # else:

  def make_angle_list(self, angle, dot):
    if dot == [0,0]:
      return
    angle = str(angle)
    if angle in self.angle_dict.keys():
      if dot not in self.angle_dict[angle]:
        self.angle_dict[angle].append(dot)
    else:
      self.angle_dict.update({angle: [dot]})

  def getrelation(self, dot):
    # vectors from dot location to top, bottom,  left, right.
    # vectors left, top will be positive, negtive for right and bottom.
    self.towall = [dot[1], -1 * self.dimensions[1]+dot[1], dot[0], -1 * self.dimensions[0]+dot[0]]

  def collect(self, v):
    # print 'vector',v,'towall dis',self.towall
    tempv = v
    i = compare(v[0], collisions(0, self.towall))
    j = compare(v[1], collisions(1, self.towall))
    # if v[0]
      # print 'Beam x', c.OKBLUE, v, c.ENDC, 'will' , c.OKGREEN,'not'if v[0]+i >= 0 else '', c.ENDC, 'bounce back'
    #   tempv[0] = actual_vector(v[0]+i, self.dimensions[0])
    # if v[1]+j < 0 and v [1] != 0:
      # print 'Beam y', c.OKBLUE, v, c.ENDC,'will' , c.OKGREEN,'not'if v[1]+j >= 0 else '', c.ENDC, 'bounce back'
      # tempv[1] = actual_vector(v[1]+j, self.dimensions[1])
    # i = v[0] if v < self.towall[3] and v < abs(self.towall[2]) else self.bounce(v, stand(0, self.towall))
    # j = v[1] if v < self.towall[0] and v < abs(self.towall[1]) else self.bounce(v, stand(1, self.towall))
    # tempv[0] = self.bounce(v[0], i, self.dimensions[0])
    # tempv[1] = self.bounce(v[1], j,  self.dimensions[1])

  # def bounce(self, scalar, ceiling):

  #   # # print value, wall
  #   # prefix = 1 if value >= 0 else -1
  #   # return will_bounce(value, axis, wall)

  # # def b(self, s, d, you):
  # #   if


  def bounce(self, s, d):
    d = abs(d)
    s = abs(s)
    c = 1 if s / d == 1 else 0
    while (s % d)>=d:
      s =  s % d
      c += 1
    print('s',s,'c',c)

def solution(dimensions, your_position, trainer_position, distance):
  v = vectors(dimensions, your_position, trainer_position, distance)
  v.direction()
  for an,dot in v.angle_dict.items():
    # print sorted(dot, key=itemgetter(0))
    arr = [vector_magnitude(m) for m in dot]
    dot = dot[dot.index(min(dot))]
    # x_plane = v.your_position[0] + dot[0] if v.your_position[0] + dot[0]
    # if v.your_position[0] + dot[0] > self.dimensions[0] or

  v.bounce(3, -2)

solution([3,2], [1,1], [2,1], 4)
