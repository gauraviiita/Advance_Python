import json
person = {"name": "John", "age": 30, "city": "New York", "hasChildren":False, "titles": ["engineer", "programmer"]}

personJSON = json.dumps(person, indent=4, sort_keys=True)#separators=(', ','= ')
#print(personJSON)

# convert from json to string python
#person = json.loads(personJSON)
#print(person)
with open('person.json', 'r') as file:
    person = json.load(file)
    print(person)
