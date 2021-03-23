import colourtheme, math
bcolors = colourtheme.bcolors()

class vectors:
  def __init__(self, dimensions, your_position, trainer_position, distance):
    self.dimensions = dimensions
    self.g = [['_' for column in range(dimensions[0]+1)] for row in range(dimensions[1]+1)]
    self.y = your_position
    self.t = trainer_position
    self.distance = distance
    self.width = dimensions[0]+1
    self.height = dimensions[1]+1
    self.possibilities = set([])
    self.diffwidth = abs(trainer_position[0]-your_position[0])
    self.diffheight = abs(trainer_position[1]-your_position[1])
    self.l = [[1, 0], [1, 2], [1, -2], [3, 2], [3, -2], [-3, 2], [-3, -2]]

  def possible(self):
    for i in range(-1*self.distance,self.distance+1,1):
      for j in range(-1*self.distance,self.distance+1,1):
        # deltax = self.rangex(i)
        # deltay = self.rangey(j)
        # if math.hypot(deltax, deltay) <= self.distance:
        self.possibilities.add((i, j))
    # print 'possibilities',self.possibilities
    for delta_vector in self.possibilities:
      temp = []
      for index, v in enumerate(delta_vector):
        dimension = self.dimensions[index] + 1
        temp.append(self.bounce(v, dimension))
      if temp[0] == self.diffwidth and temp[1] == self.diffheight:
        if math.hypot(delta_vector[0], delta_vector[1]) <= self.distance:
          if list(delta_vector) not in self.l:
            # print 'distance is ',math.hypot(delta_vector[0], delta_vector[1]),'which is within',self.distance
            print bcolors.WARNING,delta_vector,'->',temp,bcolors.ENDC,'\n'

  def bounce(self, v, dimension):
    if v >= dimension:
      # print v,'>> ',dimension,' % 2',(v >> dimension) % 2
      return (v >> dimension) % 2
    else:
      # print v,'% 2',v % 2
      return v % 2

# for vector in [[10,-7], [10,7], [-3,6], [1,-9], [1,0], [0,0]]:
def solution(dimensions, your_position, trainer_position, distance):
  l = [[1, 0], [1, 2], [1, -2], [3, 2], [3, -2], [-3, 2], [-3, -2]]
  print l
  vector = vectors(dimensions, your_position, trainer_position, distance)
  vector.possible()

solution([3,2], [1,1], [2,1], 4)