"""Write a Python program that uses a for loop to find the largest 
number in a given list."""

numbers = [12, 45, 7, 89, 23]
print(max(numbers)) #this line can do the same thing
largest_numbers = numbers[0]
for x in numbers:
    if x > largest_numbers:
        largest_numbers = x
print (largest_numbers)

"""Write a Python program that uses a for loop to find the smallest 
number in a given list."""
numbers = [34, 15, 88, 2, 7]
# print(min(numbers)) this line can do the same thing
smallest_number = numbers[0]
for x in numbers:
    if x < smallest_number:
        smallest_number = x
print(smallest_number)

"""Write a Python program to find the second largest number in a given
 list."""
numbers = [10, 20, 4, 45, 99]
large = max(numbers)
second = float("-inf")
for x in numbers:
    if x != large and x > second:
        second = x
print(f"second largest number: {second}")

"""Write a Python program to find the third largest number in a 
given list."""
my_numbers = [50, 20, 40, 90, 70]
largest = max(my_numbers)
second = float("-inf")
third = float("-inf")
for x in my_numbers:
    if x != largest and x > second:
        third = second
        second = x
    elif x != largest and x != second and x > third:
        third = x
print("third:", third)
print("**********************************")
"""A teacher gives three test scores to a student: 𝑠1, s2, and s3. 
The grades are assigned based on the average of these scores, using the
following scale:
A: Average is between 85 and 100 (inclusive).
B: Average is between 70 and 84 (inclusive).
C: Average is between 50 and 69 (inclusive).
D: Average is between 35 and 49 (inclusive).
F: Average is below 35.
Write a function calculate_grade(s1, s2, s3) that takes in three scores
and returns the grade based on the scale above."""
def calculate_grade(s1, s2, s3):
    average = (s1 + s2 + s3) / 3
    grade = ""
    if average >= 85:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 50:
        grade = "C"
    elif average >= 35:
        grade = "D"
    else:
        grade = "F"
    return grade

print(calculate_grade(90, 85, 88))  # Output: "A" (average = 87.67)
print(calculate_grade(75, 80, 72))  # Output: "B" (average = 75.67)
print(calculate_grade(60, 55, 50))  # Output: "C" (average = 55.0)
print(calculate_grade(40, 38, 35))  # Output: "D" (average = 37.67)
print(calculate_grade(20, 25, 30)) 
