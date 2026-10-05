#LAB 5 PART E


#1
""" def log_event(event_type, *messages, **metadata):

    return {"event": event_type, "messages" : messages, "metadata" : metadata}
    
user = "alve"
user = user.encode()
x = "12 MB"

print(log_event("Error", 
                "HDD is full", 
                "could not save changes", 
                user_id = "795bf449-a492-4212-a535-197d962982e0", 
                user_id2 = user,
                disk_space = "0 MB"))
 """


#2 OCH 4
""" def calculate_order(customer, *prices, **options):
    return {"customer": customer, "prices":prices, "options": options}

print(calculate_order("Alve", 100, 200, shipping_fee = 100, discount = 0.3))
print(calculate_order("Alve", 100, discount = 0.3))
print(calculate_order("Alve", 100, 200,100, 200,100, 200,
                      100, 200,100, 200,100, 200,100, 200,100, 200,
                       100, 200,100, 200,100, 200,100, 200,
                        100, 200,100, 200,100, 200,100, 200,
                         100, 200,100, 200,100, 200,100, 200,
                          100, 200,100, 200,100, 200,100, 200,
                           100, 200,100, 200,100, 200,100, 200,
                             shipping_fee = 100, discount = 0.3))
 """


#3
""" 
Jag tänker att ett "create account"-formulär ofta har många kwargs, där det finns några
nödvändiga liksom några som inte är nödvändiga. I en databas lär detta sparas som keyword
variabler?

def create_user(username, email, age=18, **kwargs):
    user_profile = {
        "username": username,
        "email": email,
        "age": age,
        "extra_info": kwargs
    }
    return user_profile
      
"""