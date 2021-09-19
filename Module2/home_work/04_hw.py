n = int(input())
print('#' * n)
for i in range(1, n - 1):
    print('#', '#'.rjust(n - 2))
print('#' * n)
