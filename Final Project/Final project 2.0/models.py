#In this file, classes and methods

class Room:
    def __init__(self, number, price, max_occupancy, booked_days):
        self.number = number
        self.price = price
        self.max_occupancy = max_occupancy
        self.booked_days = booked_days
        
    def is_available(self):
        return "Hej"

    def price(self):
        weekend_tax = 1.25
        weekend = True
        if weekend:
            self.price = self.price * weekend_tax
        
        return self.price

class HotelRoom(Room):
    def __init__(self, number):
        super().__init__(number)
        self.has_jacuzzi = False
    pass

class Suite(Room):
    def __init__(self, number):
        super().__init__(number)
        self.has_jacuzzi = True
    pass

class RedRum(Room):
    def __init__(self, number):
        super().__init__(number)
        self.has_jacuzzi = True
        jacuzzi_description = "Filled with blood"

class Guest:
    def __init__(self, first_name, last_name, email):
        pass

class Booking:
    def __init__(self, booking_id, guest, room, check_in_date, check_out_date):
        self.booking_id = booking_id
        self.guest = guest
        self.room = room 
        self.check_in_date = check_in_date 
        self.check_out_date = check_out_date
        pass