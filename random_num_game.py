#import the random 
#import random

#winning_number= random.randint(0,10)
#print(winning_number)


#num_guesses = 5
#user_won = False

#while num_guesses != 0 and user_won == False:
#	user_guess = int(input("Enter your guess: "))
#	if user_guess == winning_number:
#		print("Hey, you won!")
#		user_won = True
#	else:
#		num_guesses -= 1
#		if num_guesses == 0:
#			print("Nope, you lost.")
#		else:
#			print("Nope, try again")


import random

winning_number = random.randint(0, 100)
total_guesses = 10
guesses = []
user_won = False
guesses_taken = 0

while guesses_taken < total_guesses and user_won == False:
    user_guess = int(input("Enter your guess: "))
    guesses.append(user_guess)
    guesses_taken += 1
    if user_guess == winning_number:
        user_won = True
        print("Congrats! You won!")
    elif abs(user_guess - winning_number) <= 5:
        print("Hot!")
    elif abs(user_guess - winning_number) <= 10:
        print("Warm!")
    else:
        print("Cold :(")

print("You took", guesses_taken)
print("Your guesses were: ")
print(guesses)
