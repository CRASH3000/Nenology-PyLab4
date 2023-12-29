import json


def parse_xml_to_dict(xml_string):
    people = []
    person = {}
    for line in xml_string.splitlines():
        if '<person>' in line:
            person = {}
        elif '</person>' in line:
            people.append(person)
        else:
            start = line.find('<') + 1
            end = line.find('>')
            if start != 0 and end != -1:
                tag = line[start:end]
                value_start = end + 1
                value_end = line.find('</', value_start)
                value = line[value_start:value_end].strip()
                person[tag] = value
    return people


with open('people.xml', 'r', encoding='utf-8') as file:
    xml_content = file.read()

people_data = parse_xml_to_dict(xml_content)

json_output = json.dumps(people_data, ensure_ascii=False, indent=4)
with open('people.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_output)
