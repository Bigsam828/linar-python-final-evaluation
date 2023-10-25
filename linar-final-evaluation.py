
'''1) Variable Data Types
a) Create a variable called "Date_Of_Birth" and assign it the year you were born (or any random
year) using the right datatype. Print the value of the variable.
b) What is the difference between an integer and a floating-point number in Python? Backup your
explanation with an example for each.'''
#---------------------solution for a ------------------------------#
Date_Of_Birth = 2007
print(Date_Of_Birth)

#---------------------solution for b ------------------------------#
#The difference between intergers and floating point numbers in python is simply that integers 
#do not have decimals in them, while floats/ floating point numbers do
'''Exmaple of integer:
    1
    4000
    487384387

Examples of floating point numbers
    32.0
    345.3443
    0.767346
    '''

'''2) Basic Operations
a) Write a Python program that adds two numbers together and prints the result.
b) Write a Python program that takes a number as input and multiplies it by 10. Print the result.'''

#---------------------solution for a ------------------------------#
def sum(x,y):
    sum = x+y 
    print(sum)

sum(x=float(input(' enter the first number')), y=float(input(' enter the second number')))

#---------------------solution for b ------------------------------#
def multiplier():
    num = float(input('enter a value'))
    product = num  * 10
    return product

print(multiplier())

'''3) Control Structures
a) Write a Python program that checks if a number is even or odd. If the number is even, print
"Even", otherwise print "Odd".
b) Write a Python program that takes a number as input and checks if it is positive, negative, or
zero. Print the result.'''

#---------------------solution for a ------------------------------#
num = float(input('Enter a number'))
if num % 2 == 0:
    print('This number is even')
else:
    print ('This number if odd')

#---------------------solution for b ------------------------------#

num  = float(input('input a number'))
if num > 0 :
    print('The number you entered is positive')
elif num < 0 :
    print('The number you enterd is negative')
else:
    print('This number is equal to zero')

'''4) Lists and Loops
a) Create a list of numbers from 1 to 10. Print each number in the list using a loop.
b) Write a Python program that takes a list of numbers as input and returns the sum of all the
numbers in the list.
c) Create a dictionary ‘colleague_name’ storing all your colleague names. Hint: Use sequence of
numbers as their key. '''

#---------------------solution for a ------------------------------#
my_list = [1, 2, 3, 4, 5, 5.5, 6, 7.8, 8, 9, 10]
for items in my_list:
    print(items, end='\n')

#---------------------solution for b------------------------------#


def list_sum():
    list_values = list(input('Please enter a sequence of number values'))
    sum = sum(list_values)
    return sum

print(list_sum())

#---------------------solution for c------------------------------#

my_dict = {
    0 :'samuel',
    1 : 'ella',
    2 : 'moses',
    3 : 'gbenro',
    4 : 'simz'
}

'''5) Functions
a) Write a Python function that takes three numbers as input and return their multiplication.
b) Write a Python function that takes a list of numbers as input and returns the average of all the
numbers in the list.'''

#---------------------solution for a ------------------------------#
def product(x, y, z):
    '''this is a function that takes
    three numbers as arguments and
    returns their product'''
    times = x * y * z

    return times

#---------------------solution for b ------------------------------#

def average(x = list(input('please enter a sequence of number values'))):
    '''this function calculates the
    average of all the values in a list
    which is entered an argument when 
    the functionm is being called'''
    sum = sum(x)
    length = len(x)
    avg = sum/length

'''6) Libraries and Modules
a) Install and Import the "math" module and use its "sqrt" function to calculate the square root
of a number.
b) Install and Import the "random" module and use its "randint" function to generate a random
number between 1 and 10.
c) Install and Import the "pywhatkit" module and use its "whatsapp" function to send a DM to
your tutor with the body “Good Day Sir” 
'''

#---------------------solution for a ------------------------------#
import math as mth

x = float(input('input a number'))
square_root = mth.sqrt(x)

print(f'the square root of {x} = (square_root)')

#---------------------solution for b ------------------------------#
import random as random
x = radom.randint(1,10)
print(x)

import pywhatkit as py

#---------------------solution for c ------------------------------#

py.sendwhatmsg_instantly(
    phone_no = 'mr habeeblah',
    message= 'Good day sir',
)

'''10) Give a feedback on this Python course, your instructor and this examination.'''
print(' I really enjoyed learning python with mr habeelah, because of the interactive and practical intensive nature of the class, \n what i enjoyed the most was actually my instructor\'s friendly nature and his willigness to keep on teaching until his students have a grasp of whatever he might be teaching\n \n i think this exam was a nice way to really assess the knowledge of the students on the basics of python')