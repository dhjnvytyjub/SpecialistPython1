n, m, k = [int(input()) for i in range(3)]
print('YES' if n <= k >= m and (k % n == 0 or k % m == 0) else 'NO')
