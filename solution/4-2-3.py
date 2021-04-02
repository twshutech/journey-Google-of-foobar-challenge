import math
class vectors:
  def __init__(self, dimensions, your_position, trainer_position, distance):
    self.dimensions = dimensions
    self.your_position = your_position
    self.trainer_position = trainer_position
    self.distance = distance
    self.vectors_list = [(i,j) for j in range(distance + 1) for i in range(distance + 1)]
    self.directions = set([])
    self.d = [[1,1], [-1,1], [1, -1], [-1, -1]]
    self.angle_dict = dict({})
    self.max_distance = [your_position[0]+distance, your_position[1]+distance]

  def get_first_quadrant(self):
      """gets the number of copies that need to be done along the axis
      and gets all the guard and player coords"""
      num_copies_x = math.ceil(self.max_distance[0] / self.dimensions[0])
      num_copies_x = int(num_copies_x)
      num_copies_y = math.ceil(self.max_distance[1] / self.dimensions[1])
      num_copies_y = int(num_copies_y)

      player_exp_x = []
      player_exp_y = []
      guard_exp_x = []
      guard_exp_y = []
      # Loop expands along the x axis
      for i in range(0, num_copies_x + 1, 1):
          temp_player_y_list = []
          temp_guard_y_list = []
          r_x = self.dimensions[0] * i

          if len(player_exp_x) == 0:
              n_p_p_x = self.your_position[0]
          else:
              n_p_p_x = (r_x - player_exp_x[-1][0]) + r_x
          player_exp_x.append([n_p_p_x, self.your_position[1], 1])

          if len(guard_exp_x) == 0:
              n_g_p_x = self.trainer_position[0]
          else:
              n_g_p_x = (r_x - guard_exp_x[-1][0]) + r_x
          guard_exp_x.append([n_g_p_x, self.trainer_position[1], 7])

          # Loop expands along the x axis
          for j in range(1, num_copies_y + 1, 1):
              r_y = self.dimensions[1] * j
              if len(temp_guard_y_list) == 0:
                  n_g_p_y = (r_y - self.trainer_position[1]) + r_y
                  temp_guard_y_list.append(n_g_p_y)
              else:
                  n_g_p_y = (r_y - temp_guard_y_list[-1]) + r_y
                  temp_guard_y_list.append(n_g_p_y)
              guard_exp_y.append([n_g_p_x, n_g_p_y, 7])

              if len(temp_player_y_list) == 0:
                  n_p_p_y = (r_y - self.your_position[1]) + r_y
                  temp_player_y_list.append(n_p_p_y)
              else:
                  n_p_p_y = (r_y - temp_player_y_list[-1]) + r_y
                  temp_player_y_list.append(n_p_p_y)
              player_exp_y.append([n_p_p_x, n_p_p_y, 1])

      return player_exp_x + guard_exp_x + player_exp_y + guard_exp_y

def solution(dimensions, your_position, trainer_position, distance):
  v = vectors(dimensions, your_position, trainer_position, distance)
  print v.get_first_quadrant()

solution([3,2], [1,1], [2,1], 4)
