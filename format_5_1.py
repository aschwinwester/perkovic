
def convert(celcius):
    fahrenheit = celcius * 1.8 + 32
    return fahrenheit

print('   F      C  ')
for hot in range(-30, 40, 10):
    line_new = '{:>5}  {:>5}'.format(str(convert(hot)), str(hot))
    print(line_new)
