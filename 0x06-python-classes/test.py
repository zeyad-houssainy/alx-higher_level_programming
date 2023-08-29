class human:
    def __init__(self, name, age, gender, height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
    def __str__(self):
        return f"\n\ni'm testing the STR function and it returned...\nname: {self.name}\nAge: {self.age}"
    def greet(self):
        print(f"Hello, i'm {self.name} and i'm {self.age}. Welcome to my channel..")


h1 = human("Zeyad", 21, "Male", 182)
h1.greet()
print(h1)
h2 = human("Nour", 28, "Female", 162)
print(h2)
h2.greet()

h2.blabla = "OK i'm a new attribute that is custome"
print(h2.blabla)


print(h1.__dict__)
print(h2.__dict__)