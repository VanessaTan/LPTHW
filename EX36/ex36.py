from sys import exit

def start():
    print "You wake up in a dark room."
    print "There is a door but it is locked."
    print "Do you pick the lock or break the lock?"

    choice = raw_input("> ")

    if "pick" in choice:
        zombie_room()
    elif "break" in choice:
        print "Something hears you."
        print "It's coming..."
        print "It catches you and tears your head off. Hurray!"

def zombie_room():
    print "You enter another room."
    print "You see a body of a man on the floor."
    print "Do you go over or run away?"

    choice = raw_input("> ")

    if "go" in choice:
        print "The man turns and tears your flesh from your body piece by piece. Hurray!"
    elif "run" in choice:
        red_room()

def red_room():
    print """
    You enter a red room.
    You see a pink and a blue potion.
    Do you drink the pink or the blue potion or perhaps neither?
    """

    choice = raw_input("> ")

    if "pink" in choice:
        print "Your body dissolves from the inside out and you turn into dust. Hurray!"
    elif "blue" in choice:
        print "You gain weight and explode. Hurray!"
    elif "neither" in choice:
        crystal_room()

def crystal_room():
    print "You go past the red room into a room full of crystals."
    print "How many crystals do you want to take?"

    choice = raw_input("> ")

    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        print "Before you could take any crystals, the crystal keeper chases you out."
        science_lab()
    if how_much < 50:
        print "The crystal keeper does not sense your presence and you leave with joy and riches. Hurray!"
    else:
        print "The crystal keeper awakens and impales you with his crystal staff. Hurray!"

def science_lab():
    print "You run into a science lab and see an exit."
    print "The code to the door is a simple equation. If you solve it then you may go free, if not, you will perish."
    print "Do you want to solve it?"

    choice = raw_input("> ")

    if "yes" in choice:
        print "not (100 != 0 and 3 == 3) Is the equation True or False?"
        choice = raw_input("> ")

        if "True" in choice:
            print "You are wrong. A trap door opens beneath you and you fall to the bottom where you are impaled by sharp poles. Hurray!"
            exit(0)
        if "False" in choice:
            print "Correct! You open the door and leap to your freedom! Hurray!"
            exit(0)
    if "no" in choice:
        print "The crystal keeper catches you and turns you into a crystal statue. Hurray!"
        exit(0)
start()
