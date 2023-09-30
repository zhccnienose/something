def pd(x):
    l = len(x)
    for i in range(0,l):
        if(x[i] < '1' or x[i] > '9'):
            return False
    return True

a = []
while True:
    try:
        x = input()
    except EOFError:
        break
     
    if(pd(x)):
        a.append(int(x))
 
a.sort(reverse=True)       
print(a)