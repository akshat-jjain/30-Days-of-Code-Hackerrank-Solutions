class Student(Person):
    def __init__(self, firstName, lastName, idNumber,scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores=scores
    def calculate(self):
        a=0
        for x in self.scores:
            a+=x
        a=a/len(self.scores)     
        if 90 <= a <= 100:
            return 'O'
        elif 80<=a<=90:
            return 'E'
        elif 70<=a<=80:
            return 'A'
        elif 55<=a<=70:
            return 'P'
        elif 40<=a<=55:
            return 'D'
        elif a<40:
            return 'T'
