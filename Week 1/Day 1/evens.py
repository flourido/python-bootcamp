# the goal of this script is to print out the even numbers
# between 1 and N (inclusive), where N is a user input 

N= int(input("Enter an upper limit: "))

#for number in range(1, N+1):
	#if(number %2 == 0):
		#print(number)

#using a while loop to perfomr the same function 
N= int(input("Enter an upper limit: "))
print("using a while loop: ")
counter= 1
while counter <= N:
	if(counter %2 == 0):
		print(counter)

	counter += 1