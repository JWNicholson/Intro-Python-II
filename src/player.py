# Write a class to hold player information, e.g. what room they are in
# currently.

# class Player
#constructor - self, name, current_location
#return player name and current_location
class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = []
       
    def __repr__(self):
        return f'Player: {self.name}, Current Room: {self.current_room}' 

#pick up item
    def get(self, item):
        if item == -1:
            print("So, you take nothing.")
            return
        else:
            self.inventory.append(self.current_room.itemsList[item])
            print("You pick up the item")

#drop item
    def drop(self, droppedItem):
        pass

# player movements (refactor and move here from adv.py)


     
