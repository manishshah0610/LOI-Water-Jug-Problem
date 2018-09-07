m = input("Enter the capacity of smaller jug:                                  ")     #Taking inputs
n = input("Enter the capacity of larger jug:                                   ")
c = input("Enter the required capacity:                                        ")
m = int(m)
n = int(n)
c = int(c)

if (c>n or m>n):                                                                      #Checking error condition
	print("Error")
	exit(0)

def gcd(m,n):                                                                         #Function to find gcd
	if(n%m == 0):
		return m
	else:
		return gcd(n%m,m)

a = gcd(m,n)

if(c%a != 0):                                                                         #Checking existence of solution
	print("Solution does not exist")

else:
	x = 0                                                                         #x denotes current amount in m
	y = 0                                                                         #y denotes current amount in n

	while(x != c and y!=c):
		if(x==0):
			x = x + n
		else:
			x = (x - (m-y))
		y = (y + (n-x))
		print (x,y)
