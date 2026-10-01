'''This file handles the logics and the storage of actual data'''

#imports
import models as m


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
    m.Guest("Dolores", "Haze"), # Thought: can Dolores be the "child" of Humbert?
    m.Guest("Micheal", "Houellebecq", "jouissance@sendmail.fr") # smoking alarm turned off after each visit, bottles of chablis everywhere    
]

#list of actual bookings in hotel
bookings = [
    ]

def book_room(guest, room, check_in, check_out):
    '''Books a room for the nights from check_in up to (not including) check_out.
    Raises ValueError if the dates are invalid or the room is already taken.
    Updates both the room's booked_days and the bookings list.'''
    if check_in >= check_out: # you cannot book from 3rd day to 1st day.
        raise ValueError("Departure must be after arrival.")
    if check_in < 1 or check_out > 31: # in this system the window is for 30 days in advance
        raise ValueError("Days must be between 1 and 30.")
    if not room.is_available(check_in, check_out):
        raise ValueError(f"Room {room.number} is not available on those days.")

    for day in range(check_in, check_out):
        room.booked_days.append(day) # add the days of the booking to booked days

    # highest existing id + 1 (starts at 1 if there are no bookings).
    new_id = max([b.booking_id for b in bookings], default=0) + 1
    booking = m.Booking(new_id, guest, room, check_in, check_out)
    bookings.append(booking)
    return booking

def cancel_booking(booking_id):
    '''Cancels the booking with the given id and frees its nights.
    Returns True if a booking was removed, False if the id does not exist.'''
    for b in bookings: # if it is booked. 
        if b.booking_id == booking_id: 
            for day in range(b.check_in_date, b.check_out_date):
                if day in b.room.booked_days:
                    b.room.booked_days.remove(day)
            bookings.remove(b)
            return True
    return False

'''Returns a list of all rooms that are free for every night in the period.'''
def get_available_rooms(check_in, check_out):
    return [r for r in rooms if r.is_available(check_in, check_out)]


# Starting data so there is something to demo (rooms 101, 201, 666).
book_room(guests[0], rooms[0], 1, 5)
book_room(guests[1], rooms[3], 10, 15)
book_room(guests[2], rooms[5], 20, 30)