# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, item):
        self.name = name
        self.description = description
        self.item = item

    def __str__(self):
        return f"{self.name}: {self.description} {self.item}]"


# class Item(Room):
#     def __init__(self, name, description, item):
#         super().__init__(name, description)
#         self.item = item

#     def __str__(self):
#         print(f"There is a {self.item} in this room")
