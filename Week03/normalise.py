# This program reads in a string and strips any leading or trailing spaces
# It also converts all the lettersto lower case
# This program also outputs the lenght of the original string and normalises one
# Author Nikolay Sezonov

rawString = input ("Please input a string : ")
normalisedString = rawString. strip().lower()

lenghtOfRawString = len (rawString)
lenghtOfNormalised = len (normalisedString)

print ("That String normalised is : {} ".format (normalisedString))
print ("We reduced the input string from {} to {} charachters".format(lenghtOfRawString,lenghtOfNormalised))