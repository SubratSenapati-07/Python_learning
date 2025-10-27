# Match Case

def match_cas(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found!"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unkwon Status"
        
print(match_cas(5855)) 