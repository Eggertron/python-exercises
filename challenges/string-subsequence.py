######################################
# String Subsequence
# Given 2 strings of characters,
# find the longest subsequnce that
# exists in both strings
######################################

import time

def linear_index_search(str1, str2):
  result = ""
  if len(str1) > len(str2):
    long_str = str1
    short_str = str2
  else:
    long_str = str2
    short_str = str1
  for x in short_str:
    head = 0
    for y in long_str:
      if x == y:
        result += x
	long_str = long_str[head:]
	break
      else:
        head += 1
  return result


def debug(str1, str2, func):
  start_time = time.time()
  result = func(str1, str2)
  end_time = time.time()
  print("========= Start Test ===============")
  print("string 1: {0}".format(str1))
  print("string 2: {0}".format(str2))
  print("function: {0}".format(func))
  print("result: {0}".format(result))
  print("time: {0}".format(end_time - start_time))
  print("========= End   Test ===============\n\n")

string1 = "abcdefghijklmnopqrstuvwxyz"
string2 = "adgedz"
debug(string1, string2, linear_index_search)


def two_d_array(str1, str2):
  return ""
