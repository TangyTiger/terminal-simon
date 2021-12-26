import random
from os import system, name
from time import sleep


colors = ("A","B","C","D")
pattern = []
user_input = []
score = 0

#def main():
  #create_pattern()
  #print_pattern(pattern)
  #get_input(pattern)
  #check_pattern(user_input, pattern)

#creating pattern with "colors"
def create_pattern():
  pattern.append(random.choice(colors))
  #print(pattern)
  #return pattern
  print_pattern(pattern)

  
#displaying pattern, with clearing the outputs before
def print_pattern(pattern):
  for i in range(len(pattern)):
    print(pattern[i])
    sleep(1)
    print(chr(27) + "[2J")
    #clear()
  get_input(pattern)

  
#getting input
def get_input(pattern):
  string_user_input = input("What is the pattern: ").upper()
  user_input = list(string_user_input)
  #print(user_input)
  if len(user_input) != len(pattern):
    print("Sorry better luck next time the pattern was " + "".join(pattern))
    game_over()
  else:
    check_pattern(user_input, pattern)

  for i in range(len(user_input)):
    if  user_input[i] != "A" and user_input[i] != "B" and user_input[i] != "C" and user_input[i] != "D":
      print("Invalid input, must only be letters 'A' 'B' 'C' 'D'")
      get_input()
  return user_input

#check user patten
def check_pattern(user_input, pattern):
  for i in range(len(user_input)):
      if user_input[i] != pattern[i]:
        print("Sorry better luck next time, the pattern was", "".join(pattern))
        game_over()
        break
      else:
        create_pattern()

#clear terminal to hide what was outputed before        
def clear():
  print("In clear")
  if name == 'nt': 
    _ = system('cls') 


#start new game
def game_over():
  print("Press RUN to play again")

create_pattern()
