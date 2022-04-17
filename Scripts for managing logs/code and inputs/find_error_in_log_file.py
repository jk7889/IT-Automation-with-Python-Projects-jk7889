#!/usr/bin/env python3
import sys
import os
import re


def error_search(log_file):
    """Returns all the lines in the log file containing the error we enter in input"""
    error = input("What is the error? ")
    errors_returned = []
    with open(log_file, mode='r', encoding='UTF-8') as file:
        for log in file.readlines():
            error_patterns = ["error"]
            for i in range(len(error.split(' '))):
                error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
            if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
                errors_returned.append(log)
        file.close()
    return errors_returned


def file_output(errors_returned):
    """Writes all errors in the errors_returned list to errors_found.log file"""
    with open(os.path.expanduser('~') + '/python/errors_found.log', 'w') as file:
        for error in errors_returned:
            file.write(error)
        file.close()


if __name__ == "__main__":
    """Passes log file as a system argument and creates the errors_found.log file"""
    log_file = sys.argv[1]
    errors_returned = error_search(log_file)
    file_output(errors_returned)
    sys.exit(0)
