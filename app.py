import functions

print("Welcome to the Inspire Night Calculator")
print("---------------------------------------")
print("Please enter your first number")
numberOne = float(input())
print("Please choose your Operand from below")
operandsList = functions.operands()
for item in operandsList:
    print(item)
#print(operandsList[2])
operand = int(input())
print("---------------------------------------")
print("Please enter your second number")
numberTwo = float(input())
print("---------------------------------------")
print("You Calculated answer is:")
functions.calculation(numberOne,operand,numberTwo)