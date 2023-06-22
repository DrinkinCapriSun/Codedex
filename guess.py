guess = 0
tries = 0

while guess != 6:
  tries += 1
  guess = int(input("Guess the number:  "))

  if tries == 3:
    print("Out of chance")
    break

  elif guess ==6:
    print("You got it!")






