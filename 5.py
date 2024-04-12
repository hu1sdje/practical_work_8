n = int(input())
def divs(x):
    divs = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            divs.append(i)
            if i != x // i:
                divs.append(x // i)
    return sorted(divs)


counter = 0
for i in range(2, n + 1):
    if sum(divs(i)) == 2 * i:
        counter += 1
print(counter)
