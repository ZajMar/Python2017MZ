
def readFile(nameFile):
	inFile = open(nameFile,'r').read()
	print(inFile)

def saveToFile(nameFile):
	outFile = open(nameFile,'w')
	dataToSave = raw_input("Data to write: ")
	outFile.write(str(dataToSave))

saveToFile('test21.txt')
readFile('test21.txt')
