rooms_capacity = {
    "room 1": 50,
    "room 2": 30,
    "room 3": 150,
    "room 4" : 0,
    "teams" : 9999
}

topics = {
    "computers", 
    "marxism", 
    "post-scarcity", 
    "gilles deleuze", 
    "adorno"
}



sessions = [
    {
        "session title": "Python fundamentals",
        "speaker": ("Heithem & Aladdin", "Lexicon"),
        "room": "teams",
        "max participants": rooms_capacity["teams"],
        "registered participants": {"alve", "heithem", "erik", "pelle", "skrrt", "skurt", "jord", "bajenpundare", "lifestalker"},
        "topic": "computers",
        "start time": ("09:00", 45)
    },
    {
        "session title": "Historisk materialism i digitala eror",
        "speaker": ("Karl M.", "GU"),
        "room": "room 1",
        "max participants": rooms_capacity["room 1"],
        "registered participants": {"alve", "cassandra", "thomas", "gilles"},
        "topic": "marxism",
        "start time": ("10:00", 60)
    },
    {
        "session title": "Post-Scarcity & Framtidens ekonomi",
        "speaker": ("K. Aaron", "Ekonomiinstitutet"),
        "room": "room 3",
        "max participants": rooms_capacity["room 3"],
        "registered participants": {"alve", "heithem", "brando", "jord", "ando"},
        "topic": "post-scarcity",
        "start time": ("11:15", 90)
    },
    {
        "session title": "Deleuze och Rizomatiska nätverk",
        "speaker": ("Felix G.", "Filosofiska Institutionen"),
        "room": "room 2",
        "max participants": rooms_capacity["room 2"],
        "registered participants": {"cassandra", "gilles", "per", "markus"},
        "topic": "gilles deleuze",
        "start time": ("13:00", 60)
    },
    {
        "session title": "Negativ dialektik och kulturindustrin",
        "speaker": ("Theodor A.", "Frankfurtskolan"),
        "room": "room 2",
        "max participants": rooms_capacity["room 2"],
        "registered participants": {"alve", "greger", "krille p"},
        "topic": "adorno",
        "start time": ("14:15", 45)
    },
    {
        "session title": "Avancerad Python & Datastrukturer",
        "speaker": ("Guido V.", "Python Foundation"),
        "room": "room 3",
        "max participants": rooms_capacity["room 3"],
        "registered participants": {"alve", "heithem", "erik", "pelle", "zalve", "galve"},
        "topic": "computers",
        "start time": ("15:15", 60)
    },
    {
        "session title": "Stängd workshop: Underhåll",
        "speaker": ("Tech Team", "Drift"),
        "room": "room 4",
        "max participants": rooms_capacity["room 4"],  # 0 platser
        "registered participants": set(),               # Tomt set
        "topic": "computers",
        "start time": ("16:30", 30)
    },
    {
        "session title": "Kritisk teori och nätverkskultur",
        "speaker": ("Mark F.", "Kulturstudier"),
        "room": "teams",
        "max participants": rooms_capacity["teams"],
        "registered participants": {"alve", "cassandra", "jord", "ando", "yalve"},
        "topic": "adorno",
        "start time": ("17:10", 45)
    }
]

#part 2
""" print(sessions[0]["start time"][0]) #first session, assuming it is in correct order?
#if not in correct order = sorted_sessions = sorted(sessions, key=lambda session: session["start time"][0])
print(sessions[2]["speaker"][0]) #third session, speaker
print(sessions[-1]["room"]) #room of last session
print(sessions[4]) #all information about one random session
print(sessions[-2]["start time"][1]) #nested information
print(sessions[:3]) #first three
print(sessions[-2:]) #last two
reverse_schedule = sessions[::-1] #reversed schedule
print(reverse_schedule)
copy_morning = sessions[:3] #copy of morning sessions schedule
print(copy_morning) """

#part 3
""" print(sessions[3])
sessions[3]["room"] = "room 4"
sessions[3]["max participants"] = rooms_capacity["room 4"]
print(sessions[3])

sessions[-3]["speaker"] = ("Linus Torvalds", "Linux foundation")
print(sessions[-3])

sessions += [{
            "session title": "Computers of the evening",
            "speaker": ("Marky Mark.", "Internetstiftelsen"),
            "room": "room 3",
            "max participants": rooms_capacity["room 3"],
            "registered participants": {"alve", "cassandra", "jord", "ando", "yalve"},
            "topic": "computers",
            "start time": ("18:00", 300)

}]


sessions[-1]["registered participants"].add("Andrés Julio Iglesias")
print(sessions[-1]["registered participants"])

removed_session = sessions.pop()
print("Raderad session:", removed_session)

print(f"Antal sessioner kvar: {len(sessions)}")
 """
""" removed_participant = sessions[-1]["registered participants"].remove("alve")
print(sessions[-1]["registered participants"])

sessions[0]["Difficulty"] = "Beginner"
print(sessions[0]) """

""" unique_topics = {session["topic"] for session in sessions}
print(unique_topics)


conference_info = [
    {"dates" : {"day 1" : 20260920, "day 2" : 20250921}}
]

conference_info += [  
    {"opening times" : {conference_info[0]["dates"]["day 1"] : "08:00", conference_info[0]["dates"]["day 2"] : "08:30"}},
    {"closing times" : {conference_info[0]["dates"]["day 1"] : "16:00", conference_info[0]["dates"]["day 2"] : "15:30"}}
]
for info in conference_info:
    print(info) """ 