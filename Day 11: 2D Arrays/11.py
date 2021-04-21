s=[]
for x in range(6):
    s.append(input())
a=[]
sizes=[]
for x in s:
   a.append(x.split())
row=[]
sum1=[]
w=[]
for k in range(4):
    for z in range(4): 
        e=[]
        for x in range(3):
            e.append(a[x+k][z])
            e.append(a[x+k][z+1])
            e.append(a[x+k][z+2])
        w.append(e)
sums=[]
for x in range(16):
    c=0
    for y in range(9):
        if y!=3 and y!=5:
            c+=int(w[x][y])
    sums.append(c)
max1=-63
for x in sums:
    if x>max1:
        max1=x
print(max1)     
