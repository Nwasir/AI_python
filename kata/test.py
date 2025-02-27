"""calculate the number of days from 2024 christmas back till the day i was born to my birthday"""

from datetime import datetime

christmas = datetime(year = 2024, month = 12, day = 25)
myBirthday = datetime(year = 1990, month = 6, day = 21)

numberOfDays = christmas - myBirthday

print("there are", numberOfDays.days, "days from my 2024 christmas to myu birthday")

print("**********************")
# Write function RemoveExclamationMarks which removes all exclamation 
# marks from a given string.
# def remove_exclamation_marks(s):
#     return s.replace("!", "")

# print(remove_exclamation_marks("hello! word!"))

#        OR

def remove_exclamation_marks(s):
    return ''.join([char for char in s if char != "!"])

print(remove_exclamation_marks("hello! word!"))
#  OR
# def remove_exclamation_marks(s):
#     #your code here
#     s_list = s.split('!')
#     s = ''.join(s_list)
#     return 
print("*********************************")
# How to use join function
greetings = ['hello', 'Nwasir', 'food', 'is', 'ready']
print(" ".join(greetings))
# formatting phone number

def format_phone(phonenum):
    area_code = "(" + phonenum[:3] + ")"
    exchange = phonenum[3:6]
    line = phonenum[-4:]
    return area_code + " " + exchange + "-" + line

print(format_phone("2025551212"))

print("*********************")

input = "Four score and seven years ago"
for c in range(len(input)):
  if c in ['a', 'e', 'i', 'o', 'u']:
    print(c)
    