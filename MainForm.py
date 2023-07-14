import PySimpleGUI as sg
import re
import os
import subprocess

# Define the layout of the form
layout = [
    [sg.Text("Email:"),
     sg.Input(key="-EMAIL-", size=(30, 1), justification='left', pad=(29, 0), default_text="Your Email")],
    [sg.Text("Password:"), sg.Input(key="-PASSWORD-", size=(30, 1), justification='left', password_char='*',
                                    default_text="Password")],
    [sg.Button("Submit", size=(12, 2), pad=(25, 100)),
     sg.Button("Clear", size=(12, 2), pad=(25, 100)),
     sg.Button("Cancel", size=(12, 2), pad=(25, 100))

     ]
]

# Create the window
window = sg.Window("RAPH Model for Phishing Detection", layout, size=(500, 300))
# window.geometry("400x300")  # Width x Height

# Event loop to process events and get form data
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Cancel":
        break
    elif event == "Submit":
        email1 = values["-EMAIL-"]
        password = values["-PASSWORD-"]


                    # subprocess.Popen(["python", "testtesttest.py"])

                else:
                    sg.popup("Please enter a Gmail address.", title="Error")
            else:
                sg.popup("Please enter a valid email address.", title="Error")
    elif event == "Clear":
        window["-EMAIL-"].update("")  # Clear the name input field
        window["-PASSWORD-"].update("")  # Clear the email input field

# Close the window
window.close()


