n = input()

for i in range(int(n)):
    num1,num2,num3 = input().split(" ")
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)
    
    if num2>num1:
        num2,num1 = num1,num2
        
    if num3 > num2 and num3 < num1:
        num3,num2 = num2,num3
    
    if num3 > num1:
        num1,num2,num3 = num3,num1,num2
    
    print(num2)