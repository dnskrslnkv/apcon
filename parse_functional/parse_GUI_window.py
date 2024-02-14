import tkinter as tk

from tkinter import StringVar, OptionMenu, messagebox
from settings.settingsHTMLsearch import url_path
from settings.settingsSELENIUM import create_settings
from parse_functional.classParse import ParseNews



class ParseWindow:
    """Класс нужен для инициализации окна с функцией парсинга.
        В окне находится поле с выпадающим списком доступных сайтов для парсинга,
        а также поле с вводом количества новостных страниц"""

    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel()
        self.window.title("APCON: Parse")
        self.window.geometry("1000x600")
        self.create_widgets()

    def create_widgets(self):
        # Создание виджета Label для функции выбора сайта
        self.label_site_name = tk.Label(self.window, text="Выберите сайт: ", font=('Times New Roman', 14))
        self.label_site_name.grid(row=0, column=0, sticky='w')

        # Создание переменной для хранения выбранного значения из списка сайтов
        self.selected_value = StringVar(self.window)

        # Создание выпадающего список сайтов
        self.droplist = OptionMenu(self.window, self.selected_value, *url_path.keys())
        self.droplist.grid(row=0, column=1, sticky='w')

        # Создание виджета Label и Entry для ввода количества новостей
        self.label_count_news = tk.Label(self.window, text='Количество новостей: ', font=('Times New Roman', 14))
        self.label_count_news.grid(row=1, column=0, sticky='w')

        self.entry_count_news = tk.Entry(self.window)
        self.entry_count_news.grid(row=1, column=1, sticky='w')

        # Создание виджета Button для запуска функции Парсинг
        self.start_button = tk.Button(self.window, text="Запуск", command=self.StartParse,
                                      font=('Times New Roman', 14))
        self.start_button.grid(row=0, column=4)

        # Создание виджета Button для функции Назад
        self.back_button = tk.Button(self.window, text="Назад", command=self.close_ParseWindow,
                                     font=('Times New Roman', 14))
        self.back_button.grid(row=0, column=5)

    def StartParse(self):
        try:
            value = ParseNews(int(self.entry_count_news.get()), self.selected_value.get(), create_settings())
            value.collecting_links()
            value.collecting_info()
            value.save_information()
            messagebox.showerror("Информация", f" Парсинга сайта {self.selected_value.get()} успешно завершен"
                                 , icon="info")
        except:
            messagebox.showerror("Ошибка", f"Произошла ошибка при выполнении парсинга сайта {self.selected_value.get()}"
                                 , icon="error")

    def close_ParseWindow(self):
        self.window.destroy()
        self.parent.window.deiconify()