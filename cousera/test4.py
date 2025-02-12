import os
import datetime

# os.remove("requirements.txt")
print(os.path.exists("requirements.txt"))
print(os.path.exists("list.txt"))

time = os.path.getmtime("list.txt")
print(datetime.datetime.fromtimestamp(time))

print(os.path.getsize("list.txt"))
print()
print(os.getcwd())
