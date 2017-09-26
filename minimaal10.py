strings = eval(input('Geef lijst met minimaal 10 strings: '))

vier_letter_strings = []

for string in strings:
    if len(string) == 4:
        vier_letter_strings.append(string)

print(vier_letter_strings)

