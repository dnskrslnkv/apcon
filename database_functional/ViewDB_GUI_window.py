import tkinter as tk

from model import News

from parse_functional.time_conversion import conversion_str_date_to_datetimeformat
from tkinter import ttk
from database_functional.InfoNews_GUI_window import InfoNews
from database_functional.InfoDB_GUI_window import InfoDB


class ViewDB:
    """Класс нужен дли инициализации окна общей информацией о содержимом БД"""

    def __init__(self, parent):
        self.parent = parent

        self.window = tk.Toplevel()
        self.window.title("APCON: Database")
        self.window.state("zoomed")

        self.create_widgets()

    def create_widgets(self):
        """Функция предназначена для создания виджетов в диалоговом окне с просмотром содержимого БД"""

        self.filter_frame = tk.Frame(self.window)
        self.filter_frame.pack(pady=10)

        self.category_label = tk.Label(self.filter_frame, text="Категория:", font=('Times New Roman', 14))
        self.category_label.grid(row=0, column=0, padx=10)

        self.category_filter = tk.Entry(self.filter_frame)
        self.category_filter.grid(row=0, column=1, padx=10)

        self.name_site_label = tk.Label(self.filter_frame, text='Название сайта', font=('Times New Roman', 14))
        self.name_site_label.grid(row=0, column=2, padx=10)

        self.name_site_filter = tk.Entry(self.filter_frame)
        self.name_site_filter.grid(row=0, column=3, padx=10)

        self.start_date_label = tk.Label(self.filter_frame, text='Начальная дата', font=('Times New Roman', 14))
        self.start_date_label.grid(row=0, column=4, padx=10)

        self.start_date_filter = tk.Entry(self.filter_frame)
        self.start_date_filter.grid(row=0, column=5, padx=10)

        self.end_date_label = tk.Label(self.filter_frame, text='Конечная дата', font=('Times New Roman', 14))
        self.end_date_label.grid(row=0, column=6, padx=10)

        self.end_date_filter = tk.Entry(self.filter_frame)
        self.end_date_filter.grid(row=0, column=7, padx=10)

        self.filter_button = tk.Button(self.filter_frame, text="Применить фильтр", command=self.filter_list,
                                       font=('Times New Roman', 14))
        self.filter_button.grid(row=0, column=8, padx=10)

        self.back = tk.Button(self.filter_frame, text="Назад", command=self.close_viewDB_window,
                              font=('Times New Roman', 14))
        self.back.grid(row=0, column=9, padx=10)

        self.info_db_button = tk.Button(self.filter_frame, text="Информация о содержимом БД", command=self.view_info_db,
                                        font=('Times New Roman', 14))
        self.info_db_button.grid(row=0, column=10)

        # Создание вертикального скроллбара
        self.scrollbar = ttk.Scrollbar(self.window)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree = ttk.Treeview(self.window, yscrollcommand=self.scrollbar.set)

        # Определение столбцов и их ширины
        self.tree["columns"] = ("name_site", "category", "date_of_publication", "title")
        self.tree.column("name_site", width=100)
        self.tree.column("category", width=100)
        self.tree.column("date_of_publication", width=150)
        self.tree.column("title", width=500)

        # Определение заголовков столбцов
        self.tree.heading("name_site", text="Название сайта")
        self.tree.heading("category", text="Категория")
        self.tree.heading("date_of_publication", text="Дата публикации")
        self.tree.heading("title", text="Заголовок статьи")

        self.populate_list()

        self.tree.bind("<<TreeviewSelect>>", self.handle_tree_selection)

    def handle_tree_selection(self, event):

        selected_item = self.tree.focus()
        if selected_item:
            self.window.withdraw()
            InfoNews(self, self.tree.item(selected_item)['values'][3])

    def populate_list(self):
        query = News.select()
        for item in query:
            self.tree.insert('', tk.END, values=[item.name_site,
                                                 item.category,
                                                 item.date_of_publication,
                                                 item.text_article])
        self.scrollbar.configure(command=self.tree.yview)
        self.tree.pack(fill="both", expand=True)

    def filter_list(self):
        self.tree.delete(*self.tree.get_children())
        query = News.select()
        if self.category_filter.get():
            query = query.select().where(News.category == self.category_filter.get())
        if self.name_site_filter.get():
            query = query.select().where(News.name_site == self.name_site_filter.get())
        if self.start_date_filter.get():
            query = query.select().where(News.date_of_publication
                                         >= conversion_str_date_to_datetimeformat(self.start_date_filter.get()))
        if self.end_date_filter.get():
            query = query.select().where(News.date_of_publication
                                         <= conversion_str_date_to_datetimeformat(self.end_date_filter.get()))

        for item in query:
            self.tree.insert('', tk.END, values=[item.name_site,
                                                 item.category,
                                                 item.date_of_publication,
                                                 item.text_article])
        self.scrollbar.configure(command=self.tree.yview)
        self.tree.pack(fill="both", expand=True)

    def view_info_db(self):
        self.window.withdraw()
        InfoDB(self)

    def close_viewDB_window(self):
        self.window.destroy()
        self.parent.window.deiconify()
