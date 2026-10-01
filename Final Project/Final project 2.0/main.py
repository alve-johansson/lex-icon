import models as m
import booking_system as b
import time

print(" #######################\n",
    "#     BOOKING MENU    #\n",
    "#######################\n",
    "PRESS 1. TO SEE AVAILABLE ROOM TYPES\n",
    "PRESS 2. TO SEE AVAILABLE DATES FOR ROOM TYPE\n",
    "PRESS 3. TO BOOK A ROOM\n",
    "PRESS 4. TO CANCEL A BOOKING\n",
    "PRESS 5. TO EXIT MENU\n")

while True:
    choice = input()

    if choice == "1":
        while True:
            print("We have three room types, which one are you intrested in?\n",
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
                "PRESS 3. TO BOOK REDRUM\n",
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
        print("AVAILABLE DATES FOR WHAT ROOM TYPE?"
            "PRESS 1. TO SEE THE BASIC ROOM\n",
            "PRESS 2. TO SEE THE SUITE\n",
            "PRESS 3. TO BOOK REDRUM\n",
            "PRESS 4. TO RETURN\n")
        room_availability = input()
        if room_availability == 1:
            pass #HERE THERE SHOULD BE A FUNCTION TO PASS ROOM TYPE AND THEN REQUESTED DATE
        if room_availability == 2:
            pass
        if room_availability == 3:
            pass
        if room_availability == 4:
            break 
    elif choice == "3": 
        print("BOOK A ROOM")
        name = input("NAME: ")
        room_number = int(input("ROOM NUMBER: "))
        arrival = int(input("ARRIVAL DAY: "))
        departure = int(input("DEPARTURE DAY: "))
        #actual #book_room(name, room_number, arrival, departure) function
    elif choice == "4": 
        print("CANCEL A BOOKING")
        name = input("NAME: ")
        room_number = int(input("ROOM NUMBER: "))
        arrival = int(input("ARRIVAL DAY: "))
        departure = int(input("DEPARTURE DAY: "))
        #actual #cancel_booking(name, room_number, arrival, departure) function
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