#!/usr/bin/env python3
import os
import sys
import emails


def sender(filename):
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    message = emails.generate(sender, receiver, "Script", "This script", filename)
    emails.send(message)


def main():
    res = sys.argv[1]
    sender(res)


main()
