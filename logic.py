small_jug= input("Enter the capacity of smaller jug:                                  ")     #Taking inputs
large_jug = input("Enter the capacity of larger jug:                                   ")
amount_required = input("Enter the required capacity:                                        ")
small_jug = int(small_jug)                                                                            #Converting strings to integers
large_jug  = int(large_jug)
amount_required = int(amount_required)

if (amount_required > large_jug or small_jug > large_jug):                                                 #Checking error condition
	print("Error")
	exit(0)

def gcd(small_jug,large_jug):                                                                         #Function to find gcd
	if(large_jug % small_jug == 0):
		return small_jug
	else:
		return gcd(large_jug % small_jug,small_jug)

a = gcd(small_jug,large_jug)

if(amount_required % a != 0):                                                                         #Checking existence of solution
	print("Solution does not exist")
	exit(0)

def solution(fromcap, tocap, amount):                                                      #Function to find optimal solution
	from_jug = fromcap
	to_jug = 0
	step = 0
	step += 1
	while (from_jug != amount and to_jug != amount):
		temp = min(from_jug, tocap - t)
		to_jug += temp
		from_jug -= temp
		step += 1

		if(from_jug == amount or to_jug == amount):
			break

		if (from_jug == 0):
			from_jug = fromcap

		if (to_jug == tocap):
			t = 0

		step += 1
	return step

def printSolution(fromcap, tocap, amount):                                                  #Function to print optimal solution
	from_jug = fromcap
	to_jug = 0
	print(from_jug,to_jug)
	while (from_jug != amount and to_jug != amount):
		temp = min(from_jug, tocap - to_jug)
		to_jug += temp
		from_jug -= temp
		print(from_jug, to_jug)

		if(from_jug == amount or to_jug == amount):
			break

		if (from_jug == 0):
			from_jug = fromcap

		if (to_jug == tocap):
			to_jug = 0

		print(from_jug, to_jug)

m1 = solution(small_jug,large_jug,amount_required)
m2 = solution(large_jug,small_jug,amount_required)

if(m1<m2):
	printSolution(small_jug,large_jug,amount_required)
else:
	printSolution(large_jug,small_jug,amount_required)
