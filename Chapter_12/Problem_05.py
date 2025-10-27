n = int(input("Enter number:"))

mul_tab = [ (n*i) for i in range(1,11) ]

with open("tables.txt","a") as f:
    f.write(str(mul_tab) + "/n")

    # RUN IN FILE i/o:


# print(f"Multiplication table:",mul_tab)