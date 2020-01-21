import random

def organize_games():	
	#one door will have the money, the others have nothing:
	door_contents =[1,0,0]
	random.shuffle(door_contents)
	# the shuffle function

	#use the linear search algo to find the door with money 
	for i in range(0, len(door_contents)):
		if door_contents[i] == 1:
			winning_door = i
	#return the list of door contents and the number of winning door
	return door_contents, winning_door

def game_time():
	#the door numbers go from 0 to 2, correspnond to the door contents
	door_nums = [ 0, 1, 2]

	#runs the previous written function to orgnaize the game
	#which puts contents behind the doors, and tells the host which door
	#is the winning door
	door_contents, winning_door = organize_games()

	#simulated a contestant, the contestant will make a choice 0 to 2
	#corresponding to door numbers
	door_chosen = random.choice(door_nums)

	# make a list of the unavailable doors to be opened by the host
	unavaliable_doors = [door_chosen, winning_door]

	#using sets to find the door number left over
	#this "door to open" returns as a set
	door_to_open = set(door_nums).difference(unavaliable_doors)
	door_to_open = door_to_open.pop()

	#open door we just picked
	opened_door = door_nums[door_to_open]

	# declare the variables that tells us whether the win would
	#come from switching or staying
	switched_win = False
	stayed_win = False
	
	#we need to see if we won by switching or staying
	#first we simulate the switch
	#we cant switch to either the door we chose or door opened
	unavaliable_doors = [door_chosen, door_to_open]
	switched_choice = set(door_nums).difference(unavaliable_doors)

	#switched choice is currently a set so we use pop
	#swithced set 
	switched_choice= switched_choice.pop()

	#use the index value we established from the switched_choice variable
	#to find out the contents of the door behind it
	if door_contents[switched_choice] == 1:
		#this means that the user one by switching
		switched_win = True 
	if door_contents[door_chosen] == 1:
		stayed_win = True	

	return int(switched_win), int(stayed_win)

def monte_carlo (N):
	#keep track of number of wins from switching and staying
	total_switched_win = 0
	total_stayed_win = 0

	#need to play the game N number of times
	switched_win = 0
	stayed_win = 0
	for game_num in range (0,N):
		#determine if we won by switching, or won by staying
		switched_win,stayed_win = game_time()

		#if we won by switching, increment total switched wins
		if switched_win == 1:
			total_switched_win += 1

		#if we won by switching, increment total switched wins
		if stayed_win == 1:
			total_stayed_win += 1

	print(f"Out of {N} plays")
	print(f"Switched win percentage = {(total_switched_win/N) * 100} %")
	print(f"Stayed win percentage = {(total_stayed_win/N) * 100} %")



monte_carlo(100000)

