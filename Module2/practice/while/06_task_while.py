n, a, b = int(input()), [], []
for i in range(1, n + 1):
    count = 0
    for j in range(1, i):
        if i % j == 0:
            count += j
    a.append(i)
    b.append(count)
my_dict = dict(zip(a, b))
for k in my_dict:
    for h in my_dict:
        if k == my_dict[h] and h == my_dict[k] and k != h:
            print(k, h)
