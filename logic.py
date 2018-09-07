m = input("Enter the capacity of smaller jug:                                  ")     #Taking inputs
n = input("Enter the capacity of larger jug:                                   ")
c = input("Enter the required capacity:                                        ")
m = int(m)
n = int(n)
c = int(c)

if (c>m and c>n):                                                                     #Checking error condition
	print("Error")

def gcd(m,n):                                                                         #Function to find gcd
	if(n%m == 0):
		return m
	else:
		return gcd(n%m,m)

a = gcd(m,n)
print(a)

if(c%a != 0):                                                                         #Checking existence of solution
	print("Solution does not exist")
	return

x = 0                                                                                 #x denotes current amount in m
y = 0                                                                                 #y denotes current amount in n
