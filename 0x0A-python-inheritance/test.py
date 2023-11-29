class Animal:
    count = 0
    
    def __init__(self, blooded="Unknown", birthtype="Unknown", cover="Unknown"):
        Animal.count += 1
        self.__blooded = blooded
        self.__birthtype = birthtype
        self.__cover = cover

    @property
    def blooded(self):
        return self.__blooded
    
    @blooded.setter
    def blooded(self, blooded):
        self.__blooded = blooded

    @property
    def birthtype(self):
        return self.__birthtype

    @birthtype.setter
    def birthtype(self, birthtype):
        self.__birthtype = birthtype

    @property
    def cover(self):
        return self.__cover
    
    @cover.setter
    def cover(self, cover):
        self.__cover = cover
    
    def __str__(self):
        return f"I'm {type(self).__name__} Number #{Animal.count} my cover is {self.cover} "

a1 = Animal("yes", "Egg", "Fur")
print(a1)
a2 = Animal("NO", "Mammal", "Feather")
print(a2)


