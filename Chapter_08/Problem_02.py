# Problem - 02 
# formula C = 5*(f-32)/9

'''
def f_to_c(f):
    return 5*(f-32)/9  # In Normal Way:

f = int(input("Enter here:"))
print("In Celsius:",f_to_c(f))   '''

# But, In legends way:

def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter here:"))
call = f_to_c(f)
print(f"{round(call,2)}°C")