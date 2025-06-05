num1 = float(input("Enter the first number: \n"))
num2 = float(input("Enter the second number: \n"))

print("Select Operation:")
print("1. Add", "2. Subtract", "3. Multiply", "4.Divide")

operation = input("Enter operation: \n")

if operation == "1":
    result = num1 + num2
    print(f"The sum of the two numbers {num1} + {num2} is: {result}")
elif operation == "2":
    result = num1 - num2
    print(f"The subtraction of the two numbers {num1} - {num2} is: {result}")
elif operation == "3":
    result = num1 * num2
    print(f"The multiplication of the two numbers {num1} * {num2} is: {result}")
elif operation == "4":
    if(num2!=0):
        result = num1 / num2
        print(f"The quotient of the two numbers {num1} / {num2} is: {result}")
    else:
        print("Error!! Cannot be divide by Zero")
else:
    print("Invalid input! Please select a valid operation")