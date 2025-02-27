"""Trolls are attacking your comment section!
A common way to deal with this situation is to remove all of the vowels 
from the trolls' comments, neutralizing the threat.
Your task is to write a function that takes a string and return a new 
string with all vowels removed. For example, the string
"This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
"""
import re
# def removeVowels(strings):
#     return re.sub(r"[aeiouAEIOU]", "", strings)

# or

# def removeVowels(strings):
#     for words in "aeiouAEIOU":
#         strings = strings.replace(words, "")
#     return strings
# Or

def removeVowels(strings):
    return "".join(char for char in strings if char.lower() not in "aeiou")

print(removeVowels("This is my beloved sOn Nwasir"))
print("*********************")

"""Given two arrays a and b write a function comp(a, b) that checks 
whether the two arrays have the "same" elements, with the same 
multiplicities (the multiplicity of a member is the number of times it 
appears). "Same" means, here, that the elements in b are the elements 
in a squared, regardless of the order. Examples Valid arrays:
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]"""

# def compare(array1, array2):
#     if array1 is None or array2 is None:
#         return False
#     return sorted([numbers ** 2 for numbers in array1]) == sorted(array2)

# array1 = [121, 144, 19, 161, 19, 144, 19, 11]  
# array2 = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
# print(compare(array1, array2))