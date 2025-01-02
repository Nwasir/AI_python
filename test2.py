def digitize(n):
    # return int(str(n)[::-1])
    return [int(digit) for digit in str(n)[::-1]]

print(digitize(12345))