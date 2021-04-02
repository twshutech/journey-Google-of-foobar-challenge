import matplotlib as mpl
mpl.use('MacOSX')
import numpy as np
import matplotlib.pyplot as plt
# import  sys.settrace as systra

class vectors:
  def __init__(self):
    self.v1 = np.array([[1,1], [-2,2], [4,-7]])
    self.origin = np.array([[0, 0, 0],[0, 0, 0]])


def draw(dimensions, your_position, trainer_position, distance):
  v = vectors()
  V = v.v1
  origin = v.origin

  # print( origin,'\n',V)
  plt.quiver(origin[0], origin[1], V[:,0], V[:,1], color=['r','b','g'], scale=21)
  plt.show()

draw([3,2], [1,1], [2,1], 4)