# here serialization/encoding means converting python objects to json format
# and deserialization/decoding means converting json format to python objects
import json

person = {
    "name": "Light",
    "age": 23,
    "city": "New Delhi",
    "haschildren": False,
    "occupation": ["Software Engineer", "Programmer"]
}

# ENCODING
# converting python object to json string
person_json = json.dumps(person, indent=4) # dump's' means string
print(person_json)

# writing json to a file
with open("person.json", "w") as file:
    json.dump(person, file, indent=4) # converting python object to json file(dump means file)

# DECODING
# converting json string to python object
person = json.loads(person_json) # load's' means it will take content from json string(here person_json is json string)
print(person)

# reading json from a file and converting to python object
with open("person.json", "r") as file:
    person = json.load(file) # load means it will take content from json file
    print(person)

