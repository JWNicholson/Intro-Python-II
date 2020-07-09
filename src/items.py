# class to create items for rooms
class Items:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return(f"Item - {self.name}. Description: {self.description}")
