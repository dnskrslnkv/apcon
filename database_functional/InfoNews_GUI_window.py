import tkinter as tk

from model import News

from nltk_functional.classFrequencyBuilder_GUI_window import GraphFrequencyBuilder
from nltk_functional.classWordCloudBuilder_GUI_window import GraphWordCloudBuilder


class InfoNews:
    """Класс нужен дли инициализации окна  общей информацией о выбранной из БД статьи"""

    def __init__(self, parent, list_info):
        self.parent = parent
        self.window = tk.Toplevel()
        self.window.title("APCON: InfoNews")
        self.window.state("zoomed")

        self.list_info = list_info
        self.query = News.select().where(News.text_article == self.list_info)

        self.create_widgets()

    def create_widgets(self):
        # Создаем виджет Label и добавляем вводный текст
        self.label_common_info = tk.Label(self.window, text="Общая информация о выбранной статье:\n\n",
                                          font=('Times New Roman', 14), justify="left")
        self.label_common_info.grid(row=0, column=0)

        # Создаем виджет Text и добавляем текст с названием выбраного сайта
        self.label_name_site = tk.Label(self.window, text="Название сайта:",
                                        font=('Times New Roman', 14), justify="left")
        self.label_name_site.grid(row=1, column=0, sticky='w')

        self.label_name_site_value = tk.Text(self.window, wrap='word', width=50, height=1)
        self.label_name_site_value.insert('1.0', [el.name_site for el in self.query][0])
        self.label_name_site_value.grid(row=1, column=1, sticky='w')

        # Создаем виджет Label и добавляем текст с категорией выбранной статьи
        self.label_category = tk.Label(self.window, text="Категория:",
                                       font=('Times New Roman', 14), justify="left")
        self.label_category.grid(row=2, column=0, sticky='w')

        self.label_category_value = tk.Text(self.window, wrap='word', width=50, height=1)
        self.label_category_value.insert('1.0', [el.category for el in self.query][0])
        self.label_category_value.grid(row=2, column=1, sticky='w')

        # Создаем виджет Label и добавляем текст с датой публикации выбранной статьи
        self.label_date = tk.Label(self.window, text="Дата публикации:",
                                   font=('Times New Roman', 14), justify="left")
        self.label_date.grid(row=3, column=0, sticky='w')

        self.label_date_value = tk.Text(self.window, wrap='word', width=50, height=1)
        self.label_date_value.insert('1.0', [el.date_of_publication for el in self.query][0])
        self.label_date_value.grid(row=3, column=1, sticky='w')

        # Создаем виджет Label и добавляем текст с ссылкой выбранной статьи
        self.label_link = tk.Label(self.window, text="Ссылка:",
                                   font=('Times New Roman', 14), justify="left")
        self.label_link.grid(row=4, column=0, sticky='w')

        self.label_link_value = tk.Text(self.window, wrap='word', width=100, height=1)
        self.label_link_value.insert('1.0', [el.link for el in self.query][0])
        self.label_link_value.grid(row=4, column=1, sticky='w')

        # Создаем виджет Label и добавляем текст с заголовком выбранной статьи
        self.label_title = tk.Label(self.window, text="Заголовок:",
                                    font=('Times New Roman', 14), justify="left")
        self.label_title.grid(row=5, column=0, sticky='w')

        self.label_title_value = tk.Text(self.window, wrap='word', width=100, height=2)
        self.label_title_value.insert('1.0', [el.title for el in self.query][0])
        self.label_title_value.grid(row=5, column=1, sticky='w')

        # Создаем виджет Label и добавляем текст с содержимым выбранной статьи
        self.label_article = tk.Label(self.window, text="Содержимое:",
                                      font=('Times New Roman', 14), justify="left")
        self.label_article.grid(row=6, column=0, sticky='w')

        self.label_article_value = tk.Text(self.window, wrap='word', width=100, height=20)
        self.label_article_value.insert('1.0', [el.text_article for el in self.query][0])
        self.label_article_value.grid(row=6, column=1, sticky='w')

        # Создаем виджет Label и добавляем текст с названием выбраного сайта
        self.label_nltk_analysis = tk.Label(self.window, text="Возможные функции обработки текста:\n\n",
                                            font=('Times New Roman', 14), justify="left")
        self.label_nltk_analysis.grid(row=8, column=0)

        self.frequency_graph_button = tk.Button(self.window, text='График частотности слов',
                                                command=self.frequency_graphic,
                                                font=('Times New Roman', 14))
        self.frequency_graph_button.grid(row=9, column=0)

        self.wordcloud_graph_button = tk.Button(self.window, text='Облако слов',
                                                command=self.wordcloud_graphic,
                                                font=('Times New Roman', 14))
        self.wordcloud_graph_button.grid(row=10, column=0)

        self.back_button = tk.Button(self.window, text="Назад", command=self.close_info_window,
                                     font=('Times New Roman', 14))
        self.back_button.grid(row=11, column=0)

    def frequency_graphic(self):
        self.window.withdraw()
        GraphFrequencyBuilder(self, [el.text_article for el in self.query][0])

    def wordcloud_graphic(self):
        self.window.withdraw()
        GraphWordCloudBuilder(self, [el.text_article for el in self.query][0])

    def close_info_window(self):
        self.window.destroy()
        self.parent.window.deiconify()
