#!/usr/bin/env python
first_int = 0
second_int = 0

def get_first():
    try:
        global first_int
        first_int = int(raw_input('Enter your first integer: '))
    except:
        print 'Incorrect entry'
        get_first()

def get_second():
    try:
        global second_int
        second_int = int(raw_input('Enter your second integer: '))
    except:
        print 'Incorrect entry'
        get_second()

def add(first, second):
    '''
    the sum of the first and second number
    '''
    sum_result = first + second
    return sum_result

def subtract(first, second):
    '''
    the result of subtracting the second number from the first
    '''
    diff_result = first - second
    return diff_result

def multiply(first, second):
    '''
    the product of the first and the second number
    '''
    prod_result = first * second
    return prod_result

def divide(first, second):
    '''
    the integer division of the first number by the second number, 
    followed by the remainder from dividing the first number by the second number
    '''
    if second == 0:
        return 'undefined'
    else:
        int_div = first // second
        remainder = first % second
        return str(int_div) + ' with a remainder of ' + str(remainder)


get_first()

get_second()

print 'The sum of ' + str(first_int) + ' and ' + str(second_int) + ' is the following: ' + str(add(first_int, second_int))

print 'The difference between ' + str(first_int) + ' and ' + str(second_int) + ' is the following: ' + str(subtract(first_int, second_int))

print 'The product of ' + str(first_int) + ' and ' + str(second_int) + ' is the following: ' + str(multiply(first_int, second_int))

print 'The quotient of ' + str(first_int) + ' and ' + str(second_int) + ' is the following: ' + str(divide(first_int, second_int))

