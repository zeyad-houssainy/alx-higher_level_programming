import json


my_dict = {
    "name": "John",
    "age": 25,
    "city": "New York",
    "score": 92,
    "course": "Python Programming",
    "status": "active"
}


# my_dict = json.dumps(my_dict)
print(json.dumps(my_dict))
