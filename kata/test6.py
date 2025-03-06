"""Complete the square sum function so that it squares each number passed
into it and then sums the results together.
For example, for [1, 2, 2] it should return 9 because """

def square_sum(numbers):
    result = []
    for num in numbers:
        result.append(num ** 2)
    return sum(result)

some_numbers = [1, 2, 3]
print(square_sum(some_numbers))
print("*******************")

def cube_sum(numbers):
    result = 0
    for num in numbers:
        result += num ** 3
    return result

some_numbers = [1, 2, 3]
print(cube_sum(some_numbers))

print("*******************")

def absolute_sum(numbers):
    result = 0
    for num in numbers:
        result += abs(num)
    return result

some_numbers = [1, 2, 3]
print(absolute_sum(some_numbers))

