word = "Donkey"

with open("donkey.txt","r") as f:
    content = f.read()

new = content.replace(word,"#####")

with open("donkey.txt","w") as f:
    f.write(new)