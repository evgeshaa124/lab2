DATABASE = []

USER_SCHEME = ("id", "first_name", "second_name", "email", "password")
RECORD_SCHEME = ("id", "date", "content", "user", "title")

users = [
    "User(id=1, first_name=test name, second_name=test surname, email=test@test.test, password=123)",
    "User(id=2, first_name=another test name, second_name=another test surname, email=test1@test.test, password=456)",
    "User(id=3, first_name=test name x1, second_name=test surname x2, email=test123@test.test)",
    "User(id=4, first_name=, second_name=test surname x3, email=train@test.test)",
         ]

records = [
    "Record(id=1, date=26.02.2004, content=Some example #1, user=1, title=Example title)",
    "Record(id=2, date=01.10.2013, content=Some example #2, user=3, title=Example title one)",
    "Record(id=3, date=12.13.2008, content=Some example #3, user=2, title=Example title of user 2)"
]

def create_user(data):
    if len(data) == len(USER_SCHEME):
        user = dict(zip(USER_SCHEME, data))
        DATABASE.append({'type': 'User', **user})
        return "User created"
    return "Invalid user data"

def update_user(user_id, data):
    for item in DATABASE:
        if item.get('type') == 'User' and item.get('id') == user_id:
            for key, value in zip(data[0::2], data[1::2]):
                item[key] = value
            return "User updated"
    return "User not found"

def delete_user(user_id):
    for i, item in enumerate(DATABASE):
        if item.get('type') == 'User' and item.get('id') == user_id:
            del DATABASE[i]
            return "User deleted"
    return "User not found"

def create_record(data):
    if len(data) == len(RECORD_SCHEME):
        record = dict(zip(RECORD_SCHEME, data))
        DATABASE.append({'type': 'Record', **record})
        return "Record created"
    return "Invalid record data"

def update_record(record_id, data):
    for item in DATABASE:
        if item.get('type') == 'Record' and item.get('id') == record_id:
            for key, value in zip(data[0::2], data[1::2]):
                item[key] = value
            return "Record updated"
    return "Record not found"

def delete_record(record_id):
    for i, item in enumerate(DATABASE):
        if item.get('type') == 'Record' and item.get('id') == record_id:
            del DATABASE[i]
            return "Record deleted"
    return "Record not found"

def parse_string(input_str):
    parts = input_str.split(',')
    entity = parts[0].split('(')[0]
    data = [part.split('=')[1].strip() for part in parts]
    return entity, data
