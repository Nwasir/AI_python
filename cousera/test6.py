"""Dakota is a fairly new programmer with his company. He just earned a spot 
on the project for LogicLink Innovations. This is one of the biggest and most 
credible companies in the industry, so Dakota knows he has to excel on this 
project to help make a name for himself. LogicLink Innovations manages 
customer data and has hundreds of customer phone numbers in its database. 
The phone numbers are in inconsistent formats. Some are written with dashes, 
some in parentheses with spaces, and some are just digits. Dakota sees this:
123-456-7890
(123) 456-7890
1234567890"""

import re

def correct_phone_numbers():
    with open("phones.csv", "r") as phones:
        for phone in phone:
            new_phone = re.sub(r"^\D*(\d{3})\D*(\d{3})\D*(\d{4})$", r"(\1) \2-\3", phone)
            print(new_phone)