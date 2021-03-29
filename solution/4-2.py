import colourtheme, math, json
import numpy as np
bcolors = colourtheme.bcolors()
# def distances():
dis = lambda i,j,ti,tj:np.hypot(ti-i, tj-j)
field = lambda i,j,ti,tj,m: np.inf if dis(i,j,ti,tj) > m else dis(i,j,ti,tj)
highlight = lambda n: int(n) if n != np.inf else np.inf
length = lambda i, j: abs(i-j)
tonparray = lambda i: np.array(i)
isreverse = lambda n: True if n % 2 != 0 else False
axisdirection = lambda direction, l: [l[2]+l[0], l[1]+l[0]] if direction < 0 else [l[3], l[1]]
unit_vector = lambda vector:vector / np.linalg.norm(vector)
vector_magnitude = lambda v: np.hypot(v[0], v[1])

class vectors:
  def __init__(self, dimensions, your_position, trainer_position, distance):
    self.dimensions = dimensions
    self.test = np.array([[round(field(i,j,trainer_position[1],trainer_position[0],distance)) for j in range(-1*distance,distance,1)] for i in range(-1*distance,distance,1)])
    self.g = np.array([[field(column,row,trainer_position[1],trainer_position[0],distance) for column in range(dimensions[0]+1)] for row in range(dimensions[1]+1)])
    # self.mat = np.array([np.array([np.array(i, j)for j in range(dimensions[0])]) for i in range(dimensions[1])])
    self.y = np.array(your_position)
    self.t = np.array(trainer_position)
    self.distance = distance
    self.width = dimensions[0]+1
    self.height = dimensions[1]+1
    self.possibilities = set([])
    self.angles = set([])
    self.diffwidth = abs(trainer_position[0]-your_position[0])
    self.diffheight = abs(trainer_position[1]-your_position[1])
    #vector
    self.diff = np.array([trainer_position[0]-your_position[0], trainer_position[1]-your_position[1]])
    self.ttowalls = np.array([np.array([0,trainer_position[1]-dimensions[1]]),np.array([0,-1]),np.array([-2,0]),np.array([1,0])])
    self.l = np.array([(1, 0), (1, 2), (1, -2), (3, 2), (3, -2), (-3, 2), (-3, -2)])
    self.trainer = None
    self.you = None

  def get_relay(self, p):
    #The directions from the trainer's position to top, bottom, left, right.
    directions = [tonparray([1, 1]), tonparray([1, -1]), tonparray([1, 1]), tonparray([-1, 1])]
    #From top, bottom, left, right to the trainer's position.
    up = np.array([0, length(p[1], 0)])
    bottom = np.array([0, length(self.dimensions[1], p[1])])
    left = np.array([length(p[0], 0), 0])
    right = np.array([length(self.dimensions[0], p[0]), 0])
    return np.array([up+left, bottom+left, bottom+right, up+right]) * directions

  def rot(self, to):
    if to == 0:
      self.g = np.fliplr(self.g)
    else:
      self.g = np.flipud(self.g)
    # print np.asmatrix(self.g)
  # [[j+i for j in range(-1*distance,distance+1,1)] for i in range(-1*distance,distance+1,1)]

  def possible(self):
    vectors_list = np.array([(i,j) for j in range(self.distance) for i in range(self.distance)])
    print vectors_list
    for i in range(-1*self.distance,self.distance+1,1):
      for j in range(-1*self.distance,self.distance+1,1):
        if math.hypot(i, j) <= self.distance: #Narrow the area for distance that beam could go.
          temp = []
          delta_vector = [i, j]
          # temp = [self.bounce(i,), self.bounce(j, dimension, index)]
          for index, v in enumerate(delta_vector):
            dimension = self.dimensions[index]
            # temp.append(self.bounce(v, dimension, index))
          # if temp[0] == self.diffwidth and temp[1] == self.diffheight:
          #   if math.hypot(delta_vector[0], delta_vector[1]) <= self.distance:
              # print 'temp',temp
              # if list(delta_vector) not in self.l:
                # print 'distance is ',math.hypot(delta_vector[0], delta_vector[1]),'which is within',self.distance
              # s = np.array(delta_vector)+ self.t
              # angle = np.arctan2(s[0],s[1])
              # angle = np.arctan2(i,j)
              # print i,j
              # angle = angle_between_two([i,0],[0,j])
              # if angle not in self.angles:
              #   self.possibilities.add((i, j))
              # print '',bcolors.WARNING,delta_vector,'->',temp,bcolors.ENDC
              # self.angles.add(angle)
              # print self.y+np.array(delta_vector),'\n'
    print bcolors.WARNING,len(self.possibilities),sorted(self.possibilities),bcolors.ENDC
    # print bcolors.OKGREEN,len(self.l),sorted(self.l),bcolors.ENDC
              # self.angles.add((self.y+np.array(delta_vector)))
    # print bcolors.OKGREEN,len(self.angles),self.angles,bcolors.ENDC
              # self.angles.add((self.y+np.array(delta_vector)))
              # self.__init__(self.dimensions, self.y, self.t, self.distance)
    # print self.angles
    # print 'possibilities',len(self.possibilities),'self.diff',5 *self.diff
    # for delta_vector in self.possibilities:

  def bounce(self, v, dimension, index):
    #The coord x or y, return if out of the range
    flag = axisdirection(v, self.you)
    fromwall = flag[index][index] + v
    if fromwall > 0:
      times = fromwall // dimension
      return fromwall if times == 0 else -1 * fromwall
    else:
      return v % 2

  def detect_collision(self, vec):
    v = True
    # print 'v',vec + self.diff
    # For shot self.
    if 0 in self.diff:
      result = np.where(self.diff == 0)
      index = np.take(result, 0)
      # print result,index
    else:
      return True

  def projection(self):
    print 'self.trainer',self.trainer
    for v in self.trainer:
      new_t = self.t + (2*v)
      print self.t,'+',2*v*-1,'->',self.t + self.diff + (2*v),'\n'
      print 'self from your position', new_t - self.y



def solution(dimensions, your_position, trainer_position, distance):
  vector = vectors(dimensions, your_position, trainer_position, distance)
  # dic = vector.__dict__
  # print 'dic',dic
  # print(json.dumps(dic, indent = 4))
  vector.you = vector.get_relay(vector.y)
  vector.trainer = vector.get_relay(vector.t)
  vector.possible()
  # vector.projection()
  # for dot in vector.possibilities:
  #   print dot,'->',dot[0] * dot[1]
  #   vector.test[dot[1]][dot[0]] = dot[0] * dot[1]
  # print ' you \n',vector.you
  # print 'trainer \n', vector.trainer


def angle_between_two(v1, v2):

  unit_vector_1 = unit_vector(v1)
  unit_vector_2 = unit_vector(v2)
  dot_product = np.dot(unit_vector_1, unit_vector_2)
  angle = np.arccos(dot_product)

  print 'v1',v1,'v2',v2
  print 'unit_vector_1',unit_vector_1,'unit_vector_2',unit_vector_2,'angle',angle
  return angle

# angle_between_two()
solution([3,2], [1,1], [2,1], 4)
# solution([300,275], [150,150], [185,100], 500)