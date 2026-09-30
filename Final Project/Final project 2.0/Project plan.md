MoSCoW

MUST HAVE:
X    OOP classes - Room, Customer, Booking, etc.
    Saved states of 30 day window.
    Validation for booking with ValueError
    Possibility for cancellation.
X    CLI menu
    short and fun README.md

SHOULD HAVE:
Bussiness statistics (total income from bookings?, percentage of )
"Graphical" 30-day matrix
weekend price

COULD HAVE:
Save/load from JSON
Added services ("continental breakfast")
More Room types

WON'T HAVE:
staff, cleaned/cleaning value/functions
"real" world monthly 12 month calendar
possibility to overbook.

1. First things first:
Add classes in models.py

CLASSES:
Room (Number, price, max_occupancy, booked_days(set))
method is_available

subclasses to Room: HotelRoom/Suite/redrum

Guest (first_name, last_name, email)

Booking: booking_id, guest, room, check_in_date, check_out_date

call them from main, make sure this works

2. logics and stuff
create the data [] rooms, and [] bookings

method: create booking check is_available and if dates is in range
else ValueError

method: cancel_booking
removes the booked day from the specific room

function generate mock data (customers, rooms)
function generate mock "month" being a list of days 1 - 30
give each "date" a weekday in correct order

this list of dates is the main database

day[1] = {
    "weekday": "monday"
    booked_rooms: [
    {"room" : 101, "booker" : "john smith"},
    {"room" : 104, "booker" : "john smith"},
    {"room" : 107, "booker" : "john smith"}
    ]
    }

rooms not booked day x is in some pseudo: "room in rooms not in booked_rooms"

once every three week it's monday all week. meme.

test if everything works