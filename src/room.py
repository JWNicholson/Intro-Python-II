# Implement a class to hold room information. This should have name and
# description attributes.

# class Room
# constructor self, name, description
# set n, e, s, w to null
#return name and description

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __repr__(self):
        return f'Name: {self.name}, Description: {self.description}'