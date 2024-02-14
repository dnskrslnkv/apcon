import re
import time
import json
from selenium.webdriver.common.by import By
from settings.settingsHTMLsearch import url_path, button_next_page_XPATH, \
    dict_CLASSNAME, dict_TAGNAME

from model import News, db
from parse_functional.time_conversion import conversion_str_date_to_datetimeformat, date_conversion


def timer(func):
    """Декоратор предназначенный для вывода инфомрации о времени работы функции, а также о предназначении функции"""

    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"\nСтарт выполнения функции: {func.__name__}")
        print(f'\nПредназначение функции:\n \t{func.__doc__}')
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"\nОкончание выполнения функции: {func.__name__}")
        execution_time = end_time - start_time
        print(
            f"Время выполнения функции '{func.__name__}': {round(execution_time // 60, 3)} min, {round(execution_time % 60, 3)} sec\n")
        return result

    return wrapper


class ParseNews:

    def __init__(self, count_news: int, name_site: str, driver):
        self.info_news = {

            'Links': [],
            'Titles': [],
            'Date of publication': [],
            'Category': [],
            'Article': [],

        }
        self.count_news = count_news
        self.name_site = name_site.lower()
        self.driver = driver

    @timer
    def collecting_links(self):
        """Функция необходима для сбора ссылок на новости,по которым потом будем проходить для сбора более подробной информации"""

        self.driver.get(url_path[self.name_site])

        while len(self.info_news['Links']) < self.count_news:
            posts = self.driver.find_elements(By.CLASS_NAME, dict_CLASSNAME['post'][self.name_site])

            for post in posts:
                news_link = post.find_element(By.TAG_NAME, dict_TAGNAME['link'][self.name_site]).get_attribute(
                    "href")  # ссылка
                news_title = post.find_element(By.TAG_NAME, dict_TAGNAME['title'][self.name_site]).text
                self.info_news['Links'].append(news_link)
                self.info_news['Titles'].append(news_title)

            button_next_page = self.driver.find_element(By.XPATH, button_next_page_XPATH[self.name_site])
            button_next_page.click()

        self.info_news['Links'] = self.info_news['Links'][:self.count_news]
        self.info_news['Titles'] = self.info_news['Titles'][:self.count_news]

    @timer
    def collecting_info(self):
        """Функция необходима для сбора подробной информации: даты публикации, категории и текста статьи"""

        for elem in self.info_news['Links']:
            self.driver.get(elem)

            # Участок кода, достающий дату со страницы отдельной новости.
            # Затем удаляет оттуда фрагмент строки с помощью регулярных выражений.
            # Сохраняет получившийся результат в список с датами каждой новости.
            date = self.driver.find_element(By.CLASS_NAME, dict_CLASSNAME['date'][self.name_site]).text
            result = (re.sub(r"\u202f", '', date)).split(',')
            result_finally = date_conversion(' '.join(result))
            self.info_news['Date of publication'].append(
                conversion_str_date_to_datetimeformat(result_finally))

            # Участок кода, достающий категорию со страницы отдельной новости.
            # Сохраняет получившийся результат в список с категориями каждой новости.

            self.info_news['Category'].append(
                self.driver.find_element(By.CLASS_NAME, dict_CLASSNAME['category'][self.name_site]).text)

            # Участок кода, достающий текст статьи со страницы отдельной новости.
            # Сохраняет получившийся результат в список с текстами статьи каждой новости,
            # текст статьи преобразуется в строку.
            finally_string_text = ''
            blocks_article = self.driver.find_element(By.CLASS_NAME, dict_CLASSNAME['article'][self.name_site])
            posts_article = blocks_article.find_elements(By.TAG_NAME, dict_TAGNAME['article'][self.name_site])
            for elem_post_article in range(0, len(posts_article) - 1):
                text_article = posts_article[elem_post_article].text
                finally_string_text += text_article + " "
            self.info_news['Article'].append(finally_string_text)

    @timer
    def save_information(self):
        """Функция необходима для того, чтобы сохранить всю информацию, которую мы спарсили в БД: data_news.db"""

        data = [
            {
                'Links': i,
                'Titles': j,
                'Date of publication': k,
                'Category': l,
                'Article': m,
            } for i, j, k, l, m in zip(self.info_news['Links'],
                                       self.info_news['Titles'],
                                       self.info_news['Date of publication'],
                                       self.info_news['Category'],
                                       self.info_news['Article'])
        ]

        with open(f'json_files\{self.name_site}.json', "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        with open(f'{self.name_site}.json', 'r', encoding='utf-8') as read_file:
            data = json.load(read_file)
            with db:
                db.create_tables([News])
                for elem in data:
                    if News.select().where(News.link == elem['Links']):
                        pass
                    else:
                        News(
                            name_site=self.name_site,
                            link=elem['Links'],
                            title=elem['Titles'],
                            category=elem['Category'],
                            text_article=elem['Article'],
                            date_of_publication=elem['Date of publication'],
                        ).save()
