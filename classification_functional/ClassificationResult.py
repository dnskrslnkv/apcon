import tkinter as tk

from classification_functional.classClassification import Classification


class ClassificationResultWindow:
    def __init__(self, parent, text):
        self.parent = parent
        self.window = tk.Toplevel()
        self.window.title("APCON: ClassificationResult")

        self.text = text

        self.result = Classification(self.text)

        self.create_widgets()

    def create_widgets(self):
        # Создаем виджет Text и добавляем текст который необходимо было классифицировать
        self.label_classification_text = tk.Label(self.window, text="Текст для классификации:",
                                                  font=('Times New Roman', 14), justify="left")
        self.label_classification_text.grid(row=1, column=0, sticky='w')

        self.label_classification_text_value = tk.Text(self.window, wrap='word', width=100, height=20)
        self.label_classification_text_value.insert('1.0', self.text)
        self.label_classification_text_value.grid(row=1, column=1, sticky='w')

        # Создаем виджет Label и добавляем текст с наиболее вероятного категория данного текста
        self.label_category = tk.Label(self.window, text="Наиболее вероятная категория:",
                                       font=('Times New Roman', 14), justify="left")
        self.label_category.grid(row=2, column=0, sticky='w')

        self.label_category_value = tk.Text(self.window, wrap='word', width=50, height=1)
        self.label_category_value.insert('1.0', self.result.answer()[0])
        self.label_category_value.grid(row=2, column=1, sticky='w')

        self.back_button = tk.Button(self.window, text="Назад", command=self.close_ClassificationResultWindow,
                                     font=('Times New Roman', 14))
        self.back_button.grid(row=5, column=0)

    def close_ClassificationResultWindow(self):
        self.window.destroy()
        self.parent.window.deiconify()
