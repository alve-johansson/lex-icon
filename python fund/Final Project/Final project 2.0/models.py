'''In this file, classes and methods are defined'''

class Room:
    '''This is the parent Room class. Kepps track of price occupancy and booked nights'''
    # booked_days defaults to None, not [], so every room gets its own list.
    # A default [] would be shared between all rooms.
    def __init__(self, number, price, max_occupancy, booked_days=None):
        self.number = number
        self.price = price
        self.max_occupancy = max_occupancy # Not really used :() for later future USEAGE
        self.booked_days = booked_days if booked_days is not None else []

    def is_available(self, check_in, check_out):
        #Checks every NIGHT in booking. CHECK OUT date does not count as NIGHT.
        for day in range(check_in, check_out):
            if day in self.booked_days:
                return False
        return True

class HotelRoom(Room):
    '''The HotelRoom is a subclass of Room and is the "basic" room of the hotel.
      Most hotels have different types of rooms, amenities could be added as a paraneter'''
    
    description = '''\nAt Hotel California, there is something for everyone, and our basic rooms are no exception.
They feature light-toned interiors, a well-thought-out design throughout, and views overlooking the heart of the hotel: the atrium courtyard and Bula Bar & Mat. 
The perfect room for those who appreciate simplicity combined with a touch of finesse!
\n'''
    def __init__(self, number, price, max_occupancy, booked_days):
        super().__init__(number, price, max_occupancy, booked_days)
        self.has_jacuzzi = False

class Suite(Room):
    '''The Suite is a subclass of Room and is the more expensive room of the hotel.
      Most hotels have different types of rooms, amenities could be added as a paraneter'''
    
    description = '''\nMore of everything. Like our basic rooms, these rooms feature modern, comfortable décor, but with a few extra square meters for added spaciousness. 
They offer comfortable king size beds with premium linen in egyptian cotton and more upscale furnishings and materials. You can also step out and enjoy your very own terrace with a view of the New Haven skyline. 
A room with that little bit of extra.
'''

    def __init__(self, number, price, max_occupancy, booked_days):
        super().__init__(number, price, max_occupancy, booked_days)
        self.has_jacuzzi = True

class RedRum(Room):
    '''Easter egg'''
    
    description = '''\n
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⣌⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠄⠹⡀⣆⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠄⠀⢡⡀⢯⠀⢠⠂⢀⠀⢀⡆⠀⢀⠑⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠒⠲⡄⠀⢛⢷⢌⣐⠘⠀⡄⠂⢘⢀⢿⠠⡐⠀⠐⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢨⣦⣄⠁⢡⡿⣌⠻⡌⡆⢀⡾⠁⢥⠘⡏⣧⡔⣧⡘⣤⠀⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⣀⠆⠘⠛⠚⠿⣼⣿⣿⣆⣈⣾⣾⢄⣜⣿⣿⣿⠛⠉⠀⠀⢌⠻⣇⢈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⢦⠊⡀⠀⠀⠀⠀⡌⣿⣿⣿⣶⣿⣿⣿⣾⣿⣿⢡⠆⠀⠀⠀⠀⠇⣈⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣧⣃⣀⣀⣀⣀⣀⣠⣧⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣶⣶⣶⣶⣾⣾⣿⣧⡯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⡔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⢙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣞⠛⠛⢿⣿⣟⡛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⡟⠉⠉⠉⠉⣉⡉⣉⣀⡉⣑⣃⣁⣤⣭⣀⢄⣤⣤⣥⠀⠉⠀⠉⢈⣽⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⣄⠀⠀⠀⡛⠋⠽⣿⡿⠿⠿⠿⠿⠿⠽⠟⠋⠈⡁⠀⠀⢀⣶⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣷⣦⡈⠛⠾⣷⣤⣤⣤⣤⣄⣤⢠⣄⣠⣾⠏⠋⣠⣶⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣶⣄⢈⠁⠙⠿⠛⠷⠿⠼⠛⠉⢁⣤⣶⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣷⣬⣳⢶⣦⣶⣤⣬⣶⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣶⣉⣻⣻⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠙⠉⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\n'''

    def __init__(self, number, price, max_occupancy, booked_days):
        super().__init__(number, price, max_occupancy, booked_days)
        self.has_jacuzzi = True

class Guest:
    '''A person who books a room.'''
    def __init__(self, first_name, last_name, email=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

class Booking:
    '''Connects a Guest with a Room for a period. Has a Guest and a Room [HAS-A].'''    
    def __init__(self, booking_id, guest, room, check_in_date, check_out_date):
        self.booking_id = booking_id
        self.guest = guest
        self.room = room 
        self.check_in_date = check_in_date 
        self.check_out_date = check_out_date
        self.days = check_out_date - check_in_date