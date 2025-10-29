users: list = [
    {'name': 'Adrian', 'location': 'Wieluń', 'post': 4},
    {'name': 'Patrycja', 'location': 'Warszawa', 'post': 26},
    {'name': 'Andrzej', 'location': 'Toruń', 'post': 100},
]

for user in users:
    print(f'Twój znajomy {user['name']} w miejscowości {user['location']} opublikował {user["post"]} postów.')
