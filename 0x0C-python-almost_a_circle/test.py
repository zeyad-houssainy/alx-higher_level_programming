def test_function(var1, *argv):
    print(f"Variable Number 1: {var1}")
    count = 2
    for items in argv:
        print(f"Variable number {count}: {items}")
        count += 1

test_function("Mohamed", "Zeyad", "Habiba","Rana", "Sarah")

print("$$$$$$$$$$$$$$$$$$$$")

dict = {"name": "Zeyad", "Age": 29, "Hobbies": ["Games", "Programming"]}
# print(dict)

# for key, value in dict.iteritems():
#     print(f"{key} >>> {value}")

def test_kwargs(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print(f"{key} >>> {value}")


test_kwargs(name = "Hi i'm zeyad")


def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print (f"{key} == {value}")
greet_me(name = "Raneem", age = 26)



