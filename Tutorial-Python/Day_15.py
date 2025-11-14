# Code Exercise

import time


timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
print(timestamp)
timestampH = time.strftime("%H")
timestampint = int(timestampH)
print(timestamp)
timestampM = time.strftime("%M")
print(timestamp)
timestampS = time.strftime("%S")
print(timestamp)


# if timestampint >=12 and timestampint <=24:
#     print("Good Afternoon")
# else:
#     print("Good Morning")


import datetime


def greet_user():
    # Get the current hour (0 to 23)
    current_time = datetime.datetime.now()
    hour = current_time.hour

    # Determine the greeting based on the hour
    if hour < 12:
        greeting = "Good Morning"
    elif hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"

    user_name = input("Please enter your name: ")

    # Print the final personalized greeting
    print(f"{greeting}, {user_name}!")


# Call the function to run the script
greet_user()