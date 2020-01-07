#TODO: write a script that prints out the multiple of 3
#between 0 and N, where N is a user input

N= int(input("Enter an upper limit: "))

#number=0
#for number in range(0,N+1):
	#if(number %3 == 0):
		#print(number)

counter = 0
while counter <= N:
	if counter %3 ==0:
		print(counter)
counter += 1