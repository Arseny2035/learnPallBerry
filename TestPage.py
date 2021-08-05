import re
def to_camel_case(text):
    result = ''
    if len(text) > 0:
        result = text.title().replace('-', '').replace('_','')

    return print(result)


to_camel_case('the-stealth-warrior')
to_camel_case('A-B-C')
def get_event_date(event):
    return event.date

def current_users(events):
    events.sort(key=get_event_date)
    mashines = {}
    for event in events:
        if event.mashine not in mashines:
            mashines[event.mashine] = set()
        if event.type == "login":
            mashines[event.mashine].add(event.user)
        elif event.type == "logout":
            mashines[event.mashine].remove(event.user)
    return mashines

def generate_report(mashines):
    for mashine, users in mashines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(mashine, user_list))

class Event:
    def __init__(self, event_date, event_type, mashine_name, user):
        self.date = event_date
        self.type = event_type
        self.mashine = mashine_name
        self.user = user

