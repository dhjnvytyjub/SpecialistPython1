text = input()
for j in '!" #$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':
    if j in text:
        text = text.lower().replace(j, '')
print('YES' if text == text[::-1] else 'NO')
