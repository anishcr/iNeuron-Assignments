# Write a program which will find all such numbers that are divisible by 7
# but are not a multiple of 5, between 2000 and 3200 (both included)
# The numbers such obtained should be printed in a comma separated sequence
# on a single line

import math

def solution1() :
  start   = 2000
  end     = 3200
  i       = start
  isFirst = True
  incr    = 1
  first   = 7
  second  = 5

  while end > i :
    if ((i % first) == 0) and ((i % second) != 0) :
      if isFirst :
        isFirst = False
        incr = first
        print("{}".format(i), end="")
      else:
        print(", {}".format(i), end="")
    i += incr

  print("\n")

def solution2() :
  start   = 2000
  end     = 3200
  first   = 7
  second  = 5

  nearest_upper = first * math.ceil(start/first)
  nearest_lower = first * math.floor(end/first) + 1

  values = [str(i) for i in range(nearest_upper, nearest_lower, first) if i % second != 0]

  print(", ".join(values))

if __name__ == "__main__":
    # execute only if run as a script
    solution1()
    solution2()
