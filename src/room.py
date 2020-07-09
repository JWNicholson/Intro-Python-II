# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, roomItemsList=None):
        self.name = name
        self.description = description
        self.roomItemsList = []
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

    def onRoomChange(self):
        print("You are in - ", self.name)
        print("Description", self.description)
        print("In here, there is - ", self.roomItemsList)

    def addRoomItems(self, item):
        return self.roomItemsList.append(item)

    def __repr__(self):
        return (f"{self.name}, Description: {self.description}, Items: {self.roomItemsList}")