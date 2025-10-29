users: list = [
    {'name': 'Adrian', 'location': 'Wieluń', 'posts': 4},
    {'name': 'Patrycja', 'location': 'Warszawa', 'posts': 26},
    {'name': 'Kasia', 'location': 'Lublin', 'posts': 12},
]


def user_info(users_data: list) -> None:
    for user in users_data:
        print(f'Twój znajomy {user['name']} w miejscowości {user['location']} opublikował {user["posts"]} postów.')

def add_user(users_data: list)->None:
    name:str=input('Podaj imię nowego znajomego: ')
    location:str=input('Podaj nazwę miejscowości: ')
    post:int=int(input('Podaj liczbę postów: '))
    users_data.append({'name': name, 'location': location, 'posts': post})

def remove_user(users_data: list)->None:
    temp_name:str= input('Podaj imię użytkownika do usunięcia z listy znajomych: ')
    for user in users_data:
        if user['name'] == temp_name:
            users.remove(user)

def update_user(users_data: list)->None:
    temp_name:str= input('Podaj imię użytkownika do aktualizacji: ')
    for user in users_data:
        if user['name'] == temp_name:
            user['name']=input('Podaj nowe imie: ')
            user['location']=input('Podaj nową miejscowość: ')
            user['posts']=input('Podaj nową ilość postów: ')

while True:
    temp_choice: int = int(input('Wybierz opcję menu: '))
    if temp_choice == 0:
        break
    if temp_choice == 1:
        print('Wybrano funkcję wyświetlania aktywności znajomych')
        user_info(users)
    if temp_choice == 2:
        print('Wybrano funkcję dodawania znajomego')
        add_user(users)
    if temp_choice == 3:
        print('Wybrano funkcję usuwania znajomych')
        remove_user(users)
    if temp_choice == 4:
        print('Wybrano funkcję aktualizacji danych znajomego')
        update_user(users)