from mongoengine import *
import datetime


connect('TijuanoBot')


class Dollar(Document):
    value = StringField(max_length=120, required=True)
    date_created = DateTimeField(required=True)


class Bot(Document):
    name = fields.StringField(max_length=250, required=True)
    last_tweet_id = IntField()
    users_black_list = ListField(StringField())
