#practice with lists and functions

#example: define a function that returns a list of even numbers between
#A and B (inclusive)

def find_evens(A,B):
	evens =[]
	for nums in range(A,B+1):
		if(nums %2 == 0):
			evens.append(nums)
	return evens

print(find_evens(2,20))

#TODO: Define a function that returns a list of numbers between 
#A and B (inclusive) that are even multiples of 3 
def find_evens_mult_3(A,B):
	evens_mults =[]
	for nums in range(A,B+1):
		if(nums %2 == 0 and nums %3 == 0):
			evens_mults.append(nums)
	return evens_mults
print("List of numbers that are even multiples of 3")
print(find_evens_mult_3(0,20))