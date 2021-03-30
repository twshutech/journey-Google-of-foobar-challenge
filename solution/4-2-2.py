import numpy as np
import colourtheme, math
# c = colourtheme.bcolors()
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
vector_magnitude = lambda m: np.hypot(m[0], m[1])
vector_angle = lambda m: np.arctan2(m[0], m[1]) * 180 / np.pi
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
    self.angle_dict = dict({})

  def quadrant(self, angle, d):
    if 90 >= angle >=0:
      print d,'is at first quadrant 1'
    elif 180 >= angle >90:
      print d,'is at first quadrant 2'
    elif 270 >= angle >180:
      print d,'is at first quadrant 3'
    elif 0 > angle >270:
      print d,'is at first quadrant 4'


  def direction(self):
    self.getrelation(self.your_position)
    print 'towall',self.towall
    angles = set([])
    temp = set([])
    for delta in self.vectors_list:
      for trans in self.d:
        dot = delta * trans
        # print isntfar(dot, self.distance)
        if isntfar(dot, self.distance):
          angle = vector_angle(dot)

          # self.make_angle_list(angle, dot)
          if angle not in angles:
            # if np.array_equal(self.your_position + dot, self.trainer_position):
            #   print dot,self.your_position + dot == self.trainer_position
            # print  self.your_position + dot,dot,self.your_position + dot == self.trainer_position
            self.quadrant(angle, self.your_position+dot)
            self.collect(dot)
            angles.add(angle)
          # else:

  def make_angle_list(self, angle, dot):
    angle = str(angle)
    if angle in self.angle_dict.keys():
      self.angle_dict[angle].append(dot)
    else:
      self.angle_dict.update({angle: [dot]})

  def getrelation(self, dot):
    # vectors from dot location to top, bottom,  left, right.
    # vectors left, top will be positive, negtive for right and bottom.
    self.towall = np.array([dot[1], -1 * self.dimensions[1]+dot[1], dot[0], -1 * self.dimensions[0]+dot[0]])

  def collect(self, v):
    # print 'vector',v,'towall dis',self.towall
    tempv = np.array(v)
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
    tempv[0] = self.bounce(v[0], i, self.dimensions[0])
    tempv[1] = self.bounce(v[1], j,  self.dimensions[1])
    print c.OKGREEN,v,c.ENDC,'->',c.OKBLUE,tempv,c.ENDC

  def bounce(self, value, wall, axis):
    # print value, wall
    prefix = 1 if value >= 0 else -1
    return will_bounce(value, axis, wall)

  # def b(self, s, d, you):
  #   if



def solution(dimensions, your_position, trainer_position, distance):
  v = vectors(dimensions, your_position, trainer_position, distance)
  v.direction()
  # print v.angle_dict
solution([3,2], [1,1], [2,1], 4)
