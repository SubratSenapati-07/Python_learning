'''Write a program to find out wheather a student has passed or failed if
it requires a total of 40% and at least 33% in each subject to pass.
 (Assume 3 Subject and take marks as an input from the user.)'''

a = int(input("First subject mark: "))
b = int(input("Second subject mark: "))
c = int(input("Last subject mark: "))
d = ((a+b+c)*(100))/300
if(a>=33 and b>=33 and c>=33 and d>=40):
    print("Passed 😁","Percentages :",d,"%")

else:
    print("Failed 😭","Percentages: ",d,"%")

