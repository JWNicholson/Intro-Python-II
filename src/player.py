# Write a class to hold player information, e.g. what room they are in
# currently.

# class Player
#constructor - self, name, current_location
#return player name and current_location
class Player:
    def __init__(self, name, current_room, itemArr[]):
        self.name = name
        self.current_room = current_room
        self.itemArr = itemArr

    #show item array



    #pickup item


    #remove item

    def __repr__(self):
        return f'Player: {self.name}, Current Room: {self.current_room}' 
