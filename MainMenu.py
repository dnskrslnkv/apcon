import tkinter as tk


from parse_functional.parse_GUI_window import ParseWindow
from database_functional.ViewDB_GUI_window import ViewDB
from nltk_functional.classTextProcessing_GUI_window import TextProcessing
from classification_functional.Classification_GUI_window import ClassificationWindow



class MainMenu:
    """Класс нужен дли инициализации окна главного меню"""

    def __init__(self):
        """В методе __init__ инициализируем окно главного меню, название окна(приложения) и размер окна
           Помимо этого объявляем описание программы в переменной label, добавляем кнопки-функции программы:
           парсинг, просмотр бд с новостями, обработка текста и классификация текста. В нижнем углу добавлена кнопка
           'Справка', в которой указана последовательность действий для корректного запуска функции 'парсинг'"""
        self.window = tk.Tk()
        self.window.title("APCON: MainMenu")
        self.window.geometry("800x500")

        self.create_widgets()
        self.window.mainloop()

    def create_widgets(self):
        # Создание виджета Label с информацией о программе
        self.label_info = tk.Label(self.window, text="Добро пожаловать в APCON!\n"
                                                     "Приложение APCON предназначено для парсинга новостных источников,обработки\n"
                                                     "естественного языка новостных текстов, а также классификации текстов\n"
                                                     "по категориям на основе собранных новостных статей.\n\n"
                                                     "Для правильной работы с программой рекомендуем прочитать раздел 'Справка'\n\n\n"
                                                     "Выберите направление работы:",
                                   font=('Times New Roman', 14), justify="left")
        self.label_info.grid(row=0, column=0, padx=10, pady=10)

        # Создание виджета Button с переходом в диалоговое окно Парсинг
        self.parse_button = tk.Button(self.window, text="Парсинг", command=self.parse, font=('Times New Roman', 14))
        self.parse_button.grid(row=1, column=0, sticky='w', padx=10, pady=10)

        # Создание виджета Button c переходом в окно Просмотр БД новостей
        self.view_db_button = tk.Button(self.window, text="Просмотр БД новостей", command=self.viewDB,
                                        font=('Times New Roman', 14))
        self.view_db_button.grid(row=2, column=0, sticky='w', padx=10, pady=10)

        # Создание виджета Button с переходом в окно Обработка текста
        self.text_proccesing_button = tk.Button(self.window, text="Обработка текста", command=self.textProcessing,
                                                font=('Times New Roman', 14))
        self.text_proccesing_button.grid(row=3, column=0, sticky='w', padx=10, pady=10)

        # Создание виджета Button с переходом в окно Классификация текста
        self.text_classification_button = tk.Button(self.window, text="Классификация текста", command=self.classification,
                                                    font=('Times New Roman', 14))
        self.text_classification_button.grid(row=4, column=0, sticky='w', padx=10, pady=10)

        # Создание виджета Button c переходом в окно Справка
        self.info_button = tk.Button(self.window, text='Справка', command=self.info, font=('Times New Roman', 14))
        self.info_button.grid(row=5, column=0, padx=10, pady=10, sticky='w')

    def parse(self):
        self.window.withdraw()
        ParseWindow(self)

    def viewDB(self):
        self.window.withdraw()
        ViewDB(self)

    def textProcessing(self):
        self.window.withdraw()
        TextProcessing(self)

    def classification(self):
        self.window.withdraw()
        ClassificationWindow(self)

    def info(self):
        self.window.withdraw()
        ReferenceWindow(self)


class ReferenceWindow:
    """Класс нужен дли инициализации окна с текстовой информацией по корректной работе функции парсинг"""

    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel()
        self.window.title("APCON")
        self.window.geometry("1200x250")

        self.create_widgets()

    def create_widgets(self):
        # создание текстового поля с информацией о корректной работе программы
        message_label = tk.Label(self.window, text="Для корректной работы функции «Парсинг» необходимо:\n\n"
                                                   "- наличие браузера Google Chrome;\n"
                                                   "- наличие  в директории с программой приложения chromedriver.exe, версия которого должна СОВПАДАТЬ с версией браузера Google Chrome;\n\n"

                                                   "Скачать chromedriver.exe можно с официального сайта\n"
                                                   "- https://chromedriver.chromium.org/downloads\n\n"
                                                   "Перед запуском функции «Парсинг» ПРОВЕРЬТЕ выполнение этих условий!",
                                 font=('Times New Roman', 14), justify='left')
        message_label.grid(row=0, column=0)

        # создание кнопки "Назад" -> переход в главное меню
        back_button = tk.Button(self.window, text="Назад", command=self.close_info_window, font=('Times New Roman', 14))
        back_button.grid(row=1, column=0)

    def close_info_window(self):
        """Функция необходимо для закрытия окна с текстовой информацией
        по корректной работе функции 'парсинг'"""
        self.window.destroy()
        self.parent.window.deiconify()





