#import the random library
import random

# Lists all possible password outcomes
letters = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
  'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
  'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sChars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']

#Create password list
pw = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

pw[0] = random.choice(letters)
pw[1] = random.choice(numbers)
pw[2] = random.choice(letters)
pw[3] = random.choice(letters)
pw[4] = random.choice(sChars)
pw[5] = random.choice(letters)
pw[6] = random.choice(numbers)
pw[7] = random.choice(letters)
pw[8] = random.choice(letters)
pw[9] = random.choice(sChars)

print(pw)
