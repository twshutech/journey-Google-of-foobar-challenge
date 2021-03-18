
import math
import colourtheme
bcolors = colourtheme.bcolors()
bcolors.ENDC
powsqrt = lambda n: pow(n, 2)

class triangle():
  def __init__(self, dimensions, your_position, trainer_position, distance):
    self.y = your_position
    self.t = trainer_position
    self.width = dimensions[0]+1
    self.height = dimensions[1]+1
    self.diffwidth = abs(trainer_position[0]-your_position[0])
    self.diffheight = abs(trainer_position[1]-your_position[1])

class graph:
  def __init__(self, dimensions, your_position, trainer_position, distance):
    self.g = [['_' for column in range(dimensions[0]+1)] for row in range(dimensions[1]+1)]
    self.y = your_position
    self.t = trainer_position
    self.distance = distance
    self.width = dimensions[0]+1
    self.height = dimensions[1]+1
    self.possibilities = set([])
    self.ans = set([])
    self.diffwidth = abs(trainer_position[0]-your_position[0])
    self.diffheight = abs(trainer_position[1]-your_position[1])

  def place_location(self):
    self.g[self.y[1]][self.y[0]] = 'M'
    self.g[self.t[1]][self.t[0]] = 'T'
    for i in self.g:
      print ' '.join(i)

  def rangex(self, delta):
    if self.y[0]+delta > self.width:
      return delta+(self.y[0]-self.width)
    elif self.y[0]+delta < 0:
      return delta+(self.width-self.y[0])
    else:
      return delta

  def rangey(self, delta):
    if self.y[1]+delta > self.height:
      return delta+(self.y[1]-self.height)
    elif self.y[1]+delta < 0:
      return delta+(self.height-self.y[1])
    else:
      return delta

  def possible(self):
    for i in range(-1*self.distance,self.distance+1,1):
      for j in range(-1*self.distance,self.distance+1,1):
        deltax = self.rangex(i)
        deltay = self.rangey(j)
        # print (i, j)
        if deltax == self.diffwidth and deltay == self.diffheight:
          print (deltax, deltay),'from',(i, j)
        if math.sqrt(powsqrt(deltax)+powsqrt(deltay)) <= self.distance:
          self.possibilities.add((i, j))
    # for p in sorted(self.possibilities):
    #   if self.rangex(self.y[0]+p[0]) == self.t[0] and self.rangey(self.y[1]+p[1]) == self.t[1]:
    #     print self.rangex(p[0]), self.rangey(p[1]), 'from', p
        # if p in [(1, 0), (1, 2), (1, -2), (3, 2), (3, -2), (-3, 2), (-3, -2)]:
        # print bcolors.OKGREEN,p ,bcolors.ENDC
      # else:
      #   print p
    #       x =
    #       y =
    #       if x == 2 and y == 1:
    #         print '21',x,y,deltax,deltay,self.width,self.height

    #       self.possibilities.add((x, y))
    # for coord in sorted(self.possibilities):
    #   if math.sqrt(powsqrt(coord[0])+ powsqrt(coord[1])) <= self.distance:
    #     print coord

def solution(dimensions, your_position, trainer_position, distance):
  possibility = 0
  g = graph(dimensions, your_position, trainer_position, distance)
  g.place_location()
  g.possible()
  return possibility

solution([3,2], [1,1], [2,1], 4)

# [[1, 0], [1, 2], [1, -2], [3, 2], [3, -2], [-3, 2], [-3, -2]]
# print([0 for i in range(6) if i%2 == 0 ])
