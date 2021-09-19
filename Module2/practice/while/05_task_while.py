n = int(input())
mtx = [[' '] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j or i == n - j - 1:
            mtx[i][j] = '#'
    print(*mtx[i])
