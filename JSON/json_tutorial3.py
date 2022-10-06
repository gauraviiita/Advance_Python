import json

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('Max', 27)

def encode_user(o):
    if isinstance(o, User):
        return {'name':o.name, 'age':o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type user is not JSON serializable')

#userJSON = json.dumps(user, default=encode_user)
#print(userJSON)


from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age':o.age, o.__class__.__name__:True}
        return JSONEncoder.default(self, o)
userJSON = json.dumps(user, cls=UserEncoder)
print(userJSON)

userJSON = UserEncoder().encode(user)
print(userJSON)
print(type(userJSON))
user = json.loads(userJSON)
print(user)
print(type(user))

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct

user = json.loads(userJSON, object_hook=decode_user)
print(type(user))
print(user.name)
