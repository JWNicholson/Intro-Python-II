from room import Room
from player import Player
from items import Items

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons."),

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
items = {
    "knife": Items("knife", "USMC issue K-Bar"),
    "torch": Items("torch", "Puts light on the area"),
    "rope": Items("rope", "Use it to climb or rappel"),
    "coins": Items("coins", "Buy stuff or buy your way out of trouble"),
    "spellbook": Items("spell book", "You know what to do...")
}

# add items to rooms
room['outside'].addRoomItems('torch')
room['foyer'].addRoomItems('coins')
room['overlook'].addRoomItems('rope')
room['narrow'].addRoomItems('spellbook')
room['treasure'].addRoomItems('knife')

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
playerName = input("What should I call you? ")
player = Player(playerName, room['outside'])
#print(player)

# Write a loop that:
#
# * Prints the current room name
print(f"{playerName} is currently in {player.current_room.name}")

# * Prints the current description (the textwrap module might be useful here).
print(f"Description: {player.current_room.description}")
print(f"Items in this room: {player.current_room.roomItemsList}")

playerInventory = print(f"Inventory for you: {player.inventory}")

#  Waits for user input and decides what to do.
# direction = input("Choose dirction to go - n(north), s(south), e(east), w(west), q to quit the game - ")
#
# If the user enters "q", quit the game.

while True:
  
    itemDrop = input(
        "Do you want to drop an item from your inventory? enter 0 for NO, or the item number-1, 2,...etc ")
    player.drop(int(itemDrop)-1)
    item = input(
        "Do you want to take the item in this room? enter 0 for NO, or 1 for yes. ")
    player.take(int(item)-1)
    print(f"Inventory for you: {playerInventory}")
    direction = input(
        "Which way? enter n for n, s, e, w, or q to quit. ")
    player.movePlayer(direction)