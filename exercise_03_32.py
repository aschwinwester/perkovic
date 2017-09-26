n = int(input('enter (four digits) n:'))
a = n // 1000
b = (n - a * 1000) // 100
c = (n - a * 1000 - b * 100) // 10
d = n - a * 1000 - b * 100 - c * 10
print(a)
print(b)
print(c)
print(d)
