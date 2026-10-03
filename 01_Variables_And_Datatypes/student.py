user=input("Enter your name: ")
print("Hello, " + user + "!")
marks1=int(input("Enter your english marks: "))
marks2=int(input("Enter your maths marks: "))
marks3=int(input("Enter your science marks: "))
marks4=int(input("Enter your computer marks: "))

total_marks=marks1+marks2+marks3+marks4
print("Total marks are: ", total_marks)
average_marks=total_marks/4
print("Average marks are: ", average_marks)