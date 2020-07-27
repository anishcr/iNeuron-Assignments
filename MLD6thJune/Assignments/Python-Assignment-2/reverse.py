# Write a Python program to reverse a word after accepting the input from the user.

def get_string(prompt) :
  while True:
    val = input(prompt).strip()

    if val != "" :
      return val

def reverse_string(str):
  return str[-1::-1]

if __name__ == "__main__":
    # execute only if run as a script

    str = get_string("Please enter the string to be reversed :")

    print("Reverse of '{}' is '{}'".format(str, reverse_string(str)))
