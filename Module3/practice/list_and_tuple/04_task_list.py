import random
m = [random.randint(-10, 10) for i in range(int(input()))]
print(sum([i for i in m if i > 0]))
