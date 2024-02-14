import tkinter as tk

from model import News


class InfoDB:
    """Класс нужен дли инициализации окна количественной информации в БД"""

    def __init__(self, parent):
        self.parent = parent
        # Создаем окно типа Toplevel,
        # то есть оно будет плавающим и независимым от основного окна приложения.
        self.window = tk.Toplevel()
        self.window.title("APCON: InfoDatabase")
        self.window.state("zoomed")

        # Создаем выборку из всех новостей
        self.query = News.select()
        # Формируем словарь с общей информацией о содержимом БД
        self.selection = self.create_selection()
        # Создаем виджеты на окне InfoDB
        self.create_widgets(self.selection)

    def create_widgets(self, selection):
        # Создаем виджет Label и добавляем вводный текст
        self.label_common_info = tk.Label(self.window, text="Общая информация о содержимом БД:\n\n",
                                          font=('Times New Roman', 14), justify="left")
        self.label_common_info.grid(row=0, column=0)

        # Создаем виджет Text и добавляем кол-во всех новостей, содержащихся в БД
        self.label_count_all_news = tk.Label(self.window, text="Общее количество новостей:",
                                             font=('Times New Roman', 14), justify="left")
        self.label_count_all_news.grid(row=1, column=0, sticky='w')

        self.label_count_all_news_value = tk.Text(self.window, wrap='word', width=20, height=1)
        self.label_count_all_news_value.insert('1.0', selection['Total'])
        self.label_count_all_news_value.grid(row=1, column=1, sticky='w')

        # Создаем виджет Text и добавляем кол-во всех новостей по теме политика
        self.label_count_politics_news = tk.Label(self.window, text="По теме 'Политика':",
                                                  font=('Times New Roman', 14), justify="left")
        self.label_count_politics_news.grid(row=2, column=0, sticky='w')

        self.label_count_politics_news_value = tk.Text(self.window, wrap='word', width=20, height=1)
        self.label_count_politics_news_value.insert('1.0', selection['Politics'])
        self.label_count_politics_news_value.grid(row=2, column=1, sticky='w')

        # Создаем виджет Text и добавляем кол-во всех новостей по теме Экономика
        self.label_count_economy_news = tk.Label(self.window, text="По теме 'Экономика':",
                                                 font=('Times New Roman', 14), justify="left")
        self.label_count_economy_news.grid(row=3, column=0, sticky='w')

        self.label_count_economy_news_value = tk.Text(self.window, wrap='word', width=20, height=1)
        self.label_count_economy_news_value.insert('1.0',
                                                   selection["Economy"])
        self.label_count_economy_news_value.grid(row=3, column=1, sticky='w')

        # Создаем виджет Text и добавляем кол-во всех новостей по теме Спорт
        self.label_count_sport_news = tk.Label(self.window, text="По теме 'Спорт':",
                                               font=('Times New Roman', 14), justify="left")
        self.label_count_sport_news.grid(row=4, column=0, sticky='w')

        self.label_count_sport_news_value = tk.Text(self.window, wrap='word', width=20, height=1)
        self.label_count_sport_news_value.insert('1.0',
                                                 selection["Sports"])
        self.label_count_sport_news_value.grid(row=4, column=1, sticky='w')

        # Создаем виджет Text и добавляем кол-во всех новостей по теме Культура
        self.label_count_culture_news = tk.Label(self.window, text="По теме 'Культура':",
                                                 font=('Times New Roman', 14), justify="left")
        self.label_count_culture_news.grid(row=5, column=0, sticky='w')

        self.label_count_culture_news_value = tk.Text(self.window, wrap='word', width=20, height=1)
        self.label_count_culture_news_value.insert('1.0',
                                                   selection["Culture"])
        self.label_count_culture_news_value.grid(row=5, column=1, sticky='w')

        # Создаем виджет Text и добавляем кол-во всех оставшихся новостей
        self.label_count_other_news = tk.Label(self.window, text="По теме 'Остальное':",
                                               font=('Times New Roman', 14), justify="left")
        self.label_count_other_news.grid(row=6, column=0, sticky='w')

        self.label_count_other_news_value = tk.Text(self.window, wrap='word', width=20, height=1)
        self.label_count_other_news_value.insert('1.0',
                                                 selection["Others"])
        self.label_count_other_news_value.grid(row=6, column=1, sticky='w')

        # Создаем виджет Text и добавляем название категорий новостей
        self.label_name_category = tk.Label(self.window, text="Категории:",
                                            font=('Times New Roman', 14), justify="left")
        self.label_name_category.grid(row=7, column=0, sticky='w')

        self.label_name_category_value = tk.Text(self.window, wrap='word', width=70, height=10)
        self.label_name_category_value.insert('1.0',
                                              selection["Name category"])
        self.label_name_category_value.grid(row=7, column=1, sticky='w')

        # Создаем виджет Text и добавляем дату самой ранней новости
        self.label_first_date = tk.Label(self.window, text="Дата самой ранней  новости:",
                                         font=('Times New Roman', 14), justify="left")
        self.label_first_date.grid(row=8, column=0, sticky='w')

        self.label_first_date_value = tk.Text(self.window, width=50, height=1)
        self.label_first_date_value.insert('1.0',
                                           selection["First date"])
        self.label_first_date_value.grid(row=8, column=1, sticky='w')

        # Создаем виджет Text и добавляем дату самой ранней новости
        self.label_last_date = tk.Label(self.window, text="Дата самой поздней новости:",
                                        font=('Times New Roman', 14), justify="left")
        self.label_last_date.grid(row=9, column=0, sticky='w')

        self.label_last_date_value = tk.Text(self.window, wrap='word', width=50, height=1)
        self.label_last_date_value.insert('1.0',
                                          selection["Last date"])
        self.label_last_date_value.grid(row=9, column=1, sticky='w')

        self.back = tk.Button(self.window, text="Назад", command=self.close_InfoDB_window,
                              font=('Times New Roman', 14))
        self.back.grid(row=10, column=0, padx=10)

    def create_selection(self):
        self.query_politics = int(self.query.where(News.category == "Politics").count())
        self.query_economy = int((self.query.where(News.category == "Economy").count()))
        self.query_sports = int(self.query.where(News.category == "Sports").count())
        self.query_culture = int(self.query.where(News.category == "Culture").count())
        self.query_other_news = int(self.query.count()) - (
                self.query_politics + self.query_economy + self.query_sports + self.query_culture)
        self.date_list = [el.date_of_publication for el in self.query.order_by(News.date_of_publication)]
        self.category_list = [_.category for _ in News.select(News.category).distinct()]

        result = {
            'Total': self.query.count(),
            'Politics': self.query_politics,
            'Economy': self.query_economy,
            'Sports': self.query_sports,
            'Culture': self.query_culture,
            'Others': self.query_other_news,
            'First date': self.date_list[0],
            'Last date': self.date_list[len(self.date_list) - 1],
            'Name category': ','.join(self.category_list)
        }

        return result

    def close_InfoDB_window(self):
        self.window.destroy()
        self.parent.window.deiconify()
