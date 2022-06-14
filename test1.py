numbers = [2, 7, 11, 15]
target = 17
for x in numbers:
    for y in numbers:
        if x+y==target:
            print(x,y)