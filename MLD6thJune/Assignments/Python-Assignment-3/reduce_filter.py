# 1.1 Write a Python Program to implement your own myreduce() function which works exactly
#     like Python's built-in function reduce()
#
# 1.2 Write a Python program to implement your own myfilter() function which works exactly
#     like Python's built-in function filter()

def myreduce(function, iterable, initializer=None) :
  it = iter(iterable)

  if initializer is None :
    try:
      initializer = next(it)
    except StopIteration:
      raise TypeError('myreduced called with empty sequence')

  accu = initializer

  for x in it:
    accu = function(accu, x)

  return accu

def myfilter(function, iterable) :
  return myreduce(lambda accu, x : accu + [x] if function(x) else accu, iterable, initializer=[])

if __name__ == "__main__":
  my_list = [1, 2, 3, 4, 5]

  result = myreduce(lambda x, accu : x + accu, my_list)

  print("Sum of list using myreduce is : {}\n".format(result))

  my_list = [12, 65, 54, 39, 102, 339, 221, 50, 70, ]

  result = list(myfilter(lambda x: (x % 13 == 0), my_list))

  print("Filtered list of multiples of 13 using myfilter is : {}\n".format(result))
