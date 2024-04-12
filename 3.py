citizens = int(input())
counter = 0
s = 0
while citizens > 0:
    s += citizens
    citizens = int(input())
    counter += 1
print(s / counter)