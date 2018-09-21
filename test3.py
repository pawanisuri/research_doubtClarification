import xml.etree.ElementTree as ET
tree = ET.parse('SRSDocument-Learning tool.xml')
root = tree.getroot()

for heading in root.findall('body'):
  
  print(heading)