# Name: Faiyam Islam 
# Date: 9/02/22
# Description: Program which picks a number between 1 and 100, and allow the user to guess it, 
# checking whether or not the prediction is correct

import random 
winning_number = random.randint(1, 100)
guesses = 0; 

print("Hi player, the computer has thought of a number between 1 - 100. Your job is to guess that number. You have 7 guesses to guess the correct number.")
while guesses < 7: 
  user_guess = input("Input a number here: ")
  if user_guess.isdigit() and int(user_guess) <= 100 and int(user_guess) >= 1:
    guesses = guesses + 1
    if int(user_guess) == winning_number:
      print("You win!!! It took you " + str(guesses) + "guesses")
      break
    if int(user_guess) > winning_number:
      print("The answer is lower, try again")
      print("You have " + str(7 - guesses) + " guesses left")
    if int(user_guess) < winning_number:
      print("The answer is higher, try again")
      print("You have " + str(7 - guesses) + " guesses left")
  else: 
    print("Please enter a number from 1 to 100")

if guesses == 7:
  print("You ran out of guesses, better luck next time!")