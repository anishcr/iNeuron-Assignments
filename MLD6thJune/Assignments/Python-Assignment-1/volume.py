# Write a program to find the volume of a sphere with diameter 12 cm

import math

# Function which will return the volume of a sphere, given its diameter
# This function is not bothered about the unit of diameter (mm, cm, m etc)
def sphere_volume(diameter) :
  return (4 / 3) * math.pi * ((diameter / 2) ** 3)
  
if __name__ == "__main__":
  diameter = 12
  print("Volume of a sphere with diameter {} cm is : {:0.3f} cm cube".format(diameter, sphere_volume(diameter)))
