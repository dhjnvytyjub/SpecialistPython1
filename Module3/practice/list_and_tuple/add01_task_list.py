x = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
y = [i * 2 - 4 for i in x]
print(*[i for i in list(zip(x, y))])
