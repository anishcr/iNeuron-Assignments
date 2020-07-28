#2.1 Write a Python program using function concept that maps list of words into a list of integers
# representing the lengths of the corresponding words.
# Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
# Here 2,3 and 4 are the lengths of the words in the list.

def word_to_len(words) :
  return (list(map(len, words)))

if __name__ == '__main__':
  print(word_to_len(["a", "ab", "abc", "abcd", "abcde"]))
