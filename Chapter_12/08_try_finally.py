def fin():
    try:
        a = int(input("Hey! Enter a number:"))
        print(a)
        return

    except ValueError as v:
        print(v)
        print("Hello")
        return
    
    
    finally: # return means program stoped,but finally not obeys it
        print("finally running")  # finally return krne ke bad v chlega.
                                  # It means a har hal me chlega.
fin()