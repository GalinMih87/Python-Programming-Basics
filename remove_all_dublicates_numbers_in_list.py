lst = [1, 2, 2, 3, 2, 2, 2, 3, 2, 2, 3, 3, 3, 3, 4]

while 2 in lst:
    lst.remove(2)

while 3 in lst:
    lst.remove(3)
print(lst)
