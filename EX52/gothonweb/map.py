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

# Create the scenes of the game
wake_up_scene = Scene("Where am I", "wake_up_scene",
"""
When you wake up, you find youself in a
weird forest
You cannot remember how you get there
The pain in your hand makes you feel unwell
It is too quite
You can only hear the wind wailed between distorted trunks.
""")

bag_code_scene = Scene("You found something", "bag_code_scene",
"""
You walk around to find the way out
However, you are too hungry to walk
When you decide to take a rest
You find a bag on the ground
It seems that you can find some useful stuff inside the bag
You try to open the combination lock of the bag
The code is 3 digits.
""")

north_or_west_scene = Scene("Which side?", "north_or_west_scene",
"""
Lucky, the bag is opened
You Look inside the bag
There are chocolate, note and a pen
You eat all the chocolate while watching the note
The note indicates that you can choose to walk north or east
""")

escape_pod = Scene("Escape Pod", "escape_pod",
"""
You follow the map on the note
But there are one page missing
You don't really know which side you should go.
""")

the_end_winner = Scene("You Made It!", "the_end_winner",
"""
You see a village!
You made it!
""")

the_end_loser = Scene("...", "the_end_loser",
"""
You are trapped in the forest.
""")

generic_death = Scene("Death...", "death", "You died.")
# Define the action commands available in each scene
escape_pod.add_paths({
    'left': the_end_winner,
    '*': the_end_loser
})

north_or_west_scene.add_paths({
    'east': generic_death,
    'north': escape_pod
})

bag_code_scene.add_paths({
    '987': north_or_west_scene,
    '*': generic_death
})

wake_up_scene.add_paths({
    'rest':generic_death,
    'run':generic_death,
    'walk': bag_code_scene
})

# Make some useful variables to be used in the web application
SCENES = {
    wake_up_scene.urlname : wake_up_scene,
    bag_code_scene.urlname : bag_code_scene,
    north_or_west_scene.urlname : north_or_west_scene,
    escape_pod.urlname : escape_pod,
    the_end_winner.urlname : the_end_winner,
    the_end_loser.urlname : the_end_loser,
    generic_death.urlname : generic_death
}
START = wake_up_scene
