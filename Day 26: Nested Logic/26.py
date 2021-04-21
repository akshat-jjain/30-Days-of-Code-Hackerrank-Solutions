ad, am, ay=input().split()
ed, em,ey=input().split()
fine=1
if int(ay)!=int(ey):
    if int(ay)>int(ey):
        fine=10000
    else:
        fine=0
elif int(ay)==int(ey) and int(em)!=int(am):
    if int(am)>int(em):

        fine=500*(int(am)-int(em))
    else:
        fine=0    
    

elif int(ad)!=int(ed) and int(am)==int(em) and int(ay)==int(ey):
    if int(ad)>int(ed):

        fine=abs(15*(int(ad)-int(ed)))
    else:
        fine=0
elif n1==n:
    fine=0

print(fine)
