from room import Room
from player import Player
from item import Item

# Declare all the rooms

item = {
    'Flamberge':  Item("Flamberge",
                       "A large, serated sword."),

    'Peacemaker':    Item("Peacemaker", """A massive golden sword that brings respect and glory to the owner."""),

    'Phase Slicer': Item("Phase Slicer", """A foreign object that clearly is powerful."""),

    'Claymore':   Item("Claymore", """The trusty large sword perfect for action."""),

    'Broken Twig': Item("Broken Twig", """A whimpy twig. It almost broke just trying to pick it up"""),
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons.", item['Broken Twig']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", item['Claymore']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", item['Flamberge']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", item['Phase Slicer']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", item['Peacemaker']),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


player = Player("Warrior", room['outside'])


finished = False


while not finished:

    print(player.location)

    command = input("What do you want to do?")

    if command in ['n', 's', 'e', 'w']:
        player.location = player.move_to(command, player.location)

    if command == 'q':
        finished = True

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
