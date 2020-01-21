#define f(x)= x+1
#def f(x):
	#ans = x + 1
	#return ans  

# = f(1)
#print(my_solution)

# try for yourself
#define a function

#def g(x):
	#ans = (x**4 + x**2 + 1) 
	#return ans

#my_solution = g(1), g(2), g(3)
#print(my_solution)

#def get_first_two_evens():
	#return 2,4

#even1, even2 = get_first_two_evens()
#print(even1)
#print(even2)

#function with no returns
#def print_even(N):
	#for num in range(0,N+1):
		#if num %2 == 0:
			#print(num)

#print_even(10) #2,,4,6,8,10		

#TODO: Write a function that takes N as in an input and print 
# all common multiples of 3 and 7, between 0 and N (inclusive)
#N= int(input("enter the upper limit: "))
#def com_mul_3_7(N):
	#number=0
	#for number in range(0,N+1):
	#	if(number %3 == 0) and (number %7 == 0):
	#		print(number)	
#com_mul_3_7(N

#define a function that takes 3 inputs: x, y , N

def find_mult_x_y(x,y,N):
	number=0
	for number in range(0,N+1):
		if(number %x == 0) and (number %y == 0):
			print(number)	
find_mult_x_y(2,3,10)