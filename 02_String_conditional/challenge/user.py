user=int(input("Enter the number"))
total=0
while(True):
    if(user==0):
        break
    elif(user<0):
        user=int(input("Enter the number"))
        continue
    total=total+user
    user=int(input("Enter the number"))
  
print("Total:", total)  