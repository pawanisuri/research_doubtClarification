import xml.etree.ElementTree as ET
import re
from xml.dom.minidom import parse, Node
xmlFile = parse("Introduction_to_Software_Engineering_chaperts.xml")

def findAnswer(xmlFile,startPage,endPage,topic):
    for node1 in xmlFile.getElementsByTagName("article-title") :
        for node2 in node1.childNodes:
            if(node2.nodeType == Node.TEXT_NODE) :
                if(node2.data.encode("utf-8")==topic):
                   print(node2.data.encode("utf-8"))
                   page=xmlFile("page")
                #    print(page)

findAnswer(xmlFile,1,2,"View model")

