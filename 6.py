def cot(x):
    a = {}
    xl = len(x)
    for i in range(0,xl):
        while x[i] > 0:
            if(a.get(x[i]%10) == None):
                a[x[i]%10] = 1
            else:
                a[x[i]%10] += 1
            x[i] //= 10
    
    return a

l = []
while True:
    try:
        x = int(input())
    except EOFError:
        break
    l.append(x)

#print(l)
print(cot(l))