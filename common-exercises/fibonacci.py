import time
 
def fib(x):
  if x < 2:
    return x
  return fib(x - 2) + fib(x - 1)
 
def debug(x):
  start = time.time()
  result = fib(x)
  end = time.time()
  print("fib({0}) = {1}".format(x, result))
  print("time: {0}".format(end - start))
 
debug(0)  
debug(1)
debug(2)
debug(3)
debug(4)
debug(5)
debug(6)
debug(7)
