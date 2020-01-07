#TODO: write a script that prints the common multiples of 3
#and 5 between the range 0 and N(inclusive). Where N is a user input

N= int(input("enter the upper limit: "))
number=0
for number in range(0,N+1):
	if(number %3 == 0) and (number %5 == 0):
		print(number)