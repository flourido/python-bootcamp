import random

winning_number= random.randint(0,100)
print(winning_number)


num_guesses = 10
user_won = False

while num_guesses != 0 and user_won == False:
	user_guess = int(input("Enter your guess: "))
	if user_guess == winning_number:
		print("Hey, you won! Number of guesses left:", num_guesses)
		user_won = True
	else:
		num_guesses -= 1
		if num_guesses == 0:
			print("Nope, you lost. Number of guesses left:", num_guesses)
		else:
			print("Nope, try again")