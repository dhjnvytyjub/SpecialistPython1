n = int(input())
if n % 10 == 1 and n % 100 != 11:
    print(n, 'korova')
elif (n % 10 == 2 and n % 100 != 12) or (n % 10 == 3 and n % 100 != 13) or (n % 10 == 4 and n % 100 != 14):
    print(n, 'korovy')
else:
    print(n, 'korov')
