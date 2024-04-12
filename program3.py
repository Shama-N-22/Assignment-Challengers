t = int(input())

while t > 0:
    a, b, c = map(int, input().split())
    if a==b or a==c or b==c:
        print("NO")
    else:
        print("YES")
    
    t -= 1
