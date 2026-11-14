#function type and type casting 


a = 31 
t = type(a) # class <int>


print(t)
print(type(a)) # same without variable

b = "Azad"
q= type(b)

c = "90.2"# knowingly it is string 
print("Type of c ",type(c))

d= float(c)
print("Typecasted to float ",d, type(d))
print(q)
print(type(b)) # same without variable
