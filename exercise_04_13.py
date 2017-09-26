s = 'abcdefghijklmnopqrstuvwxyz'
print(s[1:3] == 'bc')  # a
print(s[:14] == 'abcdefghijklmn')  # b
print(s[14:] == 'opqrstuvwxyz')  # c
print(s[1:-1] == 'bcdefghijklmnopqrstuvwxy')  # d The slice of s excluding the first and last characters is 'bcdefghijklmnopqrstuvw'.