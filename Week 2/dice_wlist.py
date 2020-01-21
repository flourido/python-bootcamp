import random 
def dice(highest_num):
	return random.randint(1,highest_num)

	one= 0
	two= 0
	three= 0
	four= 0
	five= 0
	six= 0
	dice_max= 0

	for exp in range(0,n):
		if dice(dice_max) == 1:
			one += 1
		elif dice(dice_max) == 2:
			two += 1
		elif dice(dice_max) == 3:
			three += 1
		elif dice(dice_max) == 4:
			four += 1
		elif dice(dice_max) == 5:
			five += 1
		elif dice(dice_max) == 6:
			six += 1			

	print(f"probability of 1 = {(one/N) * 100} %")
	print(f"probability of 2 = {(two/N) * 100} %")
	print(f"probability of 3 = {(three/N) * 100} %")
	print(f"probability of 4 = {(four/N) * 100} %")
	print(f"probability of 5 = {(five/N) * 100} %")
	print(f"probability of 6 = {(six/N) * 100} %")

def monte_carlo_with_list(N,dice_max=6):
	results = []

	for exp in range(0,N):
		results.append(dice(dice_max))

	 print(f"{N} experments were performed")
	for outcome in range(1,dice_max + 1):
		count= results.count(outcome)
		msg = f"The probability of {outcome} = {(count/N *100)} %"
		print(msg)

dice_max= 10
print(f"The probability should converge to {1/dice_max * 100} %")
monte_carlo_with_list(10000, dice_max)
