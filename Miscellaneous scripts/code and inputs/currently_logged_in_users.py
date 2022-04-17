#!/usr/bin/env python3

class Event:
    """Creating Event class and assigning values to class properties"""
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user

    def __str__(self):
        return "[{},{},{},{}]".format(self.date, self.type, self.machine, self.user)


def get_event_date(event):
    """To get an event's date"""
    return event.date


def check_user(machine, user):
    """To check if a user is currently logged into a machine"""
    for mach in machine.values():
        for x in mach:
            if x == user:
                return True
            else:
                return False


def current_users(events):
    """Takes a list of events, sorts it according to date & time
    and returns a dictionary of currently logged-in users """
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type != "logout" and event.type != "login":
            print("Unexpected Event: '"+event.type+"' for user: "+event.user)
        else:
            machines[event.machine].discard(event.user)
    return machines


def generate_report(machines):
    """Presents the results of a dictionary in a report like format"""
    print("Currently logged in users: ")
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))


if __name__ == "__main__":
    """Creates events list having Event class objects and preparing a report out of logged-in users out of it"""
    events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'login', 'mailserver.local', 'maya'),
    Event('2020-01-21 11:24:35', 'logout', 'mailserver.local', 'chris'),
    Event('2020-01-22 11:24:35', 'incorrect password for login', 'mailserver.local', 'chris'),
    ]

users = current_users(events)
# print(users)
generate_report(users)

