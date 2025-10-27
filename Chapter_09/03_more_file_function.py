f = open("myfile_01.txt")

lines = f.readlines()      # Iska use karke hum multiple line ko reads kar skte hai. in List form.
print(lines,type(lines))   

f.close()