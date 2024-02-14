import tkinter as tk

from classification_functional.ClassificationResult import ClassificationResultWindow






class ClassificationWindow():
    """Класс необходим для реализации функции классификации текста: определение категории текста на основе
    существующей БД"""

    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel()
        self.window.title("APCON: Classification")
        self.window.geometry("1000x600")
        self.create_widgets()

    def create_widgets(self):
        # Создание виджета Label и Entry для текста
        self.label_text_area = tk.Label(self.window, text='Введите текст для классификации: ', font=('Times New Roman', 14))
        self.label_text_area.grid(row=1, column=0, sticky='w')

        self.entry_text_area = tk.Entry(self.window, width=100)
        self.entry_text_area.grid(row=1, column=1, sticky='w')


        self.classification_button = tk.Button(self.window, text='Запустить классификацию', command= self.SetupClassification,
                                                font=('Times New Roman', 14))
        self.classification_button.grid(row=4, column=0)


        # Создание виджета Button для функции Назад
        self.back_button = tk.Button(self.window, text="Назад", command=self.close_ClassificationWindow,
                                     font=('Times New Roman', 14))
        self.back_button.grid(row=6, column=0)

    def SetupClassification(self):
        self.window.withdraw()
        ClassificationResultWindow(self, self.entry_text_area.get())


    def close_ClassificationWindow(self):
        self.window.destroy()
        self.parent.window.deiconify()