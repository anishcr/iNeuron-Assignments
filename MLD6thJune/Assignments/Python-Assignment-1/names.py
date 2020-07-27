# Write a Python program to accept the user's first and last name and then getting them 
# printed in the the reverse order with a space between first name and last name.

def get_string(prompt) :
  while True:
    val = input(prompt).strip()

    if val != "" :
      return val

def reverse_string(str):
  return str[-1::-1]

if __name__ == "__main__":
    # execute only if run as a script

    firstName = get_string("Please enter your First Name :")
    lastName  = get_string("Please enter your Last Name :")

    print("Reversed First and Last Names are : {} {}".format(reverse_string(firstName), reverse_string(lastName)))
