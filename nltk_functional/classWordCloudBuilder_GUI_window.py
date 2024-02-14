import tkinter as tk
import matplotlib.pyplot as plt

from tkinter import messagebox, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from nltk_functional import classNLTK


class GraphWordCloudBuilder:
    def __init__(self, parent, text):

        self.parent = parent
        self.window = tk.Toplevel()
        self.window.title("APCON: GraphWordCloud")

        self.text = text
        self.fig = None

        self.build_graph()
        self.create_widgets()

    def create_widgets(self):

        self.back_button = tk.Button(self.window, text="Назад", command=self.close_graph_wordcloud_window,
                                     font=('Times New Roman', 14))
        self.back_button.grid(row=5, column=0)

        self.save_button = tk.Button(self.window, text="Сохранить как картинку", command=self.save_graph,
                                     font=('Times New Roman', 14))
        self.save_button.grid(row=6, column=0)

    def build_graph(self):
        # Создаем фигуру и оси
        self.fig = plt.figure(figsize=(12, 7))
        ax = self.fig.add_subplot(111)

        # Строим сам график
        ax.imshow(classNLTK.NLTK_analysys(self.text).create_wordcloud(),
                  interpolation='bilinear')

        # Настраиваем подписи осей Х и Y, название графика, а также сетку
        ax.axis('off')

        # Создаем виджет CanvasTkAgg для отображения графика
        canvas = FigureCanvasTkAgg(self.fig, master=self.window)
        canvas.draw()

        # Разместить график в главном окне с помощью grid
        canvas.get_tk_widget().grid(row=0, column=0, sticky='w')

    def save_graph(self):
        # Открытие диалоговое окно для  выбора файла сохранения
        filename = tk.filedialog.asksaveasfilename(defaultextension='.png',
                                                   filetypes=[('PNG', '*.png'), ('JPEG', '*.jpg'),
                                                              ('All files', '*.*')])
        # Если файл выбран, сохранить график как картинку
        if filename:
            self.fig.savefig(filename)
            messagebox.showinfo("Сохранение", "График успешно сохранен!")
        else:
            messagebox.showinfo("Сохранение", "Сохранение отменено")

    def close_graph_wordcloud_window(self):
        self.window.destroy()
        self.parent.window.deiconify()
