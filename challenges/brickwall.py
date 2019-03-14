'''
Interview Question from FireEye

Create an algorithm to determine if you can make a
brick wall of length n units, given that small bricks
are 1 unit and large bricks are 5 units.
'''

import time

def makes_brick_wall(small, large, goal):
  large_remainders = min( goal // large, large)
  small_remainders = goal - ( large_remainders * 5 )
  return small_remainders <= small


def debug(small, large, goal):
  print("=============================")
  print("small bricks: {0}".format(small))
  print("large bricks: {0}".format(large))
  print("wall size goal: {0}".format(goal))
  print("Can we build the wall? {0}".format(makes_brick_wall(small, large, goal)))
  print("=============================")

debug(2, 4, 13)
debug(3, 4, 13)
debug(8, 1, 13)
debug(1, 2, 13)
