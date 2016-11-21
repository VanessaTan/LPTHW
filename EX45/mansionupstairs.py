class Scene(object):
    def enter(self):
        print "She found you..."
        exit(1)

import redroom

class MansionUpstairs(Scene):
    def __init__(self):
        super(MansionUpstairs, self).__init__()
        self.MansionUpstairs = MansionUpstairs


    def insertnamehere(self):
        print "You see blood everywhere."
        print "You see bloody footsteps lead outside."
        print "You also see a bloody trail lead upstairs."
        print "You calm yourself down and rush upstairs."
        print "You enter a long corridor and see a red door at the end."
        print "Do you enter the red room? Or run away?"

        action = raw_input("> ")

        if action == "enter":
            print "You hear footsteps downstairs and rush in the red room."
            print "You lock the door behind you."
            redroom.RedRoom().insertnamehere()

        elif action == "run":
            print "You thought about how insane you were to even come upstairs in the first place."
            print "You run downstairs, right into the monster."
            print "With her bloody lips, she kisses you and drains your life."
            return 'death'

        else:
            print "Can you just choose? Enter or Run."
            mansionupstairs.MansionUpstairs().insertnamehere()
