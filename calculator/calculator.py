import os
import re

os.system('cls')
print('*'*25+'\n'+' '*7+'CALCULATOR\n')
try:
    i_num = str(float(input('Digit a number: ')))
except:
    print("error: invalid input")
    exit()
expression = i_num
result = None

while True:
    os.system('cls')
    print('*'*25+'\n'+' '*7+'CALCULATOR\n')
    print(expression + ' = ' + str(result)) if result != None else print(expression)
    print('\nA) +\nB) -\nC) \u00F7\nD) \u00D7\nE) \u2190\nQ) quit\n'+'*'*25)
    equation = input('-> ')

    if equation.lower() == 'a':
        expression += '+'
        expression += str(input('Enter other number: '))
    elif equation.lower() == 'b':
        expression += '-'
        expression += str(input('Enter other number: '))
    elif equation.lower() == 'c':
        expression += '/'
        expression += str(input('Enter other number: '))
    elif equation.lower() == 'd':
        expression += '*'
        expression += str(input('Enter other number: '))
    elif equation.lower() == 'e':
        last_equation = re.findall("(.[0-9]+)", expression)[-1]
        expression = expression.removesuffix(last_equation)
    elif equation.lower() == 'q':
        break
    
    try:
        result = eval(expression)
    except:
        print('error: invalid input')
        exit()