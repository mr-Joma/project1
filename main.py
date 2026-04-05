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
            
    
    
    name_input = ft.TextField(on_submit=on_butt_clic, label="Введите имя", expand=True)
    elevated_button = ft.ElevatedButton('send', icon=ft.Icons.SEND, color=ft.Colors.RED,
                                        icon_color=ft.Colors.GREEN, on_click=on_butt_clic)
    
    main_object = ft.Row([name_input, elevated_button])
    
    
    page.add(text_hello, main_object, history_text)

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
