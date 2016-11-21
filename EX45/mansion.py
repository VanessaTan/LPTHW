class Scene(object):
    def enter(self):
        print "She found you..."
        exit(1)
        
import mansionupstairs

class Mansion(Scene):
    def __init__(self):
        super(Mansion, self).__init__()
        self.Mansion = Mansion

    def insertnamehere(self):
        print "You are scared. But you gather your shit together and approach catiously."
        print "You tip-toe through the back door and sneak in."
        print "You hear footsteps upstairs and the sound of something being dragged."
        print "You then hear someone rush down the stairs."
        print "Where do you hide?!?!"
        print "There's a closet or you can hide behind the door."

        action = raw_input("> ")

        if action == "closet":

            print "You rush in the closet as quietly as possible."
            print "You close the doors after you but leave a crack open."
            print "Through the crack, you see a monster walk past."
            print "You are scared shitless."
            print "You start breathing heavily."
            print "The monster suddenly turns his head towards your direction."
            print "She smiles and opens the closet door."
            print " 'I found you... ' "
            return 'death'

        elif action == "door":

            print "You rush behind the door."
            print "You hold your breath as you hear the footsteps stop nearby."
            print "You hear a female voice say 'I'll find you..."
            print "The footsteps stomp away outside."
            print "You emerge from hiding."
            mansionupstairs.MansionUpstairs().insertnamehere()
        else:
            print "Just choose between the door or closet. It's not that hard."
            mansion.Mansion().insertnamehere()
