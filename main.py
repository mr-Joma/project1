# HW3
from datetime import datetime

name = input("Введите имя: ")

current_time = datetime.now().strftime("%Y:%m:%d - %H:%M:%S")

print(f"{current_time} - Привет, {name}!")



# import flet as ft

# def main_page(page: ft.Page):
#     page.title = 'Мое первое приложение'
#     page.theme_mode = ft.ThemeMode.LIGHT

#     text_hello = ft.Text(value='Hello world')

#     greeting_history = []
    
# # Добавил переменную для состояния
#     history_visible = True

#     history_text = ft.Text(value='История приветствий: ')

#     text_hello.value = 'Hello Geeks'

#     def on_button_click(_):
#         name = name_input.value

#         if name:
#             text_hello.color = None
#             text_hello.value = f"Hello {name}"

#             name_input.value = None

#             greeting_history.append(name)
            
#             history_text.value = "История приветствий\n" + '\n'.join(greeting_history)
#         else: 
#             text_hello.color = ft.Colors.RED
#             text_hello.value = 'Введите имя'
#             print('Ничего не ввели')
#         page.update()
    
#     def clear_history(_):
#         greeting_history.clear()
#         history_text.value = 'История приветствий: '
        
#         page.update()

#     def toggle_theme(_):
#         if page.theme_mode == ft.ThemeMode.LIGHT:
#             page.theme_mode = ft.ThemeMode.DARK
#         else:
#             page.theme_mode = ft.ThemeMode.LIGHT
#         page.update()

# # Добавил функцию скрыть/показать
#     def toggle_history(_):
#         nonlocal history_visible

#         if history_visible:
#             history_text.visible = False
#             history_visible = False
#         else:
#             history_text.visible = True
#             history_visible = True

#         page.update()
    
#     name_input = ft.TextField(on_submit=on_button_click, label='Введите имя', expand=True)
#     elavated_button = ft.ElevatedButton('send', icon=ft.Icons.SEND, color=ft.Colors.RED,
#                                         icon_color=ft.Colors.GREEN, on_click=on_button_click)
    
#     theme_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=toggle_theme)
#     clear_button = ft.ElevatedButton('Очистить историю', on_click=clear_history)
    
#  # Добавил кнопку 
#     toggle_history_button = ft.ElevatedButton('Скрыть/Показать историю', on_click=toggle_history)   

#     main_object = ft.Row([name_input, elavated_button, theme_button])
#     history_row = ft.Row([history_text, clear_button, toggle_history_button])

#     page.add(text_hello, main_object, history_row)

# ft.app(main_page)



# HW1
# import flet as ft

# def main(page: ft.Page):
#     count = 0
#     text_hello = ft.Text("Нажато: 0 раз")

#     def click(e):
#         nonlocal count
#         count += 1
#         text_hello.value = f"Нажато: {count} раз"
#         page.update()

#     page.add(
#         text_hello,
#         ft.ElevatedButton("Нажми", on_click=click)
#     )

# ft.app(main)


