#In this file: logics and the storage of actual data

#imports
import models as m


#storage needed: rooms and bookings

#list of actual room objects in hotel
rooms = [
    m.HotelRoom(number=101, price=800, max_occupancy=2),
    m.HotelRoom(number=102, price=800, max_occupancy=2),
    m.HotelRoom(number=103, price=850, max_occupancy=2),
    m.Suite(number=201, price=1800, max_occupancy=4),
    m.Suite(number=202, price=2000, max_occupancy=4),
    m.RedRum(number=666, price=6666, max_occupancy=1)
]

#list of guests
guests = [
    m.Guest("Jack", "Torrance", "jack@overlook.com"),
    m.Guest("Wendy", "Torrance", "wendy@overlook.com"),
    m.Guest("Danny", "Torrance", "redrum@shining.com"),
    m.Guest("Dick", "Hallorann", "dick@hotelcalifornia.com"),
    m.Guest("Humbert", "Humbert", "humhum@uone.edu"),
    m.Guest("Dolores", "Haze")
]


#list of actual bookings in hotel
bookings = [
    m.Booking(
        booking_id=1,
        guest=guests[0],
        room=rooms[0], # Rum 101
        check_in_date=1,
        check_out_date=5
    ),
    m.Booking(
        booking_id=2,
        guest=guests[1],
        room=rooms[3], # Suite 201
        check_in_date=10,
        check_out_date=15
    ),
    m.Booking(
        booking_id=3,
        guest=guests[2],
        room=rooms[5], # RedRum 666
        check_in_date=20,
        check_out_date=30
    )
]