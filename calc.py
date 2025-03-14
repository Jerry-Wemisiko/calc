
firstNum = int(input("Enter first number: "))
secondNum = int(input("Enter second number: "))

mathOperation = input("Enter math operation (+, -, *, /): ")

if mathOperation == "+":
    print(f"{firstNum} + {secondNum} = {firstNum + secondNum}")

elif mathOperation == "-":
    print(f"{firstNum} - {secondNum} = {firstNum - secondNum}")

elif mathOperation == "*":
    print(f"{firstNum} * {secondNum} = {firstNum * secondNum}")

elif mathOperation == "/":

    if secondNum != 0:
        value = firstNum / secondNum
        print(f"{firstNum}/{secondNum} = {value}")

    else:
        print("Math error~")

else :
    print("Invalid operation enter + , - , * , /")
