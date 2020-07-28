# 2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns True if
# it is a vowel, False otherwise.


def is_vowel(char) :
  vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

  if len(char) != 1 :
    return False

  return char in vowels

if __name__ == '__main__':
  print(is_vowel(''))
  print(is_vowel('abc'))
  print(is_vowel('b'))
  print(is_vowel('Z'))
  print(is_vowel('e'))
  print(is_vowel('E'))
  
