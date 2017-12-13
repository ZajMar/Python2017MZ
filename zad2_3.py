import os
from xml.dom.minidom import parse
import xml.dom.minidom


DOMdoc = xml.dom.minidom.parse("test.xml")
collection = DOMdoc.documentElement

players = collection.getElementsByTagName("player")

for i in players:
	print "Players:"
	print("Name: %s" % i.getAttribute("name"))	
	power=i.getElementsByTagName('power')[0]
	print("Power: %s" % power.childNodes[0].data)
	speed=i.getElementsByTagName('speed')[0]
	print("Speed: %s" % speed.childNodes[0].data)
	desc=i.getElementsByTagName('desc')[0]
	print("Description: %s" % desc.childNodes[0].data)

players[0].getElementsByTagName('desc')[0].firstChild.replaceWholeText("test")
fileOut = open("testOutput.xml", "w")
collection.writexml(fileOut)
fileOut.close()
