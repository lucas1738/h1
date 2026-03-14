#print(10/0)
try:  
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("you can't divide zero")
else:
    print(f"the answer is {result}")
    print("thank you for using our calculator")

