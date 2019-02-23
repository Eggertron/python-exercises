"""
How many letter of the Alphabet?

So I wanted to write a function to find out how many letters
of the alphabet would appear in a given text.

I've learned that Python has made some optimizations to string
manipulations to the point where creating functions to match
C-style programming is not needed.
"""

import time
 
def check_alphabets_v1(words):
  """
  This was my first attempt. Comming from a C-programming
  background, my approach was to create as much from
  scratch as possible.
  """
  alphabets = [0] * 26
  a = ord('a')
  z = ord('z')
  for x in words.lower():
    char = ord(x)
    if a <= char and char <= z:
      alphabets[char - a] = 1
  results = 0
  for x in alphabets:
    results += x
  return results
 
def check_alphabets_v2(words):
  """
  This was my optimization of the first approach.
  """
  alphabets = [True] * 26
  a = ord('a')
  z = ord('z')
  results = 0
  for x in words.lower():
    char = ord(x)
    if a <= char and char <= z:
      pos = char - a
      if alphabets[pos]:
        alphabets[pos] = False
        results += 1
        if results == 26:
          return results
  return results
   
def check_alphabets_v3(words):
  """
  This is an approach that utilizes python for
  what it is. The stats on this seems to look
  pretty good.
  """
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  results = 0
  for letter in alphabet:
    if letter not in words:
      break
    results += 1
  return results

def debug(text, func):
  start_time = time.time()
  characters = func(text)
  end_time = time.time()
  print("========= Start Test ===============")
  print("text: {0}".format(text))
  print("function: {0}".format(func))
  print("contains {0} letters of the alphabet".format(characters))
  print("time: {0}".format(end_time - start_time))
  print("========= End   Test ===============\n\n")
          
sample = "Hello World"
 
debug(sample, check_alphabets_v1)
debug(sample, check_alphabets_v2)
 
sample = "the quick brown fox jumps over the lazy dog" * 100
debug(sample, check_alphabets_v1)
debug(sample, check_alphabets_v2)
debug(sample, check_alphabets_v3)
