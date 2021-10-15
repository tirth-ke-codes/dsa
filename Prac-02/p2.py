# Find number of characters in a given string --without using len() function--

string=input("Enter a string : ")
counter = 0

for character in string:
    if character != "\0":
        counter += 1
print("Given string contains",counter,"characters.")


#while string[counter] != "\0":
    #print(counter)
    #counter+=1
#print("Given string contains", counter-1, "characters.")
