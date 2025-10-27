words =["not","boy","I","dog"]

with open("problem_05.txt","r") as f:
    x = f.read()

for word in words:
    y = x.replace(word,"#"*len(word))

with open("problem_05.txt","w") as f:
    f.write(y)