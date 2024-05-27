# perform basic +-*/
# specify enter a number and operator they want to use
# then enter second number
# then do operation

print("Hello welcome to your basic calculator")

num1 = int(input("Pls enter first num "))
num2 = int(input("Pls enter second num "))
operation = int(input(
    """Please enter the number corresponding to the desired operation:
    1 for Addition
    2 for Subtraction
    3 for Division
    4 for Multiplication
    Your choice: """
))


def operationfunc(num1, num2, operation):
    if operation == 1:
        return num1+num2
    elif operation == 2:
        return num1-num2
    elif operation == 3:
        return num1/num2
    else:
        return num1*num2


print("Result:",operationfunc(num1,num2,operation))
