class test:
    def __init__(self, x):
        self.__x = x

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x


p1 = test(42)
# p2 = test(4711)
p1.set_x(1111)
i = p1.get_x()
print(i)
p1.