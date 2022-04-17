#!/usr/bin/env python3
import os
from datetime import date
import reports
import emails


def gen_pdf_body():
    """Converts name and weight of a fruit from a text file into a paragraph shown in the below comment"""
    """
    name: Apple
    weight: 600lbs
    
    name: Kiwi
    weight: 500lbs
    
    name: Mango
    weight: 700lbs
    """
    fruits = os.listdir("supplier-data/descriptions")
    fruit_list = []

    for fruit in fruits:
        # Retrieving name and weight from a text file and converting it into a list of dictionaries
        # Each dictionary called fruit_wt contains name and weight of one fruit
        with open("supplier-data/descriptions/" + fruit, "r") as fil:
            fruit_wt = {"name": fil.readline().rstrip("\n"),
                        "weight": fil.readline().rstrip("\n")}
            fruit_list.append(fruit_wt)

    # Writing info of all dictionaries in fruit_list into a single paragraph (as shown in the 2nd comment above)
    paragraph = ""
    for frut in fruit_list:
        for k, v in frut.items():
            paragraph += k + ": " + v + "<br />\n"
        paragraph += "\n<br />"

    return paragraph


def gen_report_email(pdf_body):
    """Creating and emailing report"""
    # Regarding report generation
    now = date.today().strftime("%B %d, %Y")
    title = "Processed Update on " + str(now)
    reports.generate_report("/outputs/processed.pdf", title, pdf_body)

    # Regarding Creation and sending of email message
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    msg = emails.generate_email("automation@example.com", "student-jk-8b0ed7c6f@example.com", subject, body,
                                "/outputs/processed.pdf")
    emails.send_email(msg)


if __name__ == "__main__":
    pdf_text_paragraph = gen_pdf_body()
    gen_report_email(pdf_text_paragraph)
