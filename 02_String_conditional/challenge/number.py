user=int(input("Enter the number:"))
while(True):
    if(user==0):
        break
    elif(user<0):
        print("Negative number")
    else:
        print(user)
    user=int(input("Enter the number"))