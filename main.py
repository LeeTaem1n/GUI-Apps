import flet as ft
import requests
def main(page: ft.Page):
    page.title = "Weather App"
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    user_data = ft.TextField(label='Name city', width=300)
    weather_data = ft.Text()  

    def get_info(e):
        if len(user_data.value) < 2:
            return
        API = '1fdaed18881e845b590b9c7822c26672'
        URL = f'https://api.openweathermap.org/data/2.5/weather?q={user_data.value}&appid={API}&units=metric'
        res = requests.get(URL).json()
        tenp = res['main']['temp']
        weather_data.value = f'Temperature: {tenp}°C'
        page.update()

    def change_theme(e):
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
        page.update()
    
    page.add(
        ft.Row(
        [
            ft.IconButton(ft.Icons.SUNNY, on_click=change_theme),
            ft.Text("Weather App")
        ],
        alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([user_data],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([weather_data],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.ElevatedButton("Get Weather", on_click=get_info)],alignment=ft.MainAxisAlignment.CENTER)
    )


ft.app(target=main)