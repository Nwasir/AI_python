"""A school wants to calculate final grades for students based on four 
test scores: s1, s2, s3, and s4. Each score is weighted differently, 
as follows:

s1: 25% of the total grade
s2: 25% of the total grade
s3: 30% of the total grade
s4: 20% of the total grade
The final grade is assigned based on the weighted average, using this
scale:

A: 90 - 100
B: 80 - 89
C: 70 - 79
D: 60 - 69
F: Below 60
Write a function calculate_weighted_grade(s1, s2, s3, s4) that takes in
the four scores, calculates the weighted average, and returns the 
corresponding grade."""
def calculate_weighted_grade(s1, s2, s3, s4):
    average = (s1 * 0.25) + (s2 * 0.25) + (s3 * 0.30) + (s4 * 0.20)
    if (average) >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade

print(calculate_weighted_grade(85, 90, 92, 88))  # Output: "A"
print(calculate_weighted_grade(70, 75, 80, 85))  # Output: "B"
print(calculate_weighted_grade(60, 65, 70, 75))  # Output: "C"
print(calculate_weighted_grade(50, 55, 60, 65))  # Output: "D"
print(calculate_weighted_grade(40, 45, 50, 55))  # Output: "F"

