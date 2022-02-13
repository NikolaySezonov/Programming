# Program to read in two numbers and outputs the integer answer and remainder
# Author: Nikolay Sezonov
 
x = int(input('Enter first number, please : '))
y = int(input('Enter the number you want to divide by: '))

result = int(x / y)
remainder = int(x -(result*y)) # Did't know the % formula, so just input the different formula

print('{} devided by {} is equals {} with remainder {}' .format(x,y,result,remainder))