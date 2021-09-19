year = {
    'spring': '3 4 5',
    'summer': '6 7 8',
    'autumn': '9 10 11',
    'winter': '1 2 12'
    }
val = input()
for key in year:
    if val in year[key].split():
        print(key)
