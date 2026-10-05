class Room:
    def __init__(self, number, beds, price):
        self.number = number
        self.beds = beds
        self.price = price
        self.cleaned = True
        self.occupied = False

    def __str__(self):
        status = "Occupied" if self.occupied == True else "Available"
        clean_status = "Clean" if self.cleaned == True else "Needs cleaning"
        return f"Room {self.number} ({self.__class__.__name__}) - {self.beds} beds - {self.price} SEK [{status}, {clean_status}]"

class BaseRoom(Room):
    def __init__(self, number, beds=2, price=800):
        super().__init__(number, beds, price)


class PentHouse(Room):
    def __init__(self, number, beds=4, price=2500):
        super().__init__(number, beds, price)



class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email