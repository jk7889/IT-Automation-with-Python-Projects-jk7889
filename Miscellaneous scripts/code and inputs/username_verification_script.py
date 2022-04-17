#!/usr/bin/env python3

import re


def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("Username must be a string")
    if type(minlen) == str and minlen.isdigit() is True:
        minlen = int(minlen)
    if minlen < 1:
        raise ValueError("Minimum length of username must be at least 1")

    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        return "Username: " + username + " has length shorter than the specified minimum length"

    # Usernames can only use letters, numbers, dots and underscores
    # Usernames can only begin with lower case letters
    if not re.match(r'^[a-z][a-z0-9_.]*$', username):
        return "Username: " + username + " has to start with a lowercase letter and cannot contain " \
                                         "any special character except dots and underscores"

    return "Username: " + username + " is valid"


if __name__ == "__main__":
    print(validate_user("hello", 7))
    print(validate_user("blue.kale", 3))
    print(validate_user(".blue.kale", 3))
    print(validate_user("red_quinoa", 4))
    print(validate_user("_red_quinoa", "4"))
    print(validate_user("12alpino.beast", 5))
    print(validate_user("@alpino.beast", 5))
    print(validate_user("#alpino.beast", 5))
    print(validate_user("$alpino.beast", 5))
    print(validate_user("a123lpino_beast", "5"))
    print(validate_user("AQ9775alpino_beast", 5))
    print(validate_user("bc9775alpino-beast", 5))
    print(validate_user("bc9775alpino@beast", 5))
    print(validate_user("", 1))
    print(validate_user("bc9775alpino.beast@", 5))
    print(validate_user("bc9775alpino.beas&t", 5))
    print(validate_user("shane.mickel", "7"))

    # The below three checks will raise exceptions as written in the code
    # print(validate_user("shane.mickel", 0))
    # print(validate_user(1234, "7"))
    # print(validate_user("shane.mickel", "hello"))
