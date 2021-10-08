def trans(n): # преобразование любой дроби к виду [числитель, знаменатель]
    if len(n) == 1:
        m = [abs(n[0]), 1]
    elif len(n) == 3:
        m = [abs(n[0]) * n[2] + n[1], n[2]]
    else: m = [abs(n[0]), n[1]]
    if n[0] < 0:
        m[0] *= -1
    return m

def to_lis(exp):    # каждая дробь - список, каждая цифра - элемент списка
    import re
    a = [int(i) for i in re.split(' |/', exp[0].strip())]
    b = [int(i) for i in re.split(' |/', exp[1].strip())]
    return trans(a), trans(b)

def com_div(a, b):   # находит наибольший общий делитель и сокращает на него числитель и знаменатель
    div = 0
    for i in range(1, a + 1):
        if a % i == 0 and b % i == 0:
            div = i
    return [a//div, b//div]

def normalize(n):     # приведение к виду для выдачи на печать
    if len(n) == 1:
        c = n[0]
        return c
    elif len(n) == 2:
        c = com_div(abs(n[0]), n[1])
        if n[0] < 0:
            c[0] *= -1
        return f'{c[0]}/{c[1]}'
    elif len(n) == 3:
        c = [n[0]] + com_div(n[1], n[2])
        return f'{c[0]} {c[1]}/{c[2]}'

def trans_two(n):     # выделение целой части
    if abs(n[0]) // n[1] != 0:
        if abs(n[0]) % n[1] == 0:
            c = [abs(n[0]) // n[1]]
        elif abs(n[0]) % n[1] != 0:
            c = [abs(n[0]) // n[1], int(abs(n[0]) % n[1]), n[1]]
    elif abs(n[0]) // n[1] == 0:
        c = [abs(n[0]), n[1]]
    if n[0] < 0:
        c[0] *= -1
    return normalize(c)

def calculate(exp: str):        # привожу к одному оператору
    exp = exp.replace(' - ', ' + -').replace('--', '').split('+')
    a, b = to_lis(exp)
    if a[0] < 0 and b[0] > 0:          # основная математика
        c = [b[0] * a[1] - abs(a[0]) * b[1], a[1] * b[1]]
    elif a[0] > 0 and b[0] < 0:
        c = [a[0] * b[1] - abs(b[0]) * a[1], a[1] * b[1]]
    elif a[0] < 0 and b[0] < 0:
        c = [abs(a[0]) * b[1] + abs(b[0]) * a[1], a[1] * b[1]]
        c[0] *= -1
    else:
        c = [a[0] * b[1] + abs(b[0]) * a[1], a[1] * b[1]]
    return trans_two(c)


n = input('Введите данные для вычисления: ')
print(calculate(n))
