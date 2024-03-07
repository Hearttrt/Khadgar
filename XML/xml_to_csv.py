from xml.etree.ElementTree import iterparse
import csv

def parse_xml_to_csv(filename):
    with open('xml_to_csv.csv', "w", newline="", encoding='utf-8-sig') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Group Name", "Item Name", "Dropdown Name", "Key", "Value", "Type", "Data"])

        group_name, item_name, dropdown_name = None, None, None

        for event, elem in iterparse(filename, events=('start', 'end')):
            if event == 'start':
                if elem.tag == 'Group':
                    group_name = elem.attrib.get("Name")
                    print(group_name)
                elif elem.tag == 'Item':
                    item_name = elem.attrib.get("Name")
                elif elem.tag == 'Dropdown':
                    dropdown_name = elem.attrib.get("Name").split('#')[-1]
                elif elem.tag in ['Current', 'Default']:
                    dropdown_name = 'Current/Default'        
                    
            elif event == 'end':
                key = elem.attrib.get("Key")
                value = elem.attrib.get("Value")
                type_ = elem.attrib.get("Type")
                data = elem.attrib.get("Data")
                if dropdown_name == None:
                    dropdown_name = "CheckBox"
                if key and value and type_ and data:
                    csvwriter.writerow([group_name, item_name, dropdown_name, key, value, type_, data])

                elem.clear()
            
parse_xml_to_csv('Data.xml')