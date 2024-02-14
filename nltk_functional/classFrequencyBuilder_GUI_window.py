import tkinter as tk
from tkinter import messagebox, filedialog
from nltk_functional import classNLTK
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class GraphFrequencyBuilder:
    def __init__(self, parent, text):

        self.parent = parent
        self.window = tk.Toplevel()
        self.window.title("APCON: GraphFrequnecy")

        self.text = text
        self.fig = None

        self.x_data, self.y_data = classNLTK.NLTK_analysys(self.text).frequency_graphic(
            classNLTK.NLTK_analysys(self.text).nltk_processing())

        self.build_graph(self.x_data, self.y_data)

        self.create_widgets()

    def create_widgets(self):

        self.back_button = tk.Button(self.window, text="Назад", command=self.close_graph_frequency_window,
                                     font=('Times New Roman', 14))
        self.back_button.grid(row=5, column=0)

        self.save_button = tk.Button(self.window, text="Сохранить как картинку", command=self.save_graph,
                                     font=('Times New Roman', 14))
        self.save_button.grid(row=6, column=0)

    def build_graph(self, x_data, y_data):
        # Создаем фигуру и оси
        self.fig = Figure(figsize=(12, 7), dpi=100)
        ax = self.fig.add_subplot(111)

        # Строим сам график
        ax.plot(x_data, y_data)

        # Настраиваем подписи осей Х и Y, название графика, а также сетку
        ax.set_xlabel('Слова')
        ax.set_ylabel('Частота')
        ax.set_title('Частотная характеристика')
        ax.grid(True)
        ax.yaxis.set_ticks([1, 2, 3, 4, 5, 6, 7])

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

    def close_graph_frequency_window(self):
        self.window.destroy()
        self.parent.window.deiconify()
