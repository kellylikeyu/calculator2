"""CLI application for a prefix-notation calculator."""

from ast import operator
from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    print()
    consume_input = input('What is your operator and numbers? :')
    tokens = consume_input.split(' ')
    num1 = float(tokens[1])
    num2 = float(tokens[2])

    if tokens[0] == 'q':
        break

    elif tokens[0] == "+":
        result = add(num1, num2)

    elif tokens[0] == "-":
        result = subtract(num1, num2)

    elif tokens[0] == '*':
        result = multiply(num1, num2)

    elif tokens[0] == '/':
        result = divide(num1, num2)

    elif tokens[0] == 'square':
        result = square(num1)

    elif tokens[0] == 'cube':
        result = cube(num1)
    
    elif tokens[0] == 'power':
        result = power(num1, num2)

    elif tokens[0] == 'mod':
        result = mod(num1, num2)

    # elif tokens[0] == '++':
    #      result = add_mult(num1, num2, float(tokens[3]))
    print (result)
