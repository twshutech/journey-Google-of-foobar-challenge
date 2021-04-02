from math import sqrt, atan2, ceil, hypot, fsum
from copy import deepcopy

class vectors:
  def __init__(self, dimensions, your_position, trainer_position, distance):
    self.dimensions_x = dimensions[0]
    self.dimensions_y = dimensions[1]
    self.your_position_x = your_position[0]
    self.your_position_y = your_position[1]
    self.trainer_position_x = trainer_position[0]
    self.trainer_position_y = trainer_position[1]
    self.max_distance = distance
    self.max_x = self.your_position_x + distance + 1
    self.max_y = self.your_position_y + distance + 1

  def get_dist(self, point_x, point_y):
    return hypot(point_x - self.your_position_x, point_y - self.your_position_y)

  def get_angle(self, point_x, point_y):
    angle = atan2(point_y - self.your_position_y, point_x - self.your_position_x)
    return angle

  def get_first_quadrant(self):

    num_copies_x = int(ceil(self.max_x / self.dimensions_x))
    num_copies_y = int(ceil(self.max_y / self.dimensions_y))

    player_exp_x = []
    player_exp_y = []
    trainer_position_exp_x = []
    trainer_position_exp_y = []
    for i in range(0, num_copies_x + 1, 1):
      temp_player_y_list = []
      temp_trainer_position_y_list = []
      r_x = self.dimensions_x * i

      if len(player_exp_x) == 0:
        n_p_p_x = self.your_position_x
      else:
        n_p_p_x = (r_x - player_exp_x[-1][0]) + r_x
      player_exp_x.append([n_p_p_x, self.your_position_y, 1])

      if len(trainer_position_exp_x) == 0:
        n_g_p_x = self.trainer_position_x
      else:
        n_g_p_x = (r_x - trainer_position_exp_x[-1][0]) + r_x
      trainer_position_exp_x.append([n_g_p_x, self.trainer_position_y, 7])

      for j in range(1, num_copies_y + 1, 1):
        r_y = self.dimensions_y * j
        if len(temp_trainer_position_y_list) == 0:
          n_g_p_y = (r_y - self.trainer_position_y) + r_y
          temp_trainer_position_y_list.append(n_g_p_y)
        else:
          n_g_p_y = (r_y - temp_trainer_position_y_list[-1]) + r_y
          temp_trainer_position_y_list.append(n_g_p_y)
        trainer_position_exp_y.append([n_g_p_x, n_g_p_y, 7])

        if len(temp_player_y_list) == 0:
          n_p_p_y = (r_y - self.your_position_y) + r_y
          temp_player_y_list.append(n_p_p_y)
        else:
          n_p_p_y = (r_y - temp_player_y_list[-1]) + r_y
          temp_player_y_list.append(n_p_p_y)
        player_exp_y.append([n_p_p_x, n_p_p_y, 1])

    return player_exp_x + trainer_position_exp_x + player_exp_y + trainer_position_exp_y

  def genQ(self, qt, matrix):
    q = deepcopy(matrix)
    qf = []
    for j in range(len(q)):
      list = [q[j][i] * qt[i] for i in range(2)]
      dist = self.get_dist(list[0], list[1])

      if dist <= self.max_distance:
        list.append(matrix[j][2])
        qf.append(list)
    return qf

  def other_quadrants(self, matrix):
    q2f = self.genQ([-1, 1], matrix)

    q3f = self.genQ([-1, -1], matrix)

    q4f = self.genQ([1, -1], matrix)
    return q2f, q3f, q4f

  def filter_target_hit(self, matrix):
    """Uses a dict with angles as key
    Filters by range and by distance of the same angle (closer always
    wins)"""
    target = {}
    for i in range(len(matrix)):
      dist = self.get_dist(matrix[i][0], matrix[i][1])
      angle = self.get_angle(matrix[i][0], matrix[i][1])
      test_a = self.max_distance >= dist > 0
      test_b = angle not in target
      test_c = angle in target and dist < target[angle][1]
      if test_a and (test_b or test_c):
        target[angle] = [matrix[i], dist]

    return target

def return_count(dict):
  count = 0
  for key in dict:
    if dict[key][0][2] == 7:
      count += 1
  return count

def solution(dimensions, your_position, trainer_position_position, distance):
    p = vectors(dimensions, your_position, trainer_position_position, distance)
    first_quadrant = p.get_first_quadrant()

    q2, q3, q4 = p.other_quadrants(first_quadrant)
    final_list = first_quadrant + q2 + q3 + q4

    final_dict = p.filter_target_hit(final_list)

    count = return_count(final_dict)
    return count

print solution([3,2], [1,1], [2,1], 4)