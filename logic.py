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

	
#GUI CODE

from tkinter import *

root=Tk()
root.title("New Application")

root.geometry("640x640+0+0")

heading = Label(root, text="Welcome to the Water Jug Problem",font=("Aerial",40,"bold"),fg="steelblue").pack()

label=Label(root,text="Enter the value of larger jug: ", font=("aerial",20,"bold"), fg="green").place(x=10,y=200)
label=Label(root,text="Enter the value of smaller jug: ", font=("aerial",20,"bold"), fg="green").place(x=10,y=250)
label=Label(root,text="Enter the amount to be filled: ", font=("aerial",20,"bold"), fg="green").place(x=10,y=300)
label=Label(root,text="Choose the jug in which you want the water to be filled: ", font=("aerial",20,"bold"), fg="green").place(x=10,y=400)


name1=StringVar()
name2=StringVar()
name3=StringVar()

entry_box=Entry(root, text=name1, width=25, bg="lightgreen").place(x=420, y=210)
entry_box=Entry(root, text=name2, width=25, bg="lightgreen").place(x=420, y=260)
entry_box=Entry(root, text=name3, width=25, bg="lightgreen").place(x=420, y=310)


Radio_1=Radiobutton(root, text="Larger Jug   ", width= 40, value=1, font=("aerial",15,"bold"), fg="grey").place(x=10,y=440)
Radio_2=Radiobutton(root, text=" Smaller Jug", width= 40, value=2, font=("aerial",15,"bold"), fg="grey").place(x=10,y=500)

def do_it():
    print("value of the larger jug is :"+ str(name1.get()))
    print("value of the smaller jug is :"+ str(name2.get()))
    print("Value required is :"+ str(name3.get()))


work=Button(root, text="Enter", width=15, height=2, bg="lightblue", command=do_it).place(x=250,y=600)
root.mainloop()
