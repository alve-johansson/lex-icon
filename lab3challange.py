flight_data = {
    "DK-133769694201312": {
        "destination": "Heathrow, London",
        "departure time": 9.0,
        "gate": 4,
        "passangers": {"alve", "heithem", "salvador allende", "stafford beer", "strongbow", "bea uusma", "bilan osman"},
        "maximum capacity": 230,
        "delayed": 0.4,
        "cancelled": False
    },
    "SV-123456789012345": {
        "destination": "LAX, Los Angeles",
        "departure time": 14.5,
        "gate": 12,
        "passangers": {"alve", "heithem", "salvador allende", "stafford beer", "strongbow", "bea uusma", "bilan osman"},
        "maximum capacity": 230,
        "delayed": 0.5,
        "cancelled": False
    },
    "LH-987654321098765": {
        "destination": "BER, Berlin",
        "departure time": 7.25,
        "gate": 2,
        "passangers": {"rosa luxemburg", "karl liebknecht", "hannah arendt"},
        "maximum capacity": 180,
        "delayed": 0.0,
        "cancelled": False
    },
    "AF-555444333222111": {
        "destination": "CDG, Paris",
        "departure time": 11.0,
        "gate": 8,
        "passangers": {"michel foucault", "gilles deleuze", "simone de beauvoir", "jean-paul sartre"},
        "maximum capacity": 200,
        "delayed": 1.5,
        "cancelled": False
    },
    "BA-999888777666555": {
        "destination": "JFK, New York",
        "departure time": 16.0,
        "gate": 15,
        "passangers": {"mark fisher", "david graeber", "bell hooks"},
        "maximum capacity": 300,
        "delayed": 0.0,
        "cancelled": True
    },
    "SK-111222333444555": {
        "destination": "CPH, Köpenhamn",
        "departure time": 8.5,
        "gate": 1,
        "passangers": {"alve", "sören kierkegaard"},
        "maximum capacity": 150,
        "delayed": 0.0,
        "cancelled": False
    },
    "AY-777666555444333": {
        "destination": "HEL, Helsingfors",
        "departure time": 12.0,
        "gate": 6,
        "passangers": {"tove jansson", "eino leino"},
        "maximum capacity": 120,
        "delayed": 0.2,
        "cancelled": False
    },
    "KL-444555666777888": {
        "destination": "AMS, Amsterdam",
        "departure time": 13.75,
        "gate": 9,
        "passangers": {"baruch spinoza", "desiderius erasmus"},
        "maximum capacity": 190,
        "delayed": 2.0,
        "cancelled": False
    },
    "IB-222333444555666": {
        "destination": "MAD, Madrid",
        "departure time": 18.5,
        "gate": 5,
        "passangers": {"federico garcia lorca", "pablo picasso"},
        "maximum capacity": 210,
        "delayed": 0.0,
        "cancelled": False
    },
    "AZ-333444555666777": {
        "destination": "FCO, Rom",
        "departure time": 20.0,
        "gate": 11,
        "passangers": {"antonio gramsci", "umberto eco"},
        "maximum capacity": 180,
        "delayed": 0.0,
        "cancelled": True
    }
}
""" 
for e, (flight_code, flight_info) in enumerate(flight_data.items(), 1):
    print(f"{e}. {flight_code} - Avgång: {flight_info['departure time']} - Gate: {flight_info['gate']}")
 """
""" print(len(flight_data))
cancelled_flights = [flight for flight in flight_data if flight_data[flight]["cancelled"] == True]
print(len(cancelled_flights)) """

""" delayed_flights = [flight for flight in flight_data if flight_data[flight]["delayed"] > 0]
print(len(delayed_flights)) """

""" for flight in flight_data:
    x = flight_data[flight]["delayed"]
    if x > 1:
        print(f"{flight} - severly delayed")
    elif x > 0.33:
        print(f"{flight} - delayed")
    elif x > 0:
        print(f"{flight} - slight delay")
    else:
        print(f"{flight} - on time")

 """
""" daily_passangers = 0
for flight in flight_data:
    daily_passangers += len(flight_data[flight]["passangers"])

print(daily_passangers) """

""" daily_passangers = 0
flight_counter = 0
for flight in flight_data:
    daily_passangers += len(flight_data[flight]["passangers"])
    flight_counter += 1
print(daily_passangers/flight_counter) 
 """

# Hitta flygningen med flest passagerare direkt via max()
top_flight_code = max(flight_data, key=lambda f: len(flight_data[f]["passangers"]))
top_flight_info = flight_data[top_flight_code]

print(f"Flyg med flest passagerare: {top_flight_code} -> {top_flight_info}")
