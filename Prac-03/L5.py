# Insert 12 before 78 index
l1=[12,45,78,3,5,4]
print(l1)
element=12
beforeelement=78
index=l1.index(beforeelement,0,5)
l1.insert(index,element)
print(l1)
