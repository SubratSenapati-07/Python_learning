def convert(f):
    return 5*(f-32)/9

f = int(input("Enter temperature in Ferenhite:"))
print(f"In Celsius: {round(convert(f),2)}°C")
