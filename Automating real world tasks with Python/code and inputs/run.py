#!/usr/bin/env python3
import os
import requests


def main():
    """Converting fruit description from a text file into a json dictionary and then posting it on the webpage"""
    # Listing all files and directories in supplier-data/descriptions/
    files = os.listdir("supplier-data/descriptions/")
    print(files)

    for fil in files:
        # For splitting name from extension of a file
        x = fil.split(".")

        with open("/supplier-data/descriptions/" + fil, "r") as revw:
            # Saving all information from a text file to a json dictionary
            info = {"name": revw.readline().rstrip("\n"),
                    "weight": int(revw.readline().rstrip("\n").replace(" lbs", "")),
                    "description": revw.readlines()[0].rstrip("\n"),
                    "image_name": x[0] + ".jpeg"}

            # Posting data to webpage in json format
            response = requests.post("http://35.238.118.139/fruits/", data=info)

            # Checking if the response is successful
            response.raise_for_status()
            print(response.ok)
            print(response.status_code)
            print(response.request.body)


if __name__ == "__main__":
    # Calling main function
    main()
