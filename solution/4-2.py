import colourtheme, math, json
import numpy as np
bcolors = colourtheme.bcolors()
# def distances():
dis = lambda i,j,ti,tj:math.hypot(ti-i, tj-j)
field = lambda i,j,ti,tj,m: np.inf if dis(i,j,ti,tj) > m else dis(i,j,ti,tj)
highlight = lambda n: int(n) if n != np.inf else np.inf

class vectors:
  def __init__(self, dimensions, your_position, trainer_position, distance):
    self.dimensions = dimensions
    self.test = np.array([[round(field(i,j,trainer_position[1],trainer_position[0],distance)) for j in range(-1*distance,distance+1,1)] for i in range(-1*distance,distance+1,1)])
    self.g = np.array([[field(column,row,trainer_position[1],trainer_position[0],distance) for column in range(dimensions[0]+1)] for row in range(dimensions[1]+1)])
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
    self.l = np.array([[1, 0], [1, 2], [1, -2], [3, 2], [3, -2], [-3, 2], [-3, -2]])

  def rot(self, to):
    if to == 0:
      self.g = np.fliplr(self.g)
    else:
      self.g = np.flipud(self.g)
    print np.asmatrix(self.g)
# [[j+i for j in range(-1*distance,distance+1,1)] for i in range(-1*distance,distance+1,1)]
  def possible(self):
    for i in range(-1*self.distance,self.distance+1,1):
      for j in range(-1*self.distance,self.distance+1,1):
        if math.hypot(i, j) <= self.distance:
          temp = []
          delta_vector = [i, j]
          for index, v in enumerate(delta_vector):
            dimension = self.dimensions[index] + 1
            temp.append(self.bounce(v, dimension, index))
          if temp[0] == self.diffwidth and temp[1] == self.diffheight:
            if math.hypot(delta_vector[0], delta_vector[1]) <= self.distance:
              # if list(delta_vector) not in self.l:
                # print 'distance is ',math.hypot(delta_vector[0], delta_vector[1]),'which is within',self.distance
              # print '',bcolors.WARNING,delta_vector,'->',temp,bcolors.ENDC
              # s = np.array(delta_vector)+ self.t
              # angle = np.arctan2(s[0],s[1])
              angle = np.arctan2(i,j)
              if angle not in self.angles:
                self.possibilities.add((i, j))
              self.angles.add(angle)
              # print self.y+np.array(delta_vector),'\n'
    print bcolors.WARNING,len(self.possibilities),self.possibilities,bcolors.ENDC
    print
    print bcolors.OKGREEN,len(self.angles),self.angles,bcolors.ENDC
              # self.angles.add((self.y+np.array(delta_vector)))
              # self.__init__(self.dimensions, self.y, self.t, self.distance)
    # print self.angles
    # print 'possibilities',len(self.possibilities),'self.diff',5 *self.diff
    # for delta_vector in self.possibilities:

  def bounce(self, v, dimension, index):
    if v >= dimension:
  #     print v, '->', v >> dimension
      return (v >> dimension) % 2
    else:
      return v % 2

def solution(dimensions, your_position, trainer_position, distance):
  vector = vectors(dimensions, your_position, trainer_position, distance)
  # dic = vector.__dict__
  # print 'dic',dic
  # print(json.dumps(dic, indent = 4))
  vector.possible()
  # for dot in vector.possibilities:
  #   print dot,'->',dot[0] * dot[1]
  #   vector.test[dot[1]][dot[0]] = dot[0] * dot[1]
  print vector.test

solution([3,2], [1,1], [2,1], 4)
# solution([300,275], [150,150], [185,100], 500)