with open("log.txt","r") as f:
    lines = f.readlines()
line_no = 1
for line in lines:
    if("python" in line):
        print(f"python is present. Line number:{line_no}")
        break 
    line_no +=1
else:
    print("Pyhton is not here") 