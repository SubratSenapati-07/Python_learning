


def circle_properties(radias):
    area = 3.14*radias*radias
    circumference = 2*3.14*radias
    return area,circumference
r = float(input("Enter radius:"))
ar,cr = circle_properties(r)
print("area:",round(ar,2))
print("circumference:",round(cr,2))

# OUTPUT:
# area = 153.86
# circumference = 43.96

