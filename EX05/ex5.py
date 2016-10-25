Name = 'Zed A. Shaw'
Age = 35 # not a lie
Height = 74 # inches
Weight = 180 # lbs
Eyes = 'Blue'
Teeth = 'White'
Hair = 'Brown'
Centimeters = 74 / 0.39370
Kilograms = 180 * 0.453592

print "Let's talk about %s." % Name
print "He's %d inches tall." % Height
print "He's %d pounds heavy." % Weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (Eyes, Hair)
print "His teeth are usually %s depending on the coffee." % Teeth
print "He's %d kilograms heavy." % Kilograms
print "He's %d centimeters tall." % Centimeters

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    Age, Height, Weight, Age + Height + Weight)
