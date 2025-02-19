def to_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds

print('Welcome to time converter')

cont = "y"

while (cont.lower() == "y"):
    hour = int(input("Enter the amount of hour: "))
    minutes = int(input("Enter the amount of minutes: "))
    seconds = int(input("Enter the amount of seconds: "))

    print("That's {} to seconds".format(to_seconds(hour, minutes, seconds)))
    print()
    cont = input("Do you want to play another one? [press y to continue and any key to stop] ")
print("Goodbye!")

