# Add your code here
def computeDifference(self):
    b = []
    a.sort()
    for x in range(len(a)) :
        if x == len(a)-1 :
            b.append(abs(a[0]-a[x]))
        else :
            b.append(abs(a[x]-a[x+1]))
    b.sort()
    self.maximumDifference = b[len(b)-1]
