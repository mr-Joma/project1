import flet as ft
from datetime import datetime


def main_page(page: ft.Page):
    page.title = "Мое первое приложение!!"
    page.theme_mode = ft.ThemeMode.LIGHT

    text_hello = ft.Text(value="Hello World!!")
    greeting_history = []

    history_text = ft.Text(value="История приветствий:")

    def update_history(data=None, title="История приветствий:"):
        if data is None:
            data = greeting_history

        if data:
            history_text.value = title + "\n" + "\n".join(
                f"{item['name']} - {item['time'].strftime('%H:%M')}"
                for item in data
            )
        else:
            history_text.value = title + "\nПусто"

        page.update()

    def on_butt_clic(_):
        name = name_input.value

        if name:
            text_hello.color = None
            text_hello.value = f"Hello {name}"

            current_time = datetime.now()

            greeting_history.append({"name": name, "time": current_time})

            # Оставляем только последние 5
            greeting_history[:] = greeting_history[-5:]

            name_input.value = ""

            update_history()
        else:
            text_hello.color = ft.Colors.RED
            text_hello.value = "Введите имя"

        page.update()

    def clear_history(_):
        greeting_history.clear()
        update_history()

    def toggle_theme(_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT

        page.update()

    def show_morning(_):
        morning = [
            item for item in greeting_history
            if item["time"].hour < 12
        ]
        update_history(morning, "Утренние приветствия:")

    def show_evening(_):
        evening = [
            item for item in greeting_history
            if item["time"].hour >= 12
        ]
        update_history(evening, "Вечерние приветствия:")

    name_input = ft.TextField(on_submit=on_butt_clic, label="Введите имя", expand=True)

    elevated_button = ft.ElevatedButton("send", icon=ft.Icons.SEND, color=ft.Colors.RED, 
                                        icon_color=ft.Colors.GREEN, on_click=on_butt_clic)

    theme_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6,on_click=toggle_theme)
    clear_button = ft.ElevatedButton("Очистить историю", on_click=clear_history)

    morning_button = ft.ElevatedButton("Утренние", on_click=show_morning)
    evening_button = ft.ElevatedButton("Вечерние",on_click=show_evening)

    main_object = ft.Row([name_input, elevated_button, theme_button])
    buttons_row = ft.Row([clear_button, morning_button, evening_button])

    page.add(text_hello, main_object, buttons_row, history_text)


ft.app(main_page) 


