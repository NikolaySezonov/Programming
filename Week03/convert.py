# This program will will show an absolute amount in cents
# Author: Nikolay Sezonov

number = float(input("Please enter an amount: "))
absoluteValue = abs(float(number))
conversion = absoluteValue * 100

print('The amount in cents is : {}'. format(conversion))