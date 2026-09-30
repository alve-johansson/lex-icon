import models as m

#menu = 1
#while menu == 1:
#    print("     BOOKING MENU ----\n",
#        "   ___________________\n",
#        "PRESS 1. TO SEE AVAILABLE ROOM TYPES\n",
#        "PRESS 2. TO SEE AVAILABLE DATES FOR ROOM TYPE\n",
#        "PRESS 3. TO BOOK ROOM\n",
#        "PRESS 4. TO CANCEL BOOKING\n",
#        "PRESS 5. TO EXIT MENU\n")
#    menu = int(input())

objet_petit_a = m.Room(101, 900, 2, 2)
print(m.Room.price(objet_petit_a))