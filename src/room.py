# Implement a class to hold room information. This should have name and
# description attributes.

# class Room
# constructor self, name, description
# set n, e, s, w to null
#return name and description

class Room:
    def __init__(self, name, description, roomItems = []):
        self.name = name
        self.description = description
        self.roomItems = []
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None


#show room item(s)
    def onNewRoom(self):
    #feedback
        print("You are in ", self.name)
        print ("Description")
        print("Items in this room: ", self.roomItems)


#add items to list
    def addItems(self, item):
        return self.roomItems.append(item)



    def __repr__(self):
        return f'{self.name}, Description: {self.description}, Items: {self.roomItems}'