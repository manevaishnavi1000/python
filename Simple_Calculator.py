#simple calculator in python
#function to add two numbers
def add(num1,num2):
    return num1+num2
#function to subtract two numbers
def subtract(num1,num2):
    return num1-num2
#function to multiply two numbers
def multiply(num1,num2):
    return num1*num2
#function to divide two numbers
def divide(num1,num2):
    return num1/num2
while(1):
    print("Please select operation :\n")
    print("1.add\n 2.subtract\n 3.multiply\n 4.divide\n")
    #take input from the user
    select=int(input("Select operation from 1,2,3,4:"))
    number1=int(input("Enter first number to perform operations :"))
    number2=int(input("Enter second number to perform operations :"))
    if select==1:
        print(number1,"+",number2,"=",add(number1,number2))
    elif select==2:
        print(number1,"-",number2,"=",subtract(number1,number2))
    elif select==3:
        print(number1,"*",number2,"=",multiply(number1,number2))
    elif select==4:
        print(number1,"/",number2,"=",divide(number1,number2))
    else:
        print("invalid input\n")