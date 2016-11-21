class Scene(object):
    def enter(self):
        print "She found you..."
        exit(1)

class RedRoom(Scene):
    def __init__(self):
        super(RedRoom, self).__init__()
        self.RedRoom = RedRoom

    def insertnamehere(self):
        print "You turn around and see a cage with a figure inside."
        print "You hear footsteps outside rushing towards you and then angry bangs on the door."
        print "You feel safe as you locked the door."
        print "Do you climb out the window or approach the cage?"

        action = raw_input("> ")

        if action == "climb":
            print "You climb down the house carefully and run away into the dawn."
            print "You look behind you and see a dark silhouette in the mansion window."
            print "You turn and run faster...."
            print "The End."
            exit(0)

        elif action == "approach":
            print "You approach the cage and touch its metal bars."
            print "You go closer and peer inside because you can't really see."
            print "Suddenly, a pair of hands grab your head from within the cage."
            print "The hands bash your head against the cage until you die."
            print "The End."
            exit(0)
