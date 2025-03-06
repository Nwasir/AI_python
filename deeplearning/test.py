
ice_cream_flavors = {
    "Mint Chocolate Chip": "Refreshing mint ice cream studded with decadent chocolate chips.",
    "Cookie Dough": "Vanilla ice cream loaded with chunks of chocolate chip cookie dough.",
    "Salted Caramel": "Sweet and salty with a smooth caramel swirl and a hint of sea salt."
}  
print (ice_cream_flavors.keys(), end=" ")
print("******************************")
print(ice_cream_flavors.values())
# to add new item to the dictionary
ice_cream_flavors["Rocky Roads"] = "Chocolate ice cream mixed with other ingredients."
print(ice_cream_flavors)
print("*****************")

ashanka = {
    "age": 34,
    "favorite color": "black",
    "best friend": "Nwasir"
}
print(ashanka)
ashanka["Best Food"] = ["ukwa", "ogbono soup", "okro soup"]
print(ashanka)
print(ashanka)
# You can use dictionaries to store all the tasks with their priorities 
# in a single data object.
high_priority_tasks = [
    "Compose a brief email to my boss explaining that I will be late for tomorrow's meeting.",
    "Create an outline for a presentation on the benefits of remote work."
]

medium_priority_tasks = [
    "Write a birthday poem for Otto, celebrating his 28th birthday.",
    "Draft a thank-you note for my neighbor Dapinder who helped water my plants while I was on vacation."
]

low_priority_tasks = [
    "Write a 300-word review of the movie 'The Arrival'."
]
#create dictionary with all tasks dictionaries can contain lists!
prioritized_tasks = {
    "high_priority": high_priority_tasks,
    "medium_priority": medium_priority_tasks,
    "low_priority": low_priority_tasks
}
print(prioritized_tasks)