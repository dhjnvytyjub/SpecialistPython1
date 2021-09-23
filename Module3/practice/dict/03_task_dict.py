staff = [
    {
        'name': 'Алексей',
        'surname': 'Петров',
        'salary': 124300
    },
    {
        'name': 'Николай',
        'surname': 'Петров',
        'salary': 120000
    },
    {
        'name': 'Иван',
        'surname': 'Павлов',
        'salary': 34500
    },
    {
        'name': 'Василий',
        'surname': 'Кукушкин',
        'salary': 162500
    },
    {
        'name': 'Василий',
        'surname': 'Павлов',
        'salary': 47800
    },
]
max = 0
info_max = {}
for i in staff:
    if i['salary'] > max:
        max = i['salary']
        info_max = i
print('максимальная ЗП: ', info_max['name'], info_max['surname'])

min = max
info_min = {}
for i in staff:
    if i['salary'] < min:
        min = i['salary']
        info_min = i
print('минимальная ЗП:', info_min['name'], info_min['surname'])

from statistics import mean
print('средняя ЗП:', int(mean([i['salary'] for i in staff])))

surname = [i['surname'] for i in staff]
namesake = (len(surname) - len(set(surname))) * 2
print('количество однофамильцев: ', namesake)

sorted_tuple = sorted([i['salary'] for i in staff])
for i in sorted_tuple:
    for j in staff:
        if j['salary'] == i:
            print(j['name'], j['surname'])
