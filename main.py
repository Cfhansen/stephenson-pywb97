###solution to exercise 97 from ben stephenson's "the python workbook".
###restoring the commented lines restricts the password to alphanumeric characters.

import random

def good(password):
  uppercase = False
  lowercase = False
  number = False

  uppercases = []
  for i in range(65,91):
    uppercases.append(chr(i))
  lowercases = []
  for i in range(97,123):
    lowercases.append(chr(i))
  numbers = []
  for i in range(48,58):
    numbers.append(chr(i))

  for i in password:
    if i in uppercases:
      uppercase = True
    if i in lowercases:
      lowercase = True
    if i in numbers:
      number = True

  if uppercase and lowercase and number and (len(password) >= 8):
    return True
  else:
    return False

mypass = ''
attempts = []
while not good(mypass):
  mypass = ''
  for n in range(8):
    seed = random.randint(48,122)
    """
    while seed in range(58,65) or seed in range(91,97):
      seed = random.randint(48,122)
    """
    mypass = mypass + chr(seed)
  attempts.append(mypass)

print(f'Your password is {mypass}. {len(attempts)} attempt(s) were required.')
