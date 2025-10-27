words = [ "Donkey","yaar","good"]

with open("donkey.txt","r") as f:
    x = f.read()

for word in words:
    y = x.replace(word, "#" * len(word))

with open("donkey.txt","w") as f:
    f.write(y)