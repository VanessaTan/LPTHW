people = 30
cars = 40
trucks = 15

#if cars are greater than people then print line 7
if cars > people:
    print "We should take the cars."
# else if cars are less than people, print line 10
elif cars < people:
    print "We should not take the cars."
#else if neither statements are true, if cars == people, print line 13
else:
    print "We can't decide."

if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."
