n, sq_root = [2, -5, 8, 9, -25, 25, 4], []
for i in n:
    if i > 0 and i == (int(i ** 0.5)) ** 2:
        sq_root.append(int(i ** 0.5))
print(sq_root)
