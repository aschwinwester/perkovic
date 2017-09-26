lst = [1, 2, 3, 4]
print(len(lst) // 2)  # a
print(lst[:len(lst) // 2])  # b
lst.sort(reverse=True)
print(lst)  # c

lst.append(lst.pop(0))
print(lst)  # c
