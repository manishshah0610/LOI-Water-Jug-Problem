m = input("Enter the capacity of smaller jug:                                  ")     #Taking inputs
n = input("Enter the capacity of larger jug:                                   ")
c = input("Enter the required capacity:                                        ")
m = int(m)                                                                            #Converting strings to integers
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
	exit(0)

def solution(fromcap, tocap, d):                                                      #Function to find optimal solution
	f = fromcap
	t = 0
	step = 0
	step += 1
	while (f != d and t != d):
		temp = min(f, tocap - t)
		t += temp
		f -= temp
		step += 1

		if(f == d or t == d):
			break

		if (f == 0):
			f = fromcap

		if (t == tocap):
			t = 0

		step += 1
	return step

def printSolution(fromcap, tocap, d):                                                  #Function to print optimal solution
	f = fromcap
	t = 0
	print(f,t)
	while (f != d and t != d):
		temp = min(f, tocap - t)
		t += temp
		f -= temp
		print(f, t)

		if(f == d or t == d):
			break

		if (f == 0):
			f = fromcap

		if (t == tocap):
			t = 0

		print(f, t)

m1 = solution(m,n,c)
m2 = solution(n,m,c)

if(m1<m2):
	printSolution(m,n,c)
else:
	printSolution(n,m,c)
