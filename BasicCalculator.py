def BasicCalulator():
   
    operator=input("Enter the operator (+, -, *, /): ")
    if operator=='+':
        return num1+num2
    elif operator=='-':
        return num1-num2
    elif operator=='*':
        return num1*num2
    elif operator=='/':
        return num1/num2
    else:
        return "Invalid operator"
if __name__=='__main__':
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    print('The result is: ',BasicCalulator())


