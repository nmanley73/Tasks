# Output whether today is a weekday

import datetime
# Dictionary of days of the week

dte = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday',5:'Saturday',6:'Sunday'}

# Weekday variable
dy = datetime.datetime.today().weekday()

# Check if today is a weekday or weekend
if dy < 5:
    print("Yes, unfortunately today is a weekday")
else:
    print("It is the weekend, yah")
