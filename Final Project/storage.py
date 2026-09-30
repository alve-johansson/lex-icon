#The point of seperating storage is not just to clean up main, but also to have a clear architecture if one would want to "plug in" another database.

from classes import BaseRoom, PentHouse
import random


bookable_rooms = [
    BaseRoom(number=101, beds = 2, price = 750),
    BaseRoom(number=102),
    BaseRoom(number=103),
    BaseRoom(number=104),
    BaseRoom(number=105),
    BaseRoom(number=106),
    BaseRoom(number=107),
    BaseRoom(number=108),
    PentHouse(number=501),
    PentHouse(number=601)
]

customers = [

]
