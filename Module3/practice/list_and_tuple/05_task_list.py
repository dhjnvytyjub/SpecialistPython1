fruits = ["яблоко", "банан", "киви", "арбуз"]
for i in range(1, len(fruits) + 1):
    print(i, fruits[i - 1].rjust(len(max(fruits)), ' '), sep='.')
