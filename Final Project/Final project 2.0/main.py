'''This is the main file, it handles input and output of the software'''



import models as m
import booking_system as b
import time

print(" #######################\n",
    "#     BOOKING MENU    #\n",
    "#######################\n",
    "PRESS 1. TO SEE AVAILABLE ROOM TYPES\n",
    "PRESS 2. TO SEE AVAILABLE ROOMS FOR DATES\n",
    "PRESS 3. TO BOOK A ROOM\n",
    "PRESS 4. TO CANCEL A BOOKING\n",
    "PRESS 5. TO EXIT MENU\n")

while True:
    choice = input()

    if choice == "1":
        while True:
            print("We have three room types, which one are you interested in?\n",
                  '''
Included in all room bookings is:
- Wireless internet
- Generous breakfast buffet with hot dishes
- Full fitness facilities, including both indoor and outdoor gyms and a wide range of group workout classes
- Hotel California's own luxury bathroom products
- Bathrobe (on loan) and slippers to take home
- Parking right next to the hotel\n''',
                "PRESS 1. TO SEE THE BASIC ROOM\n",
                "PRESS 2. TO SEE THE SUITE\n",
                "PRESS 3. TO SEE REDRUM\n",
                "PRESS 4. TO RETURN\n")
            room_choice = input()
            if room_choice == "1":
                print(f"THE BASIC ROOM: {m.HotelRoom.description}")
            elif room_choice == "2":
                print(f"THE SUITE: {m.Suite.description}")
            elif room_choice == "3":
                print(m.RedRum.description)
                for i in range(10):
                    print("\nREDRUM REDRUM REDRUM...\n")
                    time.sleep(0.5)
            elif room_choice == "4":
                break
            else:
                print("OUT OF RANGE")
    elif choice == "2":
        arrival_input = input("ARRIVAL DAY (1-30): ")
        departure_input = input("DEPARTURE DAY (1-30): ")

        approved_dates = []
        for i in range(1, 31):
            approved_dates.append(str(i))

        if arrival_input in approved_dates and departure_input in approved_dates:
            arrival = int(arrival_input)
            departure = int(departure_input)
        
            if arrival >= departure:
                print("\nDeparture day must be after arrival day.")
            else:
                available = b.get_available_rooms(arrival, departure)
                if available:
                    print(f"\nAVAILABLE ROOMS FOR DAYS {arrival} TO {departure}:")
                    for room in available:
                        print(f" - Room {room.number} ({type(room).__name__}) - {room.price} SEK/night")
                else:
                    print("\nNo rooms available for those dates.")
        else:
            print("\nError: Please enter valid day numbers (1-30).")

    elif choice == "3": 
        print("\nBOOK A ROOM")
        name = input("NAME: ").strip()
        if not name:
            print("\nError: Name cannot be empty.")
            continue
        room_input = input("ROOM NUMBER: ")
        arrival_input = input("ARRIVAL DAY (1-30): ")
        departure_input = input("DEPARTURE DAY (1-30): ")

        approved_dates = [str(i) for i in range(1, 31)]
        approved_rooms = [str(r.number) for r in b.rooms]

        if room_input in approved_rooms and arrival_input in approved_dates and departure_input in approved_dates:
            room_number = int(room_input)
            arrival = int(arrival_input)
            departure = int(departure_input)

            if arrival >= departure:
                print("\nError: Departure day must be after arrival day.")
            else:
                room = next((r for r in b.rooms if r.number == room_number), None)
                try:
                    guest = m.Guest(name, "")
                    booking = b.book_room(guest, room, arrival, departure)
                    print(f"\nBOOKING SUCCESSFUL! Booking ID: {booking.booking_id}")
                except ValueError as e:
                    print(f"\nError: {e}")
        else:
            print("\nError: Please enter valid numbers for room, arrival, and departure.")
    elif choice == "4": 
        print("\nCANCEL A BOOKING")
        try:
            booking_id = int(input("BOOKING ID: "))
            if b.cancel_booking(booking_id):
                print(f"Booking {booking_id} successfully cancelled.")
            else:
                print(f"No booking found with ID {booking_id}.")
        except ValueError:
            print("Please enter a valid numeric Booking ID.")
    elif choice == "5":
        print("\n\n Just kidding, you are not allowed leave. You are here forever. \n\n")
        time.sleep(1)
        print("\n\n Forever. \n\n")
        time.sleep(2)
        print("\n\n Forever and ever. \n\n")
        time.sleep(1)
        print("\n\n Forever? \n\n")
        time.sleep(2)
        print("\n\n Forever... \n\n")
        break
    else:
        print("OUT OF RANGE")