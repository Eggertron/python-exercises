import time
 
def check_alphabets_v1(words):
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
   
def debug(text, func):
  start_time = time.time()
  characters = func(sample)
  end_time = time.time()
  print("contains {0} letters of the alphabet".format(characters))
  print("time: {0}".format(end_time - start_time))
          
sample = "Hello World"
 
debug(sample, check_alphabets_v1)
debug(sample, check_alphabets_v2)
 
sample = "the quick brown fox jumps over the lazy dog"
debug(sample, check_alphabets_v1)
debug(sample, check_alphabets_v2)
