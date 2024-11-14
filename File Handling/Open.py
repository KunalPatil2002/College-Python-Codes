
file = open('C:/Users/Lenovo/OneDrive/Desktop/Python Codes/File Handling/file1.txt','r')

for each in file:
    print(each)

print(file.read())    

with open('file1.txt' ) as file:
    data = file.read()

print(data)
