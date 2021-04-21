#Write your code here
class Calculator():
    def power(self,n,p):
        self.n = n
        self.p = p
        if n>=0 and p>=0:
            a=pow(n,p)
            return a
        else:
            return Exception("n and p should be non-negative")
