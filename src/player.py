# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __str__(self):
        return f"{self.name} has enetered {self.location}"

    def move_to(self, direction, location):
        attribute = direction + '_to'

        if hasattr(location, attribute):
            return getattr(location, attribute)

        print("\nMovement isn't allowed \n")

        return location
