import imaplib
import email
import re
import pandas as pd
import arrow
import nltk
from nltk.stem import PorterStemmer
from nltk.stem import ISRIStemmer
from langdetect import detect_langs
import openpyxl
from datetime import datetime

# Read the Stored Date and Store the current date and time in an Excel file
# Load the Excel workbook
workbook2 = openpyxl.load_workbook("date.xlsx")
# Select the active sheet
sheet = workbook2.active
# Read the stored date and time from cell A1
stored_datetime = sheet["B1"].value
current_datetime = datetime.now()
# Get the current system time in the desired format
current_datetime = arrow.now().format("ddd, DD MMM YYYY HH:mm:ss Z")

# Write the current date and time to a cell
sheet["A1"] = current_datetime

# sheet["B1"].value = sheet["A1"].value
# Save the workbook
workbook2.save("date.xlsx")

# Load Excel workbook
wb = openpyxl.load_workbook('Arabicdatabase.xlsx')
# Select a specific worksheet
ws = wb['data']

# from MainForm import email1
# from MainForm import password

# username = email1
# password1 = password
# check if the password is correct
try:
    # Connect to the email server using IMAP
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(username, password1)
    print("Login successful!")
except imaplib.IMAP4.error as e:
    print("Login failed. Please check your username and password.")
    print("Error:", e)

# Select the inbox folder
mail.select("inbox")

# Search for all messages from the last message
status, messages = mail.search(None, "ALL")

# Checking the Arabic Phishing LAbel if found in the email
# List all labels (mailboxes)
status, mailbox_list = mail.list()

if status == 'OK':
    # Extract the label names from the mailbox list
    label_names = [mailbox.decode().split(' "/" ')[1] for mailbox in mailbox_list]
    # Search for a specific label
    target_label = "ArabicPhishing"
    if target_label not in label_names:
        new_label_name = "ArabicPhishing"
        # Create the new label
        status, response = mail.create('"{0}"'.format(new_label_name))

# Loop through all the messages and print the body
for num in reversed(messages[0].split()):
    # Fetch the message data
    status, data = mail.fetch(num, "(RFC822)")

    # Parse the email message
    raw_email = data[0][1]
    message = email.message_from_bytes(raw_email)
    msg = email.message_from_bytes(raw_email)
    # Get the message subject
    subject = message["Subject"]
    date1 = message["date"]
    date2 = stored_datetime
    print(date1)
    print(date2)

    if date1 < date2:
        # Print the subject and message body
        # print("Subject:", subject)
        # Print the message body
        print("Older Than")

                        break
    else:
        sheet["B1"].value = sheet["A1"].value
        # Save the workbook
        workbook2.save("date.xlsx")
        exit()

# Logout from the email server
exec(open("MainForm.py").read())
mail.logout()

#    else:
#        # If the message is not multipart, print the payload
#        Lenofemail = len(part.get_payload(decode=True).decode().split())
#        print(Lenofemail)
#        print(message.get_payload(decode=True).decode())
#        cleaned_body = re.sub(r'\W+|\d+|\s+', ' ', part.get_payload(decode=True).decode())
#        print(cleaned_body)
#        words = part.get_payload(decode=True).decode().split()
#        for word in words:
#           words_to_compare = [cell.value for cell in worksheet['A']]
