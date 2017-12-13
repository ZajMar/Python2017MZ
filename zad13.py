import random

def RandomMatrixes(min,max):
	for i in range(0,number):
		for j in range(0,number):
			a[i][j]=(random.randint(min, max))
			b[i][j]=(random.randint(min, max))
def CalculateMatrixMultiply(in1,in2):
	for i in range(0,number):
		for j in range(0,number):
			for k in range(0,number):
				c[i][j]+=a[i][k]*b[k][j]


number = 8
a = [[0 for x in range(number)] for y in range(number)] 
b = [[0 for x in range(number)] for y in range(number)] 
c = [[0 for x in range(number)] for y in range(number)] 
RandomMatrixes(1,4)
CalculateMatrixMultiply(a,b)
print(a)
print(b)
print(c)

