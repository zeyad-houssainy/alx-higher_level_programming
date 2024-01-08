#!/usr/bin/python3

myfile = open("test.txt", "w+")
myfile.write(
    "Hello there i'm testing how to open and write a file from scratch")
# myfile = open
myfile = open("test.txt", "r+")

read_my_file = myfile.read()
print(read_my_file)

myfile.seek(0)
myfile.write("Starting the file\n")

myfile.seek(0, 2)
myfile.write("\nwriting by the end of the file")

# myfile.close()
# myfile.open()

# myfile = open("test.txt", "w+")
# print(read_my_file)

myfile = open("test.txt", "a+")
# myfile.read()
myfile.write("\nhihihih")
read_lines = myfile.readlines()


for line in read_lines:
    myfile.seek(0, 2)
    myfile.write("zZz\n")
    myfile.write(line)
    myfile.write("\n")


print(myfile.closed)

myfile.close()

print(myfile.closed)


with open("test.txt", "a+") as file:
    x = file.read()
    print(x)