import copy


def foo(lst):
    lst2 = lst.copy()
    lst2[0] = 100
    print(lst2)


lst = [21, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s = set()
for i in range(2000, 2010):
    s.add(i)
for i in range(10):
    s.add(10 - i)
for i in range(10):
    s.add(-i)


for i in s:
    print(i)
