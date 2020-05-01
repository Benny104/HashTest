#Author: Benny
import hashlib
list = open("PassList.txt")

#Deals with encoding and hashing the user input
z = str(input("Please input a word: "))
zv2 = z.encode()
x = hashlib.sha256()
x.update(zv2)
y = x.hexdigest()

#Deals with comparing the user's hashed word with the hashed words in the list
for i in list:
    iHashed = hashlib.sha256()
    iv2 = i.encode()
    iHashed.update(iv2)
    iy = iHashed.hexdigest()

    if iy == y:
        print("The word you entered was:", i)
        print("The hashed word was:", iy)

    print(iy)




