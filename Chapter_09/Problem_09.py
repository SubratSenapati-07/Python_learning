with open("file_01.txt","r") as f:
    file_01 = f.read()


with open("file_02.txt","r") as f:
    file_02 = f.read()

if(file_01 == file_02):
    print("Yes,Both are Identical")

else:
    print("Yes,Both are not Identical")