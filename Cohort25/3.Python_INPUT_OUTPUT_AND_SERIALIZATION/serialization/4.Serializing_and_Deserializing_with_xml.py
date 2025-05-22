import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    return {child.tag: child.text for child in root}

# Usage
sample_dict = {"name": "John", "age": "28", "city": "New York"}
serialize_to_xml(sample_dict, "data.xml")
print(deserialize_from_xml("data.xml"))