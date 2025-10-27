with open("this.txt","r") as f:
    x = f.read()

with open("this_copy.txt","w") as f:
    f.write(x)