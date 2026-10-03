user1=input("Enter a number: ")
user2=input("Enter a number: ")
user3=input("Enter a number: ")
sum= int(user1)+int(user2)+int(user3)
print("The sum of the three numbers is: ", sum)
avg= sum/3
print("The average of the three numbers is: ", avg)
product=int(user1)*int(user2)*int(user3)
print("The product of the three numbers is: ", product)
if int(user1)> int(user2) and int(user1)>int(user3):
    print("The largest number is: ", int(user1))
elif int(user2)>int(user1) and int(user2)>int(user3):
    print("The largest number is: ", int(user2))
else:
    print("The largest number is: ", int(user3))

if int(user1)< int(user2) and int(user1)<int(user3):
    print("The smallest number is: ", int(user1))
elif int(user2)<int(user1) and int(user2)<int(user3):
    print("The smallest number is: ", int(user2))
else:
    print("The smallest number is: ", int(user3))