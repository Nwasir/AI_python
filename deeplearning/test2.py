f = open("list.txt", "r")
test = f.read()
f.close()
# print(test)

for line in test:
    print (line.endswith("st"))