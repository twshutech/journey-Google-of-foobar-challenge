import matplotlib.pyplot as plt
import numpy as np

class vectors:
  def __init__(self):
    self.v1 = np.array([[1,1], [-2,2], [4,-7]])
    self.origin = np.array([[0, 0, 0],[0, 0, 0]])


def draw(dimensions, your_position, trainer_position, distance):
  x = np.linspace(-10.0, 10.0, 10)
  y = np.linspace(-10.0, 10.0, 10)
  X, Y = np.meshgrid(x,y)
  F = X**2 + Y**2 - 0.6
  # ax = plt.axes()
  # ax.arrow(0, 0, 0.5, 0.5, head_width=0.05, head_length=0.1, fc='k', ec='k')
  plt.contour(X,Y,F,[0])
  plt.show()

draw([3,2], [1,1], [2,1], 4)