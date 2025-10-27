try:
    a = int(input("Hey! Enter a number:"))
    print(a)

except ValueError as v:
    print(v)
    print("Hello")
    
else:
    print("i'm inside else😂")
    # else tabhi kam karega
    # jab try: succesfully run krega.