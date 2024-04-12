s1 = ''
k1 = 0
s2 = ''
k2 = 0
s3 = ''
for i in range(1, 10):
    s1 += str(i)
    k1 = int(s1) * 8 + i
    print(f'{s1} * 8 + {i} = {k1}')

for i in range(1, 10):
    s2 += str(i)
    k2 = int(s2) * 9 + i + 1
    print(f'{s2} * 9 + {i + 1} = {k2}')

for i in range(1, 10):
    s3 += '1'
    k3 = int(s3) ** 2
    print(f'{s3} * {s3} = {k3}')
