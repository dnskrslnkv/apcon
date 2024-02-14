from nltk_functional.classNLTK import NLTK_analysys
from model import News


class Classification:

    def __init__(self, text):

        self.query = News.select()

        self.text = NLTK_analysys(text.lower()).nltk_processing()

        self.all_count_words = len(self.count_joint_probability(self.flatten(self.convertion_text(
            [el.text_article for el in self.query if el.category in ['Politics', 'Economy', 'Sports', 'Culture']]))))

        # Создаем словарь в котором будет находиться кол-во новостей в каждой из новостных категорий

        self.dict_count_news = {
            'Politics': 0,
            'Economy': 0,
            'Sports': 0,
            'Culture': 0,
            'Result': 0
        }

        # Создаем словарь в котором будет находиться кол-во слов в каждой из новостный категорий
        self.dict_count_words_in_news_category = {
            'Politics': None,
            'Economy': None,
            'Sports': None,
            'Culture': None
        }

        # Создаем словарь в котором будут храниться оценки вероятности для каждой из категорий
        self.result_bayes_coeff = {
            'Politics': 1,
            'Economy': 1,
            'Sports': 1,
            'Culture': 1
        }

        self.info_count_news()
        self.count_word_in_category()
        self.bayes_coeff()
        self.answer()

    def convertion_text(self, array: list) -> list:
        """Функция выполняет поэтапную обработку текста с помощью класса NLTK_analysys
           из папки nltk_functional"""
        return [NLTK_analysys(el).nltk_processing() for el in array]

    def count_joint_probability(self, word_list: list) -> dict:
        """Функия подсчитывает сколько раз каждое слово встречается в новостной статье"""
        word_count = {}
        for word in word_list:
            if word not in word_count:
                word_count[word] = 0
            word_count[word] += 1

        return word_count

    def flatten(self, list_of_lists: list) -> list:
        """Функция выполняет рекурсивное раскрытие вложенных списков"""
        result = []
        for item in list_of_lists:
            if isinstance(item, list):
                result.extend(self.flatten(item))
            else:
                result.append(item)
        return result

    def info_count_news(self):
        """Функция предназначена для подсчета кол-ва статей в каждой категории, а также подсчета общего кол-ва статей"""

        list_category = ['Politics', 'Economy', 'Sports', 'Culture']
        for _ in list_category:
            self.dict_count_news[_] = self.query.where(News.category == _).limit(100).count()
            self.dict_count_news['Result'] += self.query.where(News.category == _).limit(100).count()

        return self.dict_count_news

    def count_word_in_category(self) -> dict:
        """Функция предназначена для посчета кол-ва встречающихся слов в каждой из категорий"""

        for value in ['Politics', 'Economy', 'Sports', 'Culture']:
            list_value = self.convertion_text(
                [el.text_article for el in self.query.where(News.category == value).limit(100)])
            self.dict_count_words_in_news_category[value] = self.count_joint_probability(self.flatten(list_value))

        return self.dict_count_words_in_news_category

    def bayes_coeff(self) -> dict:
        self.result = {
            'Politics': 1,
            'Economy': 1,
            'Sports': 1,
            'Culture': 1
        }
        for value in ['Politics', 'Economy', 'Sports', 'Culture']:
            for el in self.text:
                if el in self.dict_count_words_in_news_category[value].keys():
                    self.result_bayes_coeff[value] *= (
                        ((1 + self.dict_count_words_in_news_category[value][el]) / (
                                1 * (
                            sum(self.dict_count_words_in_news_category[value].values())) + self.all_count_words)))
                else:
                    self.result_bayes_coeff[value] *= (
                        ((1 + 0) / (1 * sum(
                            self.dict_count_words_in_news_category[value].values()) + self.all_count_words)))
            self.result_bayes_coeff[value] *= ((self.info_count_news()[value] / self.info_count_news()['Result']))
        return self.result_bayes_coeff

    def answer(self):
        for key, value in self.result_bayes_coeff.items():
            if value == max(self.result_bayes_coeff.values()):
                return [key, value]
