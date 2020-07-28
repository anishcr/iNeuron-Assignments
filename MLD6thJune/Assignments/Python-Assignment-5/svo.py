# Implement a Python program to generate all sentences where subject is in
# ["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in
# ["Baseball","cricket"].

def generate_sentences(subjects, verbs, objects) :
  return [ s + " " + v + " " + o + "." for s in subjects for v in verbs for o in objects]

if __name__ == "__main__":
  subjects = ["Americans", "Indians"]
  verbs    = ["play", "watch"]
  objects  = ["baseball", "cricket"]

  print(generate_sentences(subjects, verbs, objects))
