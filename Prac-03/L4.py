# Insert 50 at 4th index --without using insert() function--

l1=[12,45,78,3,5,4]
print(l1)

num=50
ind=2
l1.append(0)
i=len(l1)-2

while i >= ind:
	l1[i+1]=l1[i]
	i-=1
	
l1[ind]=num

print(l1)
	
