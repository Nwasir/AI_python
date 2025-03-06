friends = ['Churchill', 'Manson', 'Doctor', 'Agency']
for friend in friends:
    print(f"Hi {friend}")

print("*****************************")
# username = input("Enter your username: ")
def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    else:
        print("Valid username")

print("********************")
friends_list = ["Tommy", "Isabel", "Daniel", "Otto"]

### --------------- ###
friends_list.append("Sandra")

print(friends_list)

friends_list.remove("Tommy")
print(friends_list)
print("**********************")
"""Try out the enumerate function for yourself in this quick exercise.
Complete the skip_elements function to return every other element from
the list, this time using the enumerate function to check if an element
is in an even position or an odd position."""
def skip_elements(elements):
    result = []
    for index, name in enumerate(elements):
        if index % 2 == 0:
            result.append(name)
    return result


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print("***********list comprehension******************")
"""This exercise walks you through how to write a list comprehension to
create a list of squared numbers (n*n or n**2). It needs to return a
list of squares of consecutive numbers between “start” and “end” 
inclusively. For example, squares(2, 3) should return a list 
containing [4, 9]."""
def squares(start, end):
    return [n*n for n in range(start, end + 1)]
print(squares(2, 3))    # Should print [4, 9]
print(squares(1, 5))    # Should print [1, 4, 9, 16, 25]
print(squares(0, 10))   # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print("*****update****************")
wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
print(wardrobe)

speed_limits = {"street": 35, "highway": 65, "school": 15}
print(speed_limits["highway"])
