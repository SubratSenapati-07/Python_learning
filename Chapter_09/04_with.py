f = open("file.txt")
print(f.read())
f.close()

# Same thing written as :

with open("file.txt") as f:
    print(f.read())

# It closed automatically.