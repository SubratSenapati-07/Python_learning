def strip_and_repl(list,word):
    n = []

    for item in list:
        if not(item == word):
            n.append(item.strip(word))
    return n
    
list = ["Subratan","Rahan","Roocky","an"]

print(strip_and_repl(list,"an"))
        