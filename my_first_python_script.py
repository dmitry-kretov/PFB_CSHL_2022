#!/usr/bin/env python3 #this line is always needed to open python3
import sys

#Print my name
my_name = 'Dmitry'
print('My name', my_name)

#Print my favorite color
my_color = 'moss green'
print ('My favorite color:', my_color)

#Print my favorite activity
my_activity = 'Baking an apple pie'
print('My favorite activity:', my_activity)

#Print my favorite animal
my_animal = 'Deer'
print ('My favorite animal:', my_animal)

# this argument allows script to be more general. You can provide the argument from the terminal and do not need to precise it in the script. when you run this script it will require to provide the varibles -- python3 (is not a sys arg), file.py (argv 0), [1], [2] etc..
name = sys.argv[1]
color = sys.argv[2]
activity = sys.argv[3]
animal = sys.argv[4]
print(name,'+',color,'+',activity,'+',animal) 
