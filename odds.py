#The goal of this script is to print all the odd numbers between
# 0 and N inclusively, wherr N is the user input 



# Use a For loop first 
print("using a for loop: ")
N= int(input("Enter an upper limit: "))
for number in range(1, N+1):
	if(number %2 == 1):
		print(number)


# Use a while loops: 
#print (usin a while loop:)