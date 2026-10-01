#In this file: logics and the storage of actual data

#imports
import models as m

weekdays = ["Mon", "Tues", "Wen", "Thur", "Fri", "Sat", "Sun"]
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
    m.Booking(
        booking_id=3,
        guest=guests[2],
        room=rooms[2], # RedRum 666
        check_in_date=1,
        check_out_date=3
    ),
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

print(days[1])
move_forward_one_day()
print(days[1])
