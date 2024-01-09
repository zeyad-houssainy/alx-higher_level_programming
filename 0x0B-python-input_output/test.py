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


def test_raise_error(a):
    if a < 0: 
        raise ZeroDivisionError("Error #1")
# test_raise_error(-1)
    
def test_raise_multiple_errors(a):

        if (type(a) == int):
            print(f"Thank you, '{a}' will pass")
        else:
            errors = [ZeroDivisionError(
                'error 1: ZeroDivisionError'), SystemError('error 2: SystemError_TEST')]
            raise ExceptionGroup("Text: there was an error_TEST", errors)

# test_raise_multiple_errors(5)
# test_raise_multiple_errors("hey")


def f():
    raise ExceptionGroup(
        "groupA",[OSError(1),
                  SystemError(2),
                  ExceptionGroup("groupB",[
                    OSError(3),
                    RecursionError(4)])
                    ])

try :
     test_raise_multiple_errors("hey")
except Exception as e:  
    print(f"Caugt an exception '{e}'") # Caugt an exception 'there was an error_TEST (2 sub-exceptions)'


# try:
#     f()
# except* OSError as e:
#     print("There were OSErrors")
# except* SystemError as e:
#     print("There were SystemErrors")


exc_error = []
number_of_errors = 0
# def f():
#      try:
#         number_of_errors = number_of_errors + 1
#         raise TypeError(f"This's Error Number: {number_of_errors}")
#      except :
#         exc_error.append()

def f():
    raise TypeError(f"This's Error Number: {number_of_errors}")
f()
f()
