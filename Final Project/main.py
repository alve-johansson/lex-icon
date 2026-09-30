###########################################
#                                         #
#     B O O K I N G      S Y S T E M      #
#                                         #
###########################################

'''Imports from other files:'''
import classes
from storage import bookable_rooms

###########################################
#
#   T E R M I N A L    I N T E R F A C E
#
###########################################

'''Menu logics'''
print(
    "#----------------------------------#\n"
    "#  Welcome to the booking program! #\n"
    "#----------------------------------#\n"
      )

menu_active = True

while menu_active:
    print("\n-- MENU --\n"
          "---------------\n"
          "1. SEE AVAILABLE ROOM TYPES\n"
          "2. BOOK ROOM\n"
          "3. EXIT PROGRAM\n")
    
    menu_choice = input("Choice: ")

    if menu_choice == "1":
        print("\n--- Available Rooms Types ---") #THIS SHOULD BE CHANGED INTO DISPLAYING ROOM TYPES. 
                                           #I THINK THIS IS HOW MANY HOTELS DOES. 
                                           #I'VE LOOKED AT A FEW SMALL LOCAL ONES.
        for room in bookable_rooms:
            if not room.occupied and room.cleaned:
                print(room)
    
        
    elif menu_choice == "2":
        room_num = input("Enter room number to book: ") ## CHANGE TOO ROOM TYPE
        see_available_dates = int(input("press 1 to see dates this month"))
        if see_available_dates == 1: 
            print("MON, TUE, WEN, THUR, FRI, SAT, SUN")   ## ALL THIS SHOULD BE MOVED TO NEXT CATEGORY
            for day in range(1, 31):
                if day % 7 != 0:
                    #something somthing if room is occupied day x
                    #print("[XX]")
                    #else
                    print("[  ],", end = "")
                elif day % 7 == 0:
                    print("[  ]")

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