names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
max = names[0]
for i in names:
    if len(i) > len(max):
        max = i
print(max)
