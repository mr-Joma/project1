import flet as ft

def main_page (page: ft.Page):
    page.title = "Мое первое приложение!!"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    text_hello = ft.Text(value="Hello World!!")
    
    greeting_history = []
    
    history_text = ft.Text(value="История приветствий: ")
    
# Поменять значение 
    text_hello.value = "Hello GEEKS!!"

    
    def on_butt_clic(_):
        print(name_input.value)
        name = name_input.value
        
        if name:
            text_hello.color = None
            text_hello.value = f"Hello {name}"
            
            name_input.value = None
            
            greeting_history.append(name)
            
            
            history_text.value = "История приветствий:\n" + '\n'.join(greeting_history)
        else:
            text_hello.color = ft.Colors.RED
            text_hello.value = "Введите имя"
            print("Ничегосне ввели!!")
        page.update()
            
    def clear_history(_):
        greeting_history.clear()
        history_text.value = 'История приветствий: '
        page.update()
    
    def toggle_theme (_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()
    
    
    name_input = ft.TextField(on_submit=on_butt_clic, label="Введите имя", expand=True)
    elevated_button = ft.ElevatedButton('send', icon=ft.Icons.SEND, color=ft.Colors.RED,
                                        icon_color=ft.Colors.GREEN, on_click=on_butt_clic)
    
    theme_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=toggle_theme)
    clear_button = ft.ElevatedButton('Очистить историю', on_click=clear_history)
    
    main_object = ft.Row([name_input, elevated_button, theme_button])
    history_row = ft.Row([history_text, clear_button])
    
    
    page.add(text_hello, main_object, history_text, history_row)

ft.app(main_page)


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



# HW3
# import datetime
# name = input("Введите имя: ")
# now = datetime.datetime.now()
# print(f"{now.year}:{now.month}:{now.day} - {now.hour}:{now.minute}:{now.second} - Привет, {name}!")
