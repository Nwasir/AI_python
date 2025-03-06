def multiple_occurrences(string, letters):
    return string.count(letters) >= 2
      
print(multiple_occurrences("apple", 'p'))   # True  (because 'p' appears twice)
multiple_occurrences("banana", 'n')  # True  (because 'n' appears twice)
multiple_occurrences("hello", 'o')   # False (because 'o' appears only once)
multiple_occurrences("world", 'z')   # False (because 'z' is not in the string)