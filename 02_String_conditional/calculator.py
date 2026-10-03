num1=int(input("Enter the number"))
num2=int(input("Enter the number"))
operator=input("Enter the operator")
match operator:
    case "+":
        print(num1+num2)
    case "-":
        print(num1-num2)
    case "*":
        print(num1*num2)
    case "/":
        print(num1/num2)
    case _:
        print("Invalid operator")
