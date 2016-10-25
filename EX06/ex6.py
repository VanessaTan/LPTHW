#Defining variable x and giving it a value of 10
x = "There are %d types of people." % 10
#Defining variable
binary = "binary"
#Defining variable
do_not = "don't"
#Defining variable y and within it, defining 2 more variables
y = "Those who know %s and those who %s." % (binary, do_not)

#python prints x
print x
#python prints y
print y

#string with variable x input
print "I said: %r." % x
#string with varaible y input
print "I also said: '%s'." % y

#Defining variable
hilarious = False
#Defining variable and giving it a meaning
joke_evaluation = "Isn't that joke so funny?! %r"

#combining 2 variables in one string
print joke_evaluation % hilarious

#Defining variable
w = "This is the left side of..."
#Defining variable
e = "a string with a right side."

#Combining 2 vairables in one string 
print w + e
