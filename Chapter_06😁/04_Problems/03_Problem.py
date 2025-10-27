p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subsribe now"
p4 = "click this"

message = (input("Paste your comment: "))

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This is a spam💀")

else:
    print("THis is safe✅")