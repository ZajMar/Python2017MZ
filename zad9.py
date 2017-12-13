
def deleteFromFile(inputFile,outputFile):
	words = [' się ', 'oraz ', 'dlaczego ', 'nigdy ', ' i ']
	inFile = open(inputFile,'r')
	outFile = open(outputFile,'w')
	outFile.write(inFile.read())
	inFile.close()
	for word in words:
		outFile.close()
		tmp = open(outputFile,'r').readlines()
		outFile = open(outputFile,'w')
		for i in tmp:
			outFile.write(i.replace(word," "))



deleteFromFile('test.txt','output.txt')