import tkinter as tk


from nltk_functional.classFrequencyBuilder_GUI_window import GraphFrequencyBuilder
from nltk_functional.classWordCloudBuilder_GUI_window import GraphWordCloudBuilder





class TextProcessing():
    """Класс необходим для реализации функции обработки текста: построения частотной характеристики,
    а также облака слов"""

    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel()
        self.window.title("APCON: Text Processing")
        self.window.geometry("1000x600")
        self.create_widgets()

    def create_widgets(self):
        # Создание виджета Label и Entry для ввода количества новостей
        self.label_text_area = tk.Label(self.window, text='Введите текст для обрабокти: ', font=('Times New Roman', 14))
        self.label_text_area.grid(row=1, column=0, sticky='w')

        self.entry_text_area = tk.Entry(self.window, width=100)
        self.entry_text_area.grid(row=1, column=1, sticky='w')

        # Создаем виджет Label и добавляем текст с названием выбраного сайта
        self.label_nltk_analysis = tk.Label(self.window, text="Возможные функции обработки текста:\n\n",
                                            font=('Times New Roman', 14), justify="left")
        self.label_nltk_analysis.grid(row=3, column=0)

        self.frequency_graph_button = tk.Button(self.window, text='График частотности слов',
                                                command=self.frequency_graphic,
                                                font=('Times New Roman', 14))
        self.frequency_graph_button.grid(row=4, column=0)

        self.wordcloud_graph_button = tk.Button(self.window, text='Облако слов',
                                                command=self.wordcloud_graphic,
                                                font=('Times New Roman', 14))
        self.wordcloud_graph_button.grid(row=5, column=0)

        # Создание виджета Button для функции Назад
        self.back_button = tk.Button(self.window, text="Назад", command=self.close_TextProcessingWindow,
                                     font=('Times New Roman', 14))
        self.back_button.grid(row=6, column=0)

    def frequency_graphic(self):
        self.window.withdraw()
        GraphFrequencyBuilder(self, self.entry_text_area.get())

    def wordcloud_graphic(self):
        self.window.withdraw()
        GraphWordCloudBuilder(self, self.entry_text_area.get())

    def close_TextProcessingWindow(self):
        self.window.destroy()
        self.parent.window.deiconify()