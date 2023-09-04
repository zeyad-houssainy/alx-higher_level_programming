class Human:
    def __init__(self, name="Not assigned", age=0, gender="None"):
        self.name = name
        self.age = age
        if gender.lower() == "female" or gender.lower() == "male":
            self.gender = gender
        else:
            raise ValueError(f"Gender for '{self.name}' must be either 'Male' or 'Female'")
    def greet(self):
        print(f"Hello i'm {self.name} and i'm {self.age} old\nI'M a {self.gender}")

    def __str__(self):
        """to use print function on it"""
        return f"i'm a new human. my code name is {self.name}"


p1 = Human("Zeyad", 25, "Male")
# print(p1.name)
# p1.greet()
# p1.name = "Mohamed"
# print(p1.name)
# p1.greet()
p2 = Human("habiba", 15, "Female")
# print(p1)
# print(p2)

class Dog:
    #basic info about dogs
    sound = "Roff Roff"
    leg_count = 4

    def __init__(self, name, type, color):
        self.__name = name
        self.color = color
        self.type = type

    def get_name(self):
        return self.__name
    
    def set_name(self, new_name):
        self.__name = new_name

    

# print(Dog.sound)
dog1 = Dog("Bob","German shephard", "White")



