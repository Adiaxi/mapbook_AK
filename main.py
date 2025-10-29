users: list = [
    {'name': 'Adrian', 'location': 'Wieluń', 'post': 4},
    {'name': 'Patrycja', 'location': 'Warszawa', 'post': 26},
    {'name': 'Andrzej', 'location': 'Toruń', 'post': 100},
]


def user_info(users_data: list) -> None:
    for user in users_data:
        print(f'Twój znajomy {user['name']} w miejscowości {user['location']} opublikował {user["post"]} postów.')


while True:
    temp_choice: int = int(input('Wybierz opcję menu: '))
    if temp_choice == 0:
        break
    if temp_choice == 1:
        print('Wybrano funkcję wyświetlania aktywności znajomych')
        user_info(users)
    if temp_choice == 2:
        print('Wybrano funkcję dodawania znajomego')
    if temp_choice == 3:
        print('Wybrano funkcję usuwania znajomych')
    if temp_choice == 4:
        print('Wybrano funkcję aktualizacji danych znajomego')
