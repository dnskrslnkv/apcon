import string
from nltk import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk import WordNetLemmatizer
from wordcloud import WordCloud


class NLTK_analysys:

    def __init__(self, text):
        self.text = text.lower()
        self.special_chars = string.punctuation + '"”“’,#$%&()*+,-./:;<=>?@[\]^_{|}~'
        self.special_digits = '1234567890'
        self.stopwords = stopwords.words('english')
        self.lemmatizer = WordNetLemmatizer()

    def remove_chars_from_text(self):
        """ Функция убирает из исходного текста  специальные символы : !"#$%&()*+,-./:;<=>?@[\]^_{|}~"""
        return "".join([ch for ch in self.text if ch not in self.special_chars])

    def remove_digits_from_text(self):
        """Функция убирает из исходного текста числовые значения: 1234567890"""
        return "".join([elem for elem in self.text if elem not in self.special_digits])

    def remove_stopwords_from_text(self, words: list) -> list:
        """Функция удаляет из исходного текста 'стоп-слова' используя для этого встроенный в библиотеку nltk словарь"""
        return [word for word in words if word not in self.stopwords]

    def getting_the_components(self, component: str) -> list:
        """ Для последующей обработки очищенный текст необходимо разбить на составные части – токены.
        В анализе текста на естественном языке применяется разбиение на символы, слова и предложения.
        Процесс разбиения называется токенизация. Для нашей задачи частотного анализа необходимо разбить
        текст на слова.Для этого можно использовать готовый метод библиотеки NLTK"""
        return word_tokenize(component)

    def lemmatization_text(self, component: list) -> list:
        """Необходимо слова исходного текста привести к их основам или изначальной форме – провести стемминг или лемматизацию.
        Данная функция проводит лемматизацию на основе модуля WordNetLemmatizer"""
        return [self.lemmatizer.lemmatize(word) for word in component]

    def nltk_processing(self) -> list:
        """Данная функция выполняет поэтапную обработку текста"""
        self.text = self.remove_chars_from_text()
        self.text = self.remove_digits_from_text()
        words = self.getting_the_components(self.text)
        words = self.remove_stopwords_from_text(words)
        #words = self.lemmatization_text(words)
        return words

    def frequency_graphic(self, text):
        fdist = FreqDist(text)
        # Получаем 8 наиболее часто встречающихся слов
        top_words = fdist.most_common(8)
        # Разделяем слова и их частоту
        words, frequencies = zip(*top_words)
        # Создаем график
        # plt.xlabel('Слова')
        # plt.ylabel('Частота')
        # plt.title('График частотности слов')
        # plt.grid(True)
        # plt.plot(words, frequencies)
        return (words, frequencies)

    def create_wordcloud(self):
        wordcloud = WordCloud().generate(self.text)
        return wordcloud
