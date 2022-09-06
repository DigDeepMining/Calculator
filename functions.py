def operands():
    operands = [
        "1 for ' * '",
        "2 for ' - '",
        "3 for ' + '",
        "4 for ' / '"
    ]
    return operands

def calculation(numberOne,operand,numberTwo):
    if operand == 1:
        calculation = numberOne * numberTwo
    elif operand == 2:
        calculation = numberOne - numberTwo
    elif operand == 3:
        calculation = numberOne + numberTwo
    else:
        calculation = numberOne / numberTwo
        
    print(round(calculation,2))
    return calculation