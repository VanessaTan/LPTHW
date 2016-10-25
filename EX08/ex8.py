#Definded variable
formatter = "%r %r %r %r"

#printed contents of parenthesis
print formatter % (1, 2, 3, 4)
#printed contents of parenthesis
print formatter % ("one", "two", "three", "four")
#printed contents of parentesis
print formatter % (True, False, False, True)
#printed contents of parenthesis
print formatter % (formatter, formatter, formatter, formatter)
#printed contents of parenthesis in one single line
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
