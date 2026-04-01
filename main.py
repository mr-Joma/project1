# import flet as ft

# def main_page (page: ft.Page):
#     page.title = "Мое первое приложение!!"
#     page.theme_mode = ft.ThemeMode.LIGHT
    
#     text_hello = ft.Text(value="Hello World!!")
    
# # Поменять значение 
#     text_hello.value = "Hello GEEKS!!"

#     name_input = ft.TextField()
    
#     elevated_button = ft.ElevatedButton('send', icon=ft.Icons.SEND, color=ft.Colors.RED, icon_color=ft.Colors.GREEN)
#     text_button = ft.TextButton('send')
#     icon_button = ft.IconButton(icon=ft.Icons.SEND)
    
#     page.add(text_hello, name_input, elevated_button, text_button,icon_button)

# ft.app(main_page)

# HW1
import flet as ft

def main(page: ft.Page):
    count = 0
    text_hello = ft.Text("Нажато: 0 раз")

    def click(e):
        nonlocal count
        count += 1
        text_hello.value = f"Нажато: {count} раз"
        page.update()

    page.add(
        text_hello,
        ft.ElevatedButton("Нажми", on_click=click)
    )

ft.app(main)
