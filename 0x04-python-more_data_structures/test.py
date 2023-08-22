a = {"Z": 1, "b": 2, "c": 3, "d": "zeyad", "x": "Ahemd"}
b = [1, 2, 3, 4, 5, 6]
c = (1, 2, 3, 4, 5, 6)
def test(n):
    return(2*n)
print(list(map(test, b)))
print(tuple(map(test, c)))