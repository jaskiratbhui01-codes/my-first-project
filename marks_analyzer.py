#Students marks analyzer
name=input("Enter your name-")
eng=int(input("enter your marks in english-"))
maths=int(input("enter your marks in maths-"))
bst=int(input("enter your marks in business studies-"))
eco=int(input("enter your marks in Economics-"))
acc=int(input("enter your marks in accountancy-"))
t=eng+maths+bst+eco+acc
av=t/5
print("Total Marks: ",t)
print("Percentage: ",av)
if av>=90:
	print("Grade: A")
elif av>=75:
	print("Grade: B")
elif av>=60:
	print("Grade: C")
else:
	print("Grade: D")

