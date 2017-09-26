
def reverse_string(text):
    reverse_text = ''
    t = len(text)
    for i in range(len(text)):
        reverse_text = reverse_text + text[t - i - 1]
    return reverse_text


s = input('some string:')
print(reverse_string(s))
