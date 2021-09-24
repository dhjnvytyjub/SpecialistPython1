def lucky_ticket(t_n):
    if len(str(t_n)) == 6:
        if t_n % 10 + t_n % 100 // 10 + t_n % 1000 // 100 == t_n % 10000 // 1000 + t_n % 100000 // 10000 + t_n % 1000000 // 100000:
            return'Билет', t_n, 'счастливый'
        else:
            return 'Билет', t_n, 'несчастливый'
    else:
        return 'Билет',t_n, 'недействительный'


print(*lucky_ticket(123006))
print(*lucky_ticket(12321))
print(*lucky_ticket(436751))
