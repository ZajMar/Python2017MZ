import random

def randTab(min,max):
	number = 50
	tab = []
	for i in range(1,number):
		tab.append(random.randint(min, max))
	return tab
	
def Bsort(tab):
	tmp_tab=tab
	for i in range(len(tab)-1,0,-1):
		for j in range(i):
			if tmp_tab[j] > tmp_tab[j+1]:
				tmp_tab[j], tmp_tab[j+1] = tmp_tab[j+1], tmp_tab[j]
	return tmp_tab

randNum=randTab(1,100)
print("Init numbers: ",randNum)
print("Sorted: ",Bsort(randNum))