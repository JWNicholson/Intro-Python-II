
# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room, inventory=None):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def __repr__(self):
        return f'Name: {self.name}, Current_Room: {self.current_room}, Inventory: {self.inventory}'

    def take(self, item):
        if item == -1:
            print("You didn't pick anything up")
            return
        else:
            self.inventory.append(self.current_room.roomItemsList[item])
            print("You picked it up")

    def drop(self, itemDrop):
        if itemDrop == -1:
            print("So, you don't to drop anything")
            return
        else:
            self.inventory.remove(self.inventory[itemDrop])
            print("You dropped an item")

    def movePlayer(self, direction):
        moveCommands = ["n", "e", "s", "w", "q"]
        try:
            moveCommands.index(direction)
            if(direction == "q"):
                quit()

            theRoom = getattr(self.current_room, direction + "_to")

            if(theRoom):
                self.current_room = theRoom
            else:
                print("There is nothing in that direction.")
            print("\n")
            self.current_room.onRoomChange()

        except:
            print("error")
            return

###################################

# If the user enters a cardinal direction, attempt to move to the room there.
# def playerMove(direction):
#     if direction =="n":
#         # If there is no room to the north
#         if player.current_room.n_to is None:
#             # Print an error message if the movement isn't allowed.
#             print("There's nothing in that direction.")
#             print("==================================")
#             print(player)
           
#         else:
#              player.current_room = player.current_room.n_to
#              print(player)
#              print("**************************************")

#     elif direction =="s":
#         # If there is no room to the north
#         if player.current_room.s_to is None:
#             # Print an error message if the movement isn't allowed.
#             print("There's nothing in that direction.")
#             print(player)
#             print("==================================")
#         else:
#              player.current_room = player.current_room.s_to
#              print("**************************************")

#     elif direction =="e":
#         if player.current_room.e_to is None:
#            print("There's nothing in that direction.")
#            print(player)
#            print("==================================")
#         else:
#             player.current_room = player.current_room.e_to
#             print(player)
#             print("**************************************")

#     elif direction =="w":
#         if player.current_room.w_to is None:
#             print("There's nothing in that direction.")
#             print(player)
#             print("==================================")
#         else:
#             player.current_room = player.current_room.w_to
#             print(player)
#             print("**************************************")
    
#     elif direction == "q":
#         print("Leaving so soon? Bye...")


# playerMove(direction)
           
     
