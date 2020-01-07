#The goal of this script is to print all the odd numbers between
# 0 and N inclusively, wherr N is the user input 



# Use a For loop first 
N= int(input("Enter an upper limit: "))
print("using a for loop: ")
for number in range(0, N+1):
	if(number %2 == 1):
		print(number)


# Use a while loops: 
print("using a while loop: ")
number= 1
while number <= N:
	if(number %2 == 1):
		print(number)

	number += 1