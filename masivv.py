a = [5, 12, 7, 3, 9, 21, 4, 8, 15, 6]
print("Крок 1:", a)

a.append(100)
print("Крок 2:", a)

a.insert(0, 50)
print("Крок 3:", a)

a.insert(5, 77)
print("Крок 4:", a)

a.remove(max(a))
a.remove(min(a))
print("Крок 5:", a)