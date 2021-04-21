import math

n1=int(input())
for x in range(n1):
    n=int(input())
    check=True
    
    if math.sqrt(n) in [1,2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
        print("Not prime")
    else:    
        for x in range(2,int(math.sqrt(n))):
                 
            if n%x==0:
                check=False
                break
        
            
        if check:
            print('Prime')
       
        else:
            print('Not prime')
