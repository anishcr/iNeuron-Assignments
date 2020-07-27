# Make the below pattern using nested for loop in python
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

def create_pattern(max_num) :
  iter = max_num * 2
  
  for i in range(1, iter):
    if i <= max_num:
      end_num = i
    else:
      end_num = iter - i 

    for j in range(0, end_num):
      print("*", end="")
    print("")

if __name__ == "__main__":
  # execute only if run as a script

  create_pattern(5)

  print("\n\n")
  
  create_pattern(8)
