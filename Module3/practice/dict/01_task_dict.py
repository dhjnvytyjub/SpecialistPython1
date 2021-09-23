item = {"name": "Кроссовки", "price": "7540.5", "currency": "rub", "count": "10"}
dollar_rate = 74.12
print('%.2f' % (float(item['price']) / dollar_rate * int(item['count'])))
