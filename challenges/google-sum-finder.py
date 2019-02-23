"""
So I came upon this Google Video and saw an exercise
https://www.youtube.com/watch?v=XKu_SEDAykw

I thought this technique would be nice to have in my
back pocket for the future.

Challenge:
Given a sorted array of integers, you must find two 
numbers that sum up to the given target value.

O(n) 
"""

import time

def find_sums(array, value):
  head = 0
  tail = len(array) - 1
  while True:
    summed = array[head] + array[tail]
    if summed > value:
      tail -= 1
    elif summed < value:
      head += 1
    elif summed == value:
      return (array[head], array[tail])
    elif head >= tail:
      return (None, None)
	  
def debug(array, value):
  print("========== Start ==========")
  start_time = time.time()
  (head, tail) = find_sums(array, value)
  end_time = time.time()
  print("target: {0}".format(value))
  print("found in array: {0} and {1}".format(head, tail))
  print("time: {0}".format(end_time - start_time))
  print("==========  End  ==========\n\n")
  
# start here

array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 8

debug(array, target)