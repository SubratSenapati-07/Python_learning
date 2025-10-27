class employee:
    name = "Alone Star"     
    language = "python"      
    salary = 10000

Sr = employee()  # Sr be a Object
Sr.language = "Html"
                       # It means Python check krega 
                       # instance attribute hai iska kuch value ha ya nhi
                       # then agar hoga toh instance attribute hi print krega
                       # otherwise class attributes print krega.
print(Sr.name, Sr.language, Sr.salary)

