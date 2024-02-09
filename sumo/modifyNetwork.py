import xml.etree.ElementTree as ET

networkFile = 'sumo/network.net.xml'

tree = ET.parse(networkFile)
root = tree.getroot()

# Create the 'additional' element and its children
additional = ET.SubElement(root, 'additional')

vTypes = [
    {'id': 'car', 'type': 'car', 'guiShape': 'passenger'},
    {'id': 'bus', 'type': 'bus', 'guiShape': 'bus'},
    {'id': 'bike', 'type': 'bike', 'guiShape': 'motorcycle'}
]

for vType in vTypes:
    ET.SubElement(additional, 'vType', vType)

# Find the 'tlLogic' elements and set their 'duration' attributes
durations = ['60', '5']
for i, tlLogic in enumerate(root.iter('tlLogic')):
    tlLogic.set('duration', durations[i % len(durations)])

# Write the changes back to the file
tree.write(networkFile)
print(f'--> Changed duration of phases in tlLogic in {networkFile}')
print(f'--> Added vehicle types in {networkFile}')