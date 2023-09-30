a = {1023:"xiaoming",29378:"zhangsan",129271:"lisi",182341:"wangwu"}
b = []
for i in a.items():
    x = int(i[0])
    if(x % 2 == 0):
        b.append(x)

for i in range(0,len(b)):
    del a[b[i]] 
print(a)       