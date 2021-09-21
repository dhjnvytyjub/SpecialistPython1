from random import randint
n, sum_even = [], 0
for _ in range(int(input())):
    n.append(randint(-100, 100))
for i in n:
    if i > 0 and i % 2 == 0:
        sum_even += i
print(sum_even)
