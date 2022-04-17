#!/usr/bin/env python3
import re
import os
import csv
import sys


def contains_domain(address, domain):
    """Returns True if the email address contains the given domain in the domain position and false if not"""
    domain = r'[\w\.-]+@' + domain + '$'
    if re.match(domain, address):
        return True
    return False


def replace_domain(address, old_domain, new_domain):
    """Replaces the old domain with the new domain in the received address"""
    old_domain_pattern = r'' + old_domain + '$'
    address = re.sub(old_domain_pattern, new_domain, address)
    return address


def main():
    """Processes the list of emails and replaces any instances of the old domain with the new domain"""
    old_domain = input("Which old domain do you want to replace? ")
    new_domain = input("What is the name of the new domain? ")
    csv_file = sys.argv[1]
    report_file = os.path.expanduser('~') + '/python/updated_domain_names.csv'

    with open(csv_file, 'r') as file:
        user_data_list = list(csv.reader(file))
        for first_index in range(0, len(user_data_list)):
            if contains_domain(user_data_list[first_index][1], old_domain):
                replaced_email = replace_domain(user_data_list[first_index][1], old_domain, new_domain)
                user_data_list[first_index][1] = replaced_email

    with open(report_file, 'w+') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(user_data_list)
        output_file.close()


main()
