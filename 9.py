def is_prime(x):
    d = 2
    while x % d != 0:
        d += 1
    return d == x


n = int(input())
for i in range(2, n + 1):
    if is_prime(i):
        print(i)
