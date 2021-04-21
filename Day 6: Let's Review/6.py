n=int(input())
arr1=[]
for x in range(n):
    arr1.append(input())
for x in arr1:
    e=""
    o=""
    for y in range(0,len(x),2):
        e+=x[y]
    for y in range(1,len(x),2):
        o+=x[y]
    print(e+" "+o)
