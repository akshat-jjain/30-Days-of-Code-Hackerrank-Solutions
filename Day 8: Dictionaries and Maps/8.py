n=int(input())
dict1={}
for x in range(n):
    s1=input().split()
    dict1[s1[0]]=s1[1]
while True:
    try:
        s2=input()
        if s2 in dict1:
            
            print(s2+"="+dict1[s2])
        else:
            print("Not found")
    except:
        break
