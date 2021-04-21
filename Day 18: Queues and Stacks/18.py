class Solution:
    # Write your code here
    a=[]
    b=[]
    def pushCharacter(self,c):
        self.b.insert(0,c)
        
    def enqueueCharacter(self,c):
        self.a.append(c)
        
    def popCharacter(self):
        c=self.b.pop()
        return c
    def dequeueCharacter(self):
        d=self.a.pop()
        return d
