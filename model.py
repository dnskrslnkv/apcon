from peewee import *

db = SqliteDatabase("data_news.db")


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'date_of_publication'


class News(BaseModel):
    name_site = CharField()
    link = CharField()
    title = TextField()
    category = CharField()
    text_article = TextField()
    date_of_publication = DateField()

    class Meta:
        db_table = 'news'
