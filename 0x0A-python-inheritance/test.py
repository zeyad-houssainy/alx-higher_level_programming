class Human:

    def __init__(self, name="None", age=0, gender="male", height=150):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height


    def human_data(self):
        return {"Name": self.name,
                "Age": self.age, 
                "Gender": self.gender,
                "Height": self.height
                }
    
    def __str__(self):
        return f"####\nHello, i'm {self.name}, i'm {self.age}.\nMy height is {self.age} and i'm a {self.gender}\n####"
    

p1 = Human("zeyad", 25, "Male", 190)
print(p1)
print(p1.human_data())
