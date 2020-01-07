# the goal of this script is to sum up all the numbers between
# N and M (inclusively), where N and M are both user inputs.

N= int(input("Enter an lower limit: "))
M= int(input("Enter an upper limit: "))
#print("using a for loop: ")
#sum = 0

#for num in range(N,M+1):
	#sum += num 

#print("The total sum is:", sum)

#print("The type is:", type(sum))


print("using a while loop ")
sum = 0
num = N
while num <= M:
	sum += num
	num += 1

print("The total sum is:", sum)