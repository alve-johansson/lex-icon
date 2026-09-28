###########################################
#                                         #
#     B O O K I N G      S Y S T E M      #
#                                         #
###########################################

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

    def price(self):
        weekend_tax = 1.25
        if weekend:
            self.price = self.price * weekend_tax
        return self.price


class TimeState

class BaseRoom(Room):
    def __init__(self, number, beds=2, price=800):
        super().__init__(number, beds, price)

class RedRum(Room):
    def __init__(self, number, beds=2, price=800):
        super().__init__(number, beds, price)


class Penthouse(Room):
    def __init__(self, number, beds=4, price=2500):
        super().__init__(number, beds, price)
        self.has_jacuzzi = True


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Staff:
    def __init__(self, name):
        self.name = name

    def clean_room(self, room):
        room.cleaned = True
        print(f"Staff {self.name} cleaned room {room.number}.")

bookable_rooms = [
    BaseRoom(number=101, beds = 2, price = 750),
    BaseRoom(number=102),
    BaseRoom(number=103),
    BaseRoom(number=104),
    BaseRoom(number=105),
    BaseRoom(number=106),
    BaseRoom(number=107),
    BaseRoom(number=108),
    Penthouse(number=501),
    Penthouse(number=601)
]


############################################
#
#    T E R M I NA L    I NT E R FA CE
#
###########################################
print("#----------------------------------#\n"
      "#  Welcome to the booking program! #\n"
      "#----------------------------------#\n")

menu_active = True

while menu_active:
    print("\n-- MENU --\n"
          "---------------\n"
          "1. SEE AVAILABLE ROOMS\n"
          "2. BOOK ROOM\n"
          "3. EXIT PROGRAM\n")
    
    menu_choice = input("Choice: ")

    if menu_choice == "1":
        print("\n--- Available Rooms ---")
        for room in bookable_rooms:
            if not room.occupied and room.cleaned:
                print(room)
                
    elif menu_choice == "2":
        room_num = input("Enter room number to book: ")
        found_room = None
        for room in bookable_rooms:
            if str(room.number) == room_num:
                found_room = room
                break
        
        if found_room:
            if found_room.occupied:
                print("Room is already occupied!")
            else:
                name = input("Enter customer name: ")
                found_room.occupied = True
                print(f"Room {found_room.number} booked for {name}.")
        else:
            print("Room is not found.")

    elif menu_choice == "3":
        print("Exiting... Bye bye!")
        menu_active = False
    else:
        print("Input out of range, sorry, try again.")