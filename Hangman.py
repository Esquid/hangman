import random
import csv


def hang():
    gallows = [',--;-', '| ', '| ', '| ', '| ', '| ', '|_____']
    parts = iter([' 0 ', '/', '|', '\\', ' | ', ' A ', '/ ', '\\'])
    sequence = [1, 3, 1, 1, 2]
    for i, v in enumerate(sequence, start=1):
        for k in range(v):
            gallows[i] += next(parts)
            yield '\n'.join(gallows)
    raise StopIteration

def game():
  csv_file = open('words.csv')
  secret = random.choice(list(csv_file))
  blanks = "_ ".join("_ " for l in secret)
  print(blanks)
  guess = input("Guess a letter: ")
  if guess != secret:
    print(guess)
    print(next(hang()))
    input("Guess Again:")
  if guess == secret:
      print(guess for l in blanks)
      print(blanks)
      input("Guess Again:")
  

  


  
  
  
