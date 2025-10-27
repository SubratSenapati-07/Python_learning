# Check that a tuple type cannot be changed in python.

a = (54,46,"Subrat") # List can mutable but Tuple can't.
a[2] = "RockSubrat"
print(a)
