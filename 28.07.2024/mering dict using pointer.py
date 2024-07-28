def Merge(a, b):
    res = {**a, **b}
    return res
a = {'a': 1, 'b': 2}
b = {'d': 3, 'c': 4}
c = Merge(a,b)
print(c)
