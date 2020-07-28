# Write a Python Program(with class concepts) to find the area of the triangle using the below formula.
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# Function to take the length of the sides of triangle from user should be defined in the parent
# class and function to calculate the area should be defined in subclass.

import unittest

class ParentTriangle():
  def __init__(self) :
    self.lengthsValid = False
    self.len1 = 0
    self.len2 = 0
    self.len3 = 0

  def __is_lengths_valid(self, len1, len2, len3) :
    if (len1 <= 0) or (len2 <= 0) or (len3 <= 0) :
      return False;

    return (len1 < (len2 + len3)) and (len2 < (len1 + len3)) and (len3 < (len1 + len2)) 

  def set_lengths(self, len1, len2, len3) :
    if self.__is_lengths_valid(len1, len2, len3) :
      self.len1 = len1
      self.len2 = len2
      self.len3 = len3
      self.lengthsValid = True

      return {"success" : True}
    else :
      return {"success" : False, "error" : "The lengths cannot make a valid triangle"}


class Triangle(ParentTriangle) :
  def __init__(self) :
    ParentTriangle.__init__(self)

  def get_area(self) :
    if (self.lengthsValid == False) :
      return {"success" : False, "error" : "The lengths of the triangle has not been set"}

    s = (self.len1 + self.len2 + self.len3) / 2

    return {"success" : True, "area" : ((s * (s - self.len1) * (s - self.len2) * (s - self.len3)) ** 0.5)}


class TestTriangleMethods(unittest.TestCase):

    def test_will_not_accept_zero_length(self) :
      t = Triangle()

      ret = t.set_lengths(0, 1, 2)
      self.assertEqual(ret['success'], False)

      ret = t.set_lengths(2, 0, 3)
      self.assertEqual(ret['success'], False)

      ret = t.set_lengths(8, 4, 0)
      self.assertEqual(ret['success'], False)


    def test_will_not_accept_negative_length(self) :
      t = Triangle()

      ret = t.set_lengths(-1, 1, 2)
      self.assertEqual(ret['success'], False)

      ret = t.set_lengths(2, -9, 3)
      self.assertEqual(ret['success'], False)

      ret = t.set_lengths(8, 4, -100)
      self.assertEqual(ret['success'], False)

    def test_will_not_accept_lengths_that_cannot_form_a_triangle(self) :
      t = Triangle()

      ret = t.set_lengths(1, 1, 3)
      self.assertEqual(ret['success'], False)

      ret = t.set_lengths(3, 1, 1)
      self.assertEqual(ret['success'], False)

      ret = t.set_lengths(1, 3, 1)
      self.assertEqual(ret['success'], False)

    def test_set_valid_lengths(self) :
      t = Triangle()

      ret = t.set_lengths(1, 1, 1)
      self.assertEqual(ret['success'], True)

      ret = t.set_lengths(4, 3, 2)
      self.assertEqual(ret['success'], True)

    def test_areas(self) :
      t = Triangle()

      ret = t.set_lengths(4, 3, 2)
      self.assertEqual(ret['success'], True)

      ret = t.get_area()
      self.assertEqual(ret['success'], True)
      
      expected_area = 2.9047
      returned_area = ret['area']
      self.assertEqual(abs(expected_area - returned_area) <=  0.01, True)

    def test_no_change_in_area_after_setting_invalid_length(self) :
      t = Triangle()

      ret = t.set_lengths(4, 3, 2)
      self.assertEqual(ret['success'], True)

      ret = t.get_area()
      self.assertEqual(ret['success'], True)
      returned_area = ret['area']

      ret = t.set_lengths(1, 5, 1)
      self.assertEqual(ret['success'], False)

      ret = t.get_area()
      self.assertEqual(ret['success'], True)
      self.assertEqual(ret['area'], returned_area)

if __name__ == '__main__':
  unittest.main()
