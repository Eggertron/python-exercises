'''
'''

import time

def equilibrium(array):
  array_sum = sum(array)
  left_sum = 0
  index = 0
  for x in array:
    array_sum -= x
    if array_sum == left_sum:
      return index
    left_sum += x
    index += 1
  return None

def debug(array):
  print("==================")
  print("array:")
  print(array)
  print("equilibrium index is: {0}".format(equilibrium(array)))
  print("==================")

debug([1, 2, 3, 4, 5, 6, 7])
debug([3, 6, 1, 2, 9, 6])
debug([-7, 1, 5, 2, -4, 3, 0])
debug([1, 1, 1, 2, 3])
