import os 

if not os.path.exists("tables"):
    os.makedirs("tables")  # For set the file location.

def generateTable(n):
    table = ""
    for i in range(1,11):
        table += f"{n} x {i} = {n*i}\n"

    with open(f"tables/table_{n}.txt","w") as f:
        f.write(table) # tables/table_ it mean table within tables

for i in range(1,21):
    generateTable(i)
