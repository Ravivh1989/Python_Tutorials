userInput = int(input("enter the value:"))
if userInput == userInput[::-1]:
    print('YES')
else:
    print('NO')