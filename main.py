from bs4 import BeautifulSoup
import requests

users: list = [
    {'name': 'Kasia', 'location': 'Warszawa', 'posts': 3, 'img_url': '' },
    {'name': 'Asia', 'location': 'Wrocław', 'posts': 5,  'img_url': '' },
    {'name': 'Basia', 'location': 'Kraków', 'posts': 7, 'img_url': '' },
]

def get_coordinates(city_name:str)->list:
    url: str = f'https://pl.wikipedia.org/wiki/{city_name}'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    # print(response.text)
    response_html = BeautifulSoup(response.text, "html.parser")
    # print(response_html.prettify())

    latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
    longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
    return([latitude, longitude])

def get_map(users_data: list) -> None:
    import folium
    m = folium.Map(location=[52.23, 21.0], zoom_start=6)
    for user in users_data:
        folium.Marker(
            location=get_coordinates(user['location']),
            tooltip="Click me!",
            popup=f"<h5> user:</h5><h3>{user['name']}</h3> \n {user['location']}\n{user['posts']} <img src=f'{user['img_url']}' alt='1'/> ",
            icon=folium.Icon(icon="cloud"),
        ).add_to(m)
    m.save('index.html')

def user_info(users_data: list) -> None:
    for user in users_data:
        print(f'Twój znajomy {user['name']} w miejscowości {user['location']} opublikował {user["posts"]} postów.')

def add_user(users_data: list)->None:
    name:str=input('Podaj imię nowego znajomego: ')
    location:str=input('Podaj nazwę miejscowości: ')
    post:int=int(input('Podaj liczbę postów: '))
    img_url:str=input('Podaj adres url zdjęcia: ')
    users_data.append({'name': name, 'location': location, 'posts': post, 'img_url': img_url})

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
    print('==========================MENU================================')
    print('0. Wyjście z programu')
    print('1. Wyświetlanie znajomego')
    print('2. Dodaj znajomego')
    print('3. Usuń znajomego')
    print('4. Aktualizuj znajomego')
    print('5. Generuj mapę')
    print('==============================================================')
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
    if temp_choice == 5:
        print('Wybrano funkcję pokazywania mapy użytkowników')
        get_map(users)