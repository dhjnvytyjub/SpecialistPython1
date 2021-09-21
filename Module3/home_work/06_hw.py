m = []
for item in items:
    m.append(item['brand'])
print("Товары на складе представлены брэндами: ", end=' ')
print(*set(m))

freq_set = dict((i, m.count(i)) for i in m)
f_s_max = (max(freq_set, key=freq_set.get))
print("На складе больше всего товаров брэнда(ов): ", end=' ')
for k in freq_set:
    if freq_set[k] == freq_set[f_s_max]:
        print(k, end=' ')
print()
        
m = []
for item in items:
    m.append(item['price'])
max_price = max(m)
print("На складе самый дорогой товар брэнда(ов): ", end=' ')
for item in items:
    if item['price'] == max_price:
        print(item['brand'], end=' ')
