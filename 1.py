friends = int(input())
points = 0
while friends > -1:
    friends = int(input())
    if friends > points:
        points = friends
print(points)