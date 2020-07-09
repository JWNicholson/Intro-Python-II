from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

#declare items


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Vik", room['outside'])
print(player)

# Write a loop that:
#
# * Prints the current room name
print(f"Current Room: {player.current_room.name}")

# * Prints the current description (the textwrap module might be useful here).
print(f"Description: {player.current_room.description}")
# * Waits for user input and decides what to do.
direction = input("Choose dirction to go - n(north), s(south), e(east), w(west), q to quit the game - ")

# If the user enters a cardinal direction, attempt to move to the room there.
def playerMove(direction):
    if direction =="n":
        # If there is no room to the north
        if player.current_room.n_to is None:
            # Print an error message if the movement isn't allowed.
            print("There's nothing in that direction.")
            print("==================================")
            print(player)
           
        else:
             player.current_room = player.current_room.n_to
             print(player)
             print("**************************************")

    elif direction =="s":
        # If there is no room to the north
        if player.current_room.s_to is None:
            # Print an error message if the movement isn't allowed.
            print("There's nothing in that direction.")
            print(player)
            print("==================================")
        else:
             player.current_room = player.current_room.s_to
             print("**************************************")

    elif direction =="e":
        if player.current_room.e_to is None:
           print("There's nothing in that direction.")
           print(player)
           print("==================================")
        else:
            player.current_room = player.current_room.e_to
            print(player)
            print("**************************************")

    elif direction =="w":
        if player.current_room.w_to is None:
            print("There's nothing in that direction.")
            print(player)
            print("==================================")
        else:
            player.current_room = player.current_room.w_to
            print(player)
            print("**************************************")
    
    elif direction == "q":
        print("Leaving so soon? Bye...")


playerMove(direction)
           

#
# If the user enters "q", quit the game.


