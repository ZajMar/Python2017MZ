import math


class Complex():
	real=0
	imag=0

	def __init__(self, real, imag=0.0):
		self.real = real
		self.imag = imag
	
	def __str__(self):
		return '(%s, %s)' % (self.real, self.imag)
	
	def add(x,y):
		return Complex(x.real+y.real,x.imag+y.imag)
	
	def sub(x,y):
		return Complex(x.real-y.real,x.imag-y.imag)
	
	def mod(self):
		return math.sqrt(self.real*self.real+self.imag*self.imag)

	def _sub_(self,other):
		return Complex(self.real-other.real,self.imag-other.imag)

	def _add_(self,other):
		return Complex(self.real+other.real,self.imag+other.imag)

	def neg(self):
		return Complex(-self.real,-self.imag)

a = Complex (1.0,1.0)
b=Complex(3.0,4.0)
print("a = "+str(a))
print("b = "+str(b))
print("Sum: ")
print(b.add(a))
print("Mod: ")
print(a.mod())
print("Neg: ")
print(b.neg())

