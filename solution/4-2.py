
class graph:
  def __init__(self, dimensions, your_position, trainer_position, distance):
    self.g = [['x' for column in range(dimensions[0]+1)] for row in range(dimensions[1]+1)]
    self.y = your_position
    self.t = trainer_position

  def place_location(self):
    self.g[self.y[1]][self.y[0]] = 'O'
    self.g[self.t[1]][self.t[0]] = 'O'
    for r in self.g:
      print r

def solution(dimensions, your_position, trainer_position, distance):
  possibility = 0
  g = graph(dimensions, your_position, trainer_position, distance)
  g.place_location()
  return possibility

solution([3,2], [1,1], [2,1], 4)


# print(['x' for i in range(5)])