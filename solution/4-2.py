import colourtheme, math, numpy, json
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
        if math.hypot(i, j) <= self.distance:
          temp = []
          delta_vector = [i, j]
          for index, v in enumerate(delta_vector):
            dimension = self.dimensions[index] + 1
            temp.append(self.bounce(v, dimension))
          self.possibilities.add((i, j))
          # print 'temp',bcolors.WARNING,delta_vector,'->',temp,bcolors.ENDC,'\n'
          if temp[0] == self.diffwidth and temp[1] == self.diffheight:
            # print 'same vector',bcolors.WARNING,delta_vector,'->',temp,bcolors.ENDC,'\n'
            if math.hypot(delta_vector[0], delta_vector[1]) <= self.distance:
              # if list(delta_vector) not in self.l:
                # print 'distance is ',math.hypot(delta_vector[0], delta_vector[1]),'which is within',self.distance
              print '',bcolors.WARNING,delta_vector,'->',temp,bcolors.ENDC,'\n'
    print 'possibilities',len(self.possibilities)
    # for delta_vector in self.possibilities:

  def bounce(self, v, dimension):
    if v >= dimension:
      return (v >> dimension) % 2
    else:
      return v % 2

def distances():


def solution(dimensions, your_position, trainer_position, distance):
  vector = vectors(dimensions, your_position, trainer_position, distance)
  # dic = vector.__dict__
  # print 'dic',dic
  # print(json.dumps(dic, indent = 4))
  vector.possible()

solution([3,2], [1,1], [2,1], 4)
# solution([300,275], [150,150], [185,100], 500)