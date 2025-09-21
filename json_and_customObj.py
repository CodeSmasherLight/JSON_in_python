import json

# custom python object(not serializable by default by json module because it is not a built in data type)
class Person:
    def __init__(self, name, age, city, haschildren):
        self.name = name
        self.age = age
        self.city = city
        self.haschildren = haschildren

person = Person("Light", 23, "New Delhi", False)

# ENCODING
# one way to do this is by defining a function and passing it to default parameter of json.dumps method
def encoding_person(obj):
    if isinstance(obj, Person):
        return {
            "name": obj.name,
            "age": obj.age,
            "city": obj.city,
            "haschildren": obj.haschildren,
            obj.__class__.__name__: True
        }
    else:
        raise TypeError("Object of type Person is not JSON serializable")

person_json = json.dumps(person, default=encoding_person, indent=4)
print(person_json)


# Another way to do the same thing is by subclassing JSONEncoder class
# from json import JSONEncoder

# class PersonEncoder(JSONEncoder):

#     def default(self, obj):
#         if isinstance(obj, Person):
#             return {
#                 "name": obj.name,
#                 "age": obj.age,
#                 "city": obj.city,
#                 "haschildren": obj.haschildren,
#                 obj.__class__.__name__: True
#             }
#         return JSONEncoder.default(self, obj)

# # person_json = json.dumps(person, cls=CustomDecoder, indent=4)
# # # or
# person_json = PersonEncoder().encode(person)
# print(person_json)

# DECODING 

# person = json.loads(person_json) # this will convert json string to python dictionary and not to Person object
# print(person)
# print(type(person)) # thsis will print <class 'dict'> and not <class '__main__.Person'>, just to be clear

# to convert it to Person object we can define a function and pass it to object_hook parameter of json.loads method
def decoding_person(dct):
    if Person.__name__ in dct: # we haave added a key with class name while encoding to identify the object type in line 22 or 43
        return Person(
            name=dct["name"],
            age=dct["age"],
            city=dct["city"],
            haschildren=dct["haschildren"]
        )
    return dct

person = json.loads(person_json, object_hook=decoding_person)
print(person.name) # this will print Light coz now person is a Person object and can access attributes of Person class
print(type(person)) # this will print <class '__main__.Person'>


    
