import time
 
def is_palindrome(word):
  end = len(word) - 1
  for x in range(int((end + 1) / 2)):
    if word[x] != word[end - x]:
      return False
  return True
  
def debug(t1, t2):
  print("{0} is palindrome? {1}".format(t1, t2))
   
sample = "edgar"
debug(sample, is_palindrome(sample))
 
sample = "racecar"
debug(sample, is_palindrome(sample))
 
sample = "lvllvl"
debug(sample, is_palindrome(sample))
 
sample = "hello"
debug(sample, is_palindrome(sample))
