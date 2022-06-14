
with open('sample.txt') as f:
    lines = f.readlines()
    for i in lines:
        print(i)

with open('output.txt', 'w') as f:
    f.write("my first file\n")
    f.write("This file\n\n")
    f.write("contains three lines\n")