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
       

    #show item array



    #pickup item 
    #roomItems is an array


    #remove item

    def __repr__(self):
        return f'Player: {self.name}, Current Room: {self.current_room}' 
