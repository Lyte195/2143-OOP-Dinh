""""
Name: Luong Dinh
Email: ldinh195@gmail.com
Assignment: Homework 2 - Add Fraction Class
Due: 26 Sep @ 1:00 p.m.
""""
def gcd(a, b):
    while b:      
        a, b = b, a % b
    return a

class fraction(object):
    def __init__(self,n=None,d=None):
        self.numerator = n
        self.denominator = d
        self.reduce()

    def __str__(self):
        return "%s / %s" % (self.numerator , self.denominator)

    def numerator(self,n):
        self.numerator = n 

    def denominator(self,d):
        self.denominator = d
        
	def reduce(self):
		thegcd = gcd(self.numerator,self.denominator)
    	self.numerator /= thegcd
        self.denominator /= thegcd

    def __add__(self,rhs):
        num = self.numerator*rhs.denominator + self.denominator*rhs.numerator
        denom = self.denominator*rhs.denominator
        if(num == denom):
        	return 1
        else:
        	return fraction(num,denom)
        	

if __name__ == '__main__':
    a = fraction(3,2)
    b = fraction(4,5)
    c = a + b
    print(fraction.__str__(c))  
