import os

curPath="/home/marcinzajac/Dokumenty/pyton"
def displayPath(path): 
    for i in os.listdir(path):
	path2 = os.path.join(path, i)
	if os.path.isdir(path2):
        	displayPath(path2)
        else:
		print(path2)	
displayPath(curPath)

