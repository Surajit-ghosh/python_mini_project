import datetime
import time
import os

while True:
    # Get current time
    d = datetime.datetime.now()
    # Clear screen (works in Windows & Linux)
    os.system('cls' if os.name == 'nt' else 'clear')
    # Print time in HH:MM:SS format
    print(d.strftime("%H:%M:%S"))
    # Wait for 1 second
    time.sleep(1)
