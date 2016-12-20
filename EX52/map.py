class Scene(object):
    def __init__(self, title, urlname, description):
        self.title = title
        self.urlname = urlname
        self.description = description
        self.paths = {}

    def go(self, direction):
        default_direction = None
        if '*' in self.paths.keys():
            default_direction = self.paths.get('*')
        return self.paths.get(direction, default_direction)

    def add_paths(self, paths):
        self.paths.update(paths)

#Create the scenes of the game
Woods_Scene = Scene("You're In The Woods", "Woods_Scene",
"""
You wake up in the middle of the woods.
The sky darkens and fear grips you.
You have no memory of how you ended up here.
You need to get home.
You get up and a small light in the distance catches your eye.
Do you GO towards the light or do you decide to WAIT until help arrives?
""")


Wait_Scene = Scene("You Wait...", "death",
"""
Darkness approaches as you wait in the woods.
You hear twigs snap nearby and start to rise in fear.
Unable to see anything, you start to panic.
Suddenly, you hear a whisper in your ear:
I found you...
She grabs you by the neck and bites into your skull.

""")

Mansion_Scene = Scene("You Approach the Mansion...", "Mansion_Scene",
"""
You are scared. But you gather your shit together and approach catiously.
You tip-toe through the back door and sneak in.
You hear footsteps upstairs and the sound of something being dragged.
You then hear someone rush down the stairs.
Where do you hide?!?!
There's a CLOSET or you can hide behind the DOOR.
""")

Closet_Scene = Scene("You're a Coward", "death",
"""
You rush in the closet as quietly as possible.
You close the doors after you but leave a crack open.
Through the crack, you see a monster walk past.
You are scared shitless.
You start breathing heavily.
The monster suddenly turns his head towards your direction.
She smiles and opens the closet door.
I found you...
She grabs you by the neck and bites into your skull.
""")

Mansion_Upstairs = Scene("You Go Upstairs...", "Mansion_Upstairs",
"""
You see blood everywhere.
You see bloody footsteps lead outside.
You also see a bloody trail lead upstairs.
You calm yourself down and rush upstairs.
You enter a long corridor and see a red door at the end.
Do you ENTER the red room? Or RUN away?
""")

Run_Scene = Scene("You're Running Away...", "death",
"""
You thought about how insane you were to even come upstairs in the first place.
You run downstairs, right into the monster.
With her bloody lips, she kisses you and drains your life.
""")

Red_Room = Scene("You Enter The Red Room...", "Red_Room",
"""
You turn around and see a cage with a figure inside.
You hear footsteps outside rushing towards you and then angry bangs on the door.
You feel safe as you locked the door.
Do you CLIMB out the window or APPROACH the cage?
""")

Approach_Scene = Scene("You Go Towards The Cage...", "death",
"""
You approach the cage and touch its metal bars.
You go closer and peer inside because you can't really see.
Suddenly, a pair of hands grab your head from within the cage.
The hands bash your head against the cage until you die.
""")

Climb_Scene = Scene("You Climb Out The Window...", "death",
"""
You climb down the house carefully and run away into the dawn.
You look behind you and see a dark silhouette in the mansion window.
You turn and run faster....
It is your victory.
The End.
""")


#Define the action commands available in each Scene
Red_Room.add_paths({
    'climb': Climb_Scene,
    'approach': Approach_Scene
})

Mansion_Upstairs.add_paths({
    'enter': Red_Room,
    'run': Run_Scene
})

Mansion_Scene.add_paths({
    'door': Mansion_Upstairs,
    'closet': Closet_Scene
})

Woods_Scene.add_paths({
    'go': Mansion_Scene,
    'wait': Wait_Scene

})

#Make some useful variables to be used in the web application
SCENES = {
    Woods_Scene.urlname : Woods_Scene,
    Mansion_Scene.urlname : Mansion_Scene,
    Mansion_Upstairs.urlname : Mansion_Upstairs,
    Red_Room.urlname : Red_Room,
    Wait_Scene.urlname : Wait_Scene,
    Closet_Scene.urlname : Closet_Scene,
    Run_Scene.urlname: Run_Scene,
    Climb_Scene.urlname : Climb_Scene,
    Approach_Scene.urlname: Approach_Scene

}
START = Woods_Scene
