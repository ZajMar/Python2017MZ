
def InputData():
	VecSize = float(input("Vector size= "))
	if VecSize<1:
		print("Wrong size")
	else:
		for i in range(1,int(VecSize)+1):
			a.append(float(input("vec1[" + str(i) +"]=")))
		for i in range(1,int(VecSize)+1):
			b.append(float(input("vec2[" + str(i) +"]=")))

a = []
b = []
InputData()
sum=0;
for i in range(len(a)):
   sum += a[i] * b[i]

print(sum)