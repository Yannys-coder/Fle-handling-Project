file = open("TopSecret.txt", "r")
print(file.read())
file.close()

file = open("TopSecret.txt", "r")
print(file.read(10))
file.close()

