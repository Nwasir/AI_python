# def digitize(n):
#     # return int(str(n)[::-1])
#     return [int(digit) for digit in str(n)[::-1]]

# print(digitize(12345))

print("**********************************************************")

def litres(time):
    return int(time / 2)

print(litres(0.7))
print(litres(5.9))

print("***********************")

def positive_sum(arr):
    sum = 0
    for e in arr:
        if e > 0:
            sum = sum + e
    return sum
numbers = [1,6,3,6,-2,8, -7]
print(positive_sum(numbers))

print("******************************************")

for i in range(10):
    print("Hello World")

print((9-3)/(2*(1+2)))
print("*****************************")
print("xyzy".isalpha())

test = "How much wood would a woodchuck chuck"
print(test.split())
print(test.split('-'))

weather = "rainfall"

print(weather[:4])