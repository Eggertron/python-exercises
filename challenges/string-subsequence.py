######################################
# String Subsequence
# Given 2 strings of characters,
# find the longest subsequnce that
# exists in both strings
######################################

import time

def linear_index_search(str1, str2):
  result = ""
  # The shorter string will be traversed
  # The longer string will be chopped after every matching letter
  if len(str1) > len(str2):
    long_str = str1
    short_str = str2
  else:
    long_str = str2
    short_str = str1
  # start from the begining of the short string
  counter = 0
  for x in short_str:
    head = 1
    for y in long_str:
      counter += 1
      if x == y:
        result += x
	long_str = long_str[head:]
	# if the last matching character is the end of long string
	# then we are done
	if len(long_str) == 0:
	  return result, counter
	break
      else:
        head += 1
  return result, counter


def debug(str1, str2, func):
  start_time = time.time()
  result, count = func(str1, str2)
  end_time = time.time()
  print("========= Start Test ===============")
  print("string 1: {0}".format(str1))
  print("string 2: {0}".format(str2))
  print("function: {0}".format(func))
  print("result: {0}".format(result))
  print("loops: {0}".format(count))
  print("time: {0}".format(end_time - start_time))
  print("========= End   Test ===============\n\n")

string1 = "abcdefghijklmnopqrstuvwxyz"
string2 = "adgedzeeeeeeeeeeeeeeeeeee"
debug(string1, string2, linear_index_search)


def two_d_array(str1, str2):
  return ""
