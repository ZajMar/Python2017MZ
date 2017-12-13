import re

def Replace(nameFileIn,nameFileOut):
	words = {'i ': 'oraz ', 'oraz ': 'i ', 'nigdy': 'prawie nigdy', 'dlaczego': 'czemu', ' i ': ' oraz ',' i': ' oraz','^i ': 'oraz '}
	input = open(nameFileIn).read()
	for w1,w2 in words.items():
		input = re.sub(w1, w2,input)

	open(nameFileOut, 'w').write(input)
	
Replace("testZad10.txt","outZad10.txt")