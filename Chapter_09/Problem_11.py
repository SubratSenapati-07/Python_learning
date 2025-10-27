with open("old.txt","r") as f:
    x = f.read()

with open("renamed_by_python","w") as f:
    f.write(x)