from sys import exit
import mansion as mansion
import mansionupstairs
import redroom


class Scene(object):
    def enter(self):
        print "She found you..."
        exit(1)


class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


class Death(Scene):
    quips = [
        "Death comes with his scythe and cuts your soul into tiny pieces. RIP."
        "Better luck next time, buddy."
        "Mua ha ha ha ha"
    ]


def start():
    print "You wake up in the middle of the woods."
    print "The sky darkens and fear grips you."
    print "You have no memory of how you ended up here."
    print "You need to get home."
    print "You get up and a small light in the distance catches your eye."
    print "Do you go towards the light or do you decide to wait until help arrives?"

    action = raw_input("> ")

    if action == "go":
        print "You cautiously walk towards the little light."
        print "As you approach the light source, you see an old mansion in front of you."
        print "You suddenly hear a scream from within."
        mansion.Mansion().insertnamehere()

    elif action == "wait":
        print "Darkness approaches as you wait in the woods."
        print "You hear twigs snap nearby and start to rise in fear."
        print "Unable to see anything, you start to panic."
        print "Suddenly, you hear a whisper in your ear:"
        print """
                  I found you...
                  """
        return 'death'

    else:
        print "I told you to choose. Go or Wait. Now decide."
        return start()


class Mansion(Scene):
    def enter(self):
        print "You are scared. But you gather your shit together and approach"
        print "catiously."
        print "You tip-toe through the back door and sneak in."
        print "You hear footsteps upstairs and the sound of something being"
        print "dragged."
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




class MansionUpstairs(Scene):
    def enter(self):
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


class RedRoom(Scene):
    def enter(self):
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

        elif action == "apporach":
            print "You approach the cage and touch its metal bars."
            print "You go closer and peer inside because you can't really see."
            print "Suddenly, a pair of hands grab your head from within the cage."
            print "The hands bash your head against the cage until you die."
            return 'death'


class Finished(Scene):
    def enter(self):
        print "You escaped. Nicely done..."
        return 'finished'


class Map(object):
    scenes = {
        'death': Death(),
        'MansionUpstairs': MansionUpstairs(),
        'RedRoom': RedRoom(),
        'finished': Finished(),
        'mansion': Mansion(),

    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


start()
