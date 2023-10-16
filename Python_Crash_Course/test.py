users = {
    'dsaechao': {
        'first_name': 'Dominic',
        'last_name': 'Saechao',
        'age': 27,
        'location': 'SJ'
    },
    'jchan': {
        'first_name': 'Josephine',
        'last_name': 'Chan',
        'age': 28,
        'location': 'SJ'
    },
    'aflores': {
        'first_name': 'Alan',
        'last_name': 'Flores',
        'age': 27,
        'location': 'SAC'
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first_name']} {user_info['last_name']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location}")