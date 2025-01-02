"""calculate the number of days from 2024 christmas back till the day i was born to my birthday"""

from datetime import datetime

christmas = datetime(year = 2024, month = 12, day = 25)
myBirthday = datetime(year = 1990, month = 6, day = 21)

numberOfDays = christmas - myBirthday

print("there are", numberOfDays.days, "days from my 2024 christmas to myu birthday")