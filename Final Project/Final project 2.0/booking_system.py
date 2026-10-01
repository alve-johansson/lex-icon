'''This file handles the logics and the storage of actual data'''

#imports
import models as m

weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
next_day_index = 2

days = {}
for i in range(1, 31):
    days[i] = {
        "weekday" : weekdays[(i-1) % 7],
        "booked_rooms": []
    }

def move_forward_one_day():
    global next_day_index
    
    for i in range(1, 30):
        days[i] = days[i + 1]

    days[30] = {
        "weekday": weekdays[next_day_index],
        "booked_rooms" : []
    }

    next_day_index = (next_day_index + 1) % 7 


#list of actual room objects in hotel
rooms = [
    m.HotelRoom(number=101, price=800, max_occupancy=2, booked_days= []),
    m.HotelRoom(number=102, price=800, max_occupancy=2, booked_days= []),
    m.HotelRoom(number=103, price=850, max_occupancy=2, booked_days= []),
    m.Suite(number=201, price=1800, max_occupancy=4, booked_days= []),
    m.Suite(number=202, price=2000, max_occupancy=4, booked_days= []),
    m.RedRum(number=666, price=6666, max_occupancy=1, booked_days= [])
]

#list of guests
guests = [
    m.Guest("Jack", "Torrance", "jack@overlook.com"),
    m.Guest("Wendy", "Torrance", "wendy@overlook.com"),
    m.Guest("Danny", "Torrance", "redrum@shining.com"),
    m.Guest("Dick", "Hallorann", "dick@hotelcalifornia.com"),
    m.Guest("Humbert", "Humbert", "humhum@uone.edu"),
    m.Guest("Dolores", "Haze"), #can Dolores be the "child" of Humbert?
    m.Guest("Micheal", "Houellebecq", "jouissance@sendmail.fr") #smoking alarm turned off after each visit, bottles of chablis everywhere    
]


#list of actual bookings in hotel
bookings = [
    ]

def book_room(guest, room, check_in, check_out): ## the book_room function uses guest room and check in and check out parameter
    if check_in >= check_out: #you cannot book from 3d day to 1st day.
        raise ValueError("Departure must be after arrival.")
    if check_in < 1 or check_out > 31: #in this system you cannot book more than 30 days in advance
        raise ValueError("Days must be between 1 and 30.")
    if not room.is_available(check_in, check_out): # if the room is unavailable. Should this really be a valueError thoug?
        raise ValueError(f"Room {room.number} is not available on those days.")

    for day in range(check_in, check_out):
        room.booked_days.append(day) ## add the days of the booking to booked days

    new_id = max([b.booking_id for b in bookings], default=0) + 1
    booking = m.Booking(new_id, guest, room, check_in, check_out)
    bookings.append(booking)
    return booking