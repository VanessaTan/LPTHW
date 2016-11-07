#importing agrv (a feature) from sys (a package)
from sys import argv

#using argv to get a filename
script, filename = argv

#Makes a file object with open command
txt = open(filename)

#prints a message with set variable filename
print "Here's your file %r:" % filename
#putting a function (read) on txt - commands given to a file by using period
print txt.read()

#prints a message
print "Type the filename again:"
#sets variable that makes you type in the file name manually
file_again = raw_input("> ")

#sets the variable
txt_again = open(file_again)

#prints txt and command 
print txt_again.read()
