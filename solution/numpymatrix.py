# import sys, matplotlib, math
# matplotlib.use('Agg')

# import matplotlib.pyplot as plt
# import numpy as np

import colourtheme
bcolors = colourtheme.bcolors()
vector_length = lambda vx, vy, d: True if math.hypot(vx, vy) <= d else False

def initmatrix(x, y):
  # xpoints = np.array([[0 for column in range(x)] for row in range(y)])
  # ypoints = np.array([0 for i in range(y)])
  arr = np.full((y,x), 0, dtype=int)
  # a = [[0 for column in range(x)] for row in range(y)]
  matrix = np.asmatrix(arr)
  # print arr
  # print matrix
  # plt.plot(xpoints, ypoints)
  # plt.show()
  # #Two  lines to make our compiler able to draw:
  # plt.savefig(sys.stdout.buffer)
  # sys.stdout.flush()
collision = [[1, -2], [1,-1]]
dimension = [4, 3]

def bounce(v, index):
  if v > dimension[index]:
    print v,'>> ',dimension[index],' % 2',(v >> dimension[index]) % 2
  else:
    print v,'% 2',v % 2

  if index == 0:
    correction = collision[0][0] if v < 0 else collision[0][1]
  else:
    correction = collision[1][0] if v < 0 else collision[1][1]
  if abs(v) > abs(correction):
    v+=correction

  remaining = v % dimension[index]
  if v >> dimension[index] % 2 != 0:
    remaining *= -1
  print v,'remaining',remaining
  # print bcolors.OKGREEN,v,'%',dimension[index],'=',-1 * (v % dimension[index]),bcolors.ENDC

  return v

# for vector in [[10,-7], [10,7], [-3,6], [1,-9], [1,0], [0,0]]:
for vector in [[1, 0], [1, 2], [1, -2]]:
  temp = []
  for index, v in enumerate(vector):
    temp.append(bounce(v, index))
  print bcolors.WARNING,vector,'->',temp,bcolors.ENDC,'\n'

# initmatrix(3, 2)
# Three lines to make our compiler able to draw:

# xpoints = np.array([1, 8])
# ypoints = np.array([3, 10])

# plt.plot(xpoints, ypoints, 'o')
# plt.show()

# #Two  lines to make our compiler able to draw:
# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()

