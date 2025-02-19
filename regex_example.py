#!/usr/bin/env
# name = input("please eter your name: ")
# print("Hello! my name  is " + name)

print("*****************************")
import re
# print(re.search("n.a", "nwasir"))
# print(re.search("^N", "nwasir", re.IGNORECASE))
# print(re.search("nwa", "Nwasir", re.IGNORECASE))

# print(re.search(r"dog|cat", "I like dogs."))
# print(re.search(r"dog|cat", "I like cats."))
# print(re.findall(r"dog|cat", "i like dogs and cats."))
# print(re.search(r"[Pp]ython", "python"))
#it will return none because of the space around the "good"
print(re.search(r"[a-z]good", "nwasir is the good guy"))
# this will run normal
print(re.search(r"[a-z]ood", "nwasir is the good guy"))
print(re.search(r"[a-z]", "Nwasir is the good guy"))
print(re.search(r"[a-zA-Z]", "Nwasir is the good guy"))
print(re.search(r"[a-zA-Z0-9]", "Nwasir is the good guy9"))
print(re.search(r"cloud[a-zA-Z0-9]", "cloudy"))
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))
print(re.search(r"n.*r",  "nwasir"))
print(re.search(r"n[a-z]*r", "Nwasir", re.IGNORECASE))
print(re.search(r"n?sir", "nwasir"))
# print(re.search(r".w", "nwasir is a good boy"))
# print(re.search(r"\.nwasir", "nwasir is the good guy"))
# print(re.search(r"\.nwasir", "jim.nwasir"))
# # line 32 and 33 gives the same result
# print(re.findall(r"\b[a-zA-Z]{5,}\b", "A scary ghost appeared"))
# print(re.findall(r"\w{5,}", "A scary ghost appeared"))
# print(re.search(r"\[(\d+)\]", "I am [453] year old"))

# print(re.split(r"the|a", "One sentence. Another one? And the last one!"))

