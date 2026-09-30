NY PROJEKTPLAN REWORK 2.0
bokningssytemet bör ha ett diakront element. 30 dagar framåt? klick klick klick. eller årets månader?  Nej det blir för rörigt.

städning staff, cleanfunktionen och cleanedstatus känns lite onödigt.

kanske kan vara om ett rum är bokat [X][X] och någon vill bokan dagen efter, får de en notis "CHECK IN 1100 after cleaning crew"
annars... "CHECK IN 0800". detta är verkligen inte viktigt.

menyn bör tänkas igenom mer ingående.

generera mock-up data med hjälp av ai eller skriv en funktion som slumpar fram? 

#room_type
room_type_id
name
description
max_occupancy
amenities


#room_type_rate
date
rate
room_type_id

#room
room_id
floor
number
is_available
room_type_id

#reservation
reservation_id
room_type_id
guest_id
start_date
end_date
status
room_count

#guest
guest_id
first_name
last_name
email

room_type_id | date | total inventory | booked |
1001         | 01-23|   50            | 44

overbooking? isf typ 5% minst 20 dagar fram? cancelling? ok

bygg system för att sen kunna kapa databas och koppla in JSON eller liknande.

OVAN STRUKTUR för komplex för litet dataprogram.
Enklare att hålla tre klasser istället för olika relationella
databasentiteter som ska ha unique id och så.

I programmet separerar vi ej RESERVE och BOOKED. I SÅ FALL görs detta i senare steg. 

OVERBOOKING tas bort det lägger till komplexitet som inte alls är nödvändig. men det är tänkvärt, undra hur stora hotell gör? misstänker hög overbooking långt fram i tiden och ingen alls nästa månad? eller?
