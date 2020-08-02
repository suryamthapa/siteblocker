"""So, this is the another programme which i have completed.
However, the idea of the programme is not mine originally.
There are many things that i have learnt from this programme.
Such as:
----------------------------------------------------------------------------------------
1. We can run python scripts in background.
2. We have .pyw extension also.
    With the help of scripts with .pyw extension, we can run codes in background also.
3. How to block the website access?
4. How to set up a background process in windows?
4. About seek() and truncate() method.
    seek() helps us to set the cursor to the specific position.
    While truncate() helps us to remove all the content after the cursor.
5. About any() function
    It returns true if any one of the content inside the iterable is True.
    It will return true if iterable is not empty.
------------------------------------------------------------------------------------------
It was fun.
-----------
Basically, what it does is block the access of certain websites during a certain period 
of time in a day.(Time is specified accordingly.)
Modules used:
1. datetime module
"""

# Impotring datetime
from datetime import datetime as dt
import time
# host_path = "hosts"
# Path of the hosts file
host_path = "C:/Windows/System32/drivers/etc/hosts"
# List of the websites to be blocked
website_list = ["www.facebook.com",
                "facebook.com", "google.com", "www.google.com"]
# Ip adress to which the websites are to be redirected
# Here, we are taking our localhost ip adress
redirect = "127.0.0.1"

# Setting up the loop.
while True:
    # Checking the condition(Specifying time)
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 20):
        print("working hours...")
        # Opening the hosts file in read/append mode
        with open(host_path, "r+") as hosts:
            lines = hosts.read()
            # Looping through the website list
            for website in website_list:
                # Checking if the websites are already blocked
                if website in lines:
                    pass
                else:
                    # Writing the respective lines
                    hosts.write("\n" + redirect + " " + website)
    else:
        print("Fun hours...")
        # Opening the file
        with open(host_path, "r+") as hosts:
            lines = hosts.readlines()
            hosts.seek(0)  # cursor to the begining of the file
            # Iterating through the lines
            for line in lines:
                # Checking if the website is on the line
                if not any(website in line for website in website_list):
                    # Wrtiting the same line if website is not present in the line
                    hosts.write(line)
            # Removing the content after the current position of cursor
            hosts.truncate()
    time.sleep(5)
