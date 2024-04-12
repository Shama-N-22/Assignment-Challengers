t = int(input())

while t > 0:
    x, y, z = map(int, input().split())

    money = x*5 + y*10
    numOfChocolates = int(money/z)
    print(numOfChocolates)
    
    t -= 1
