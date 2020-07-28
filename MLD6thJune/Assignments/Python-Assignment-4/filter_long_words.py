# Write a function filter_long_words() that takes a list of words and an integer n and returns
# the list of words that are longer than n.
import functools

def filter_long_words1(words, n) :
  return functools.reduce(lambda accu, x : accu + [x] if len(x) > n else accu, words, [])

def filter_long_words2(words, n) :
  return list(filter(lambda x : len(x) > n, words))

def filter_long_words3(words, n) :
  return [word for word in words if len(word) > n]

if __name__ == '__main__':
  print(filter_long_words1(['a' , 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg'], 1))
  print(filter_long_words2(['a' , 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg'], 1))
  print(filter_long_words3(['a' , 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg'], 1))
  print(filter_long_words1(['a' , 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg'], 3))
  print(filter_long_words2(['a' , 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg'], 3))
  print(filter_long_words3(['a' , 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg'], 3))
