a = []
x = int(input())
y = int(input())
z = int(input())
a.append(x)
a.append(y)
a.append(z)

a.sort(key=None,reverse=True)

for i in range(0,3):
    print(a[i])