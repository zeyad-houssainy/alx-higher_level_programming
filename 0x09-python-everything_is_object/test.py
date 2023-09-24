#l1 = [1, 2, 3]
#l2 = l1
#print(l1 is l2)

a = "Zeyad"
print(id(a))
a = "Mohamed"
print(id(a))
a = [1,2,3]
print(id(a))
a[0] = 8
print(id(a))
b = a
print(id(a))
print(id(b))
b = "Z"
print(id(a))
print(id(b))

