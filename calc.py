import math as m
import re

def op(x,y,operator):
    if(checknum(x,y)):
        if operator == '+': return x+y,
        if operator == '-': return x-y,
        if operator == '*': return x*y,
        if operator == "/" and y != 0: return x/y,
        if operator == "/" and y == 0: return ["division by zero",]
    else:
        return "bad expression"

def parse(str):
    numbers = []
    operators = 0
    operator = ''
    flag = False
    num = ''
    # re.sub(str, '', ' ')

    if str[0] in '-+':
        num += str[0]
        str = str[1:len(str)]

    for symbol in str:
        if symbol == ' ':
            symbol = ''
            continue
        if symbol in '123456789.0':
            flag = True
            num += symbol
            continue
        else:
            if symbol in '+-*/':
                operators += 1
                if operators > 1: symbol = ''
                if operators == 1:
                    operator = symbol
                    numbers.append(float(num))
                    num = ''
                    flag = False
                continue
        if not flag:
            print("Bad expression")
            return

    if operators < 1:
        print("No operators found")
        return
    numbers.append(float(num))

    if operators==1 and flag==True and len(numbers)>1:
        return numbers, operator


def checknum(*args):
    for var in args:
        if type(var) is float:
            return True
        else:
            print("at least one value is not a number")
            return False


def main():
    print("Welcome to the standart calc!")
    print("Type two numeric values with an operation between")
    while True:
        expr = input()
        if expr != '':
            try:
                numbers, operator = parse(expr)
            except TypeError:
                print("Bad Expression")
            except ValueError:
                print("Bad Expression")
            else:
                print(op(numbers[0], numbers[1], operator)[0])

main()