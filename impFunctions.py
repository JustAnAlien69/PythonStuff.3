a = open("text.txt")

#Reads the text from a file
b = a.read()
print(b)

#reads the entire text and stores the lines as elements in an array
c = a.readlines()
print(c)
print(c[1])