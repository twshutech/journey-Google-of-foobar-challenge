
import math
import colourtheme
bcolors = colourtheme.bcolors()
bcolors.ENDC
powsqrt = lambda n: pow(n, 2)
greater = lambda n: n > 0
# towall = lambda
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
    # go left and go right
    self.wallx = [your_position[0], -1 * (dimensions[0]-your_position[0])]
    # go up and go down
    self.wally = [your_position[1], -1 * (dimensions[1]-your_position[1])]

  def place_location(self):
    self.g[self.y[1]][self.y[0]] = 'M'
    self.g[self.t[1]][self.t[0]] = 'T'

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
        # if deltax == self.diffwidth and deltay == self.diffheight:
        #   print (deltax, deltay),'from',(i, j)
        # Add the vectors within the distance.
        if math.hypot(deltax, deltay) <= self.distance:
          self.possibilities.add((i, j))
    for inex, vector in enumerate(self.possibilities):
      #vector is the values of delta x and delt9a y as array.
      temp = []
      for i, v in enumerate(vector):
        #i == 0 as x else y, negative v as move up or left else down, right.ji
        collisson = self.wallx if i == 0 else self.wally
        wall = self.width if i == 0 else self.height
        print "abs(collisson[1])",abs(collisson[1]),' abs(v)', abs(v),'abs(collisson[0])',abs(collisson[0])
        # if collisson[1] > abs(v) > 0:
        #   print 'v',v
        # else:
        #   print 'self.bounce(v, collisson)',self.bounce(v, collisson)
        destination = v if abs(collisson[1]) >= abs(v) or abs(v) >= abs(collisson[0])  else self.bounce(v, collisson)
        temp.append(destination)
      print vector,'->',temp
      if inex == 10:
        break

  def bounce(self, coord, collision):
    coord = coord + collision[1] if coord > collision[1] else coord + collision[0]
    return coord

def solution(dimensions, your_position, trainer_position, distance):
  possibility = 0
  g = graph(dimensions, your_position, trainer_position, distance)
  # g.place_location()
  g.possible()
  return possibility

solution([3,2], [1,1], [2,1], 4)

# [[1, 0], [1, 2], [1, -2], [3, 2], [3, -2], [-3, 2], [-3, -2]]
# print([0 for i in range(6) if i%2 == 0 ])
