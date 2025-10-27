# By loop

f = open("myfile_01.txt","r")
line = f.readline()
while(line !=""): 
    print(line)
    line = f.readline()
    
f.close() 