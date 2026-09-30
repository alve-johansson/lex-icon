MoSCoW
MUST HAVE:
OOP classes - Room, Customer, Booking, etc.
Saved states of 30 day window.
Validation for booking with ValueError
Possibility for cancellation.
CLI menu
short and fun README.md

SHOULD HAVE:
Bussiness statistics
"Graphical" 30-day matrix

COULD HAVE:
Save/load from JSON
Added services ("continental breakfast")
More Room types

WON'T HAVE:
staff, cleaned/cleaning value/functions
"real" world monthly 12 month calendar
possibility to overbook.

First things first:
Add classes in models.py
call them from main, make sure this works
CLASSES:
Room (Number, price, max_occupancy, booked_days(set))
method is_available

subclasses to Room: HotelRoom/Suite

Guest (first_name, last_name, email)

Booking: booking_id, guest, room, check_in_date, check_out_date