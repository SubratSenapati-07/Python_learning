with open("log.txt","r") as f:
    content = f.read()

if("python" in content):
    print("python word present in the above content")

else:
    print("python word is not present the above content")
