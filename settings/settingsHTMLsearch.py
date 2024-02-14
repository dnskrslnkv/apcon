# Словарь, содержащий ссылки на архивы новостей сайта
url_path = {
    'mehrnews': "https://en.mehrnews.com/archive",
    'tehrantimes': "https://www.tehrantimes.com/archive",

}

# Словарь, содержащий XPath на кнопку >> следующая страница для каждого сайта
button_next_page_XPATH = {
    'mehrnews': "/html/body/main/div/div[2]/div/div/div[1]/section/footer/div/ul/li[13]/a",
    'tehrantimes': '/html/body/main/div/div/div/section/div/section/div[3]/ul/li[13]/a',

}

# Словарь, содержащий название "классов" поиска по html-коду новостной страницы даты, категории, текста новости
dict_CLASSNAME = {
    'date': {
        'mehrnews': 'col-6.col-sm-4.item-date',
        'tehrantimes': 'item-date.half-left',

    },

    'category': {
        'mehrnews': 'col-6.col-sm-4',
        'tehrantimes': 'item-path.half-right',

    },

    'post': {
        'mehrnews': 'news',
        'tehrantimes': 'clearfix.news',

    },

    'article': {
        'mehrnews': "item-body",
        'tehrantimes': 'item-text',

    }
}

# Словарь, содержащий название "тэгов" поиска по html-коду новостной страницы ссылки и названия новостной статьи
dict_TAGNAME = {
    'link': {
        'mehrnews': 'a',
        'tehrantimes': 'a',

    },

    'title': {
        'mehrnews': 'h3',
        'tehrantimes': 'h3',

    },

    'article': {
        'mehrnews': 'p',
        'tehrantimes': 'p',

    }
}
