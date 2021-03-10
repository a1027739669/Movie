import mongoengine


class Movie(mongoengine.Document):
    movieid = mongoengine.StringField(required=True)
    actorid = mongoengine.StringField()
    actors = mongoengine.StringField()
    alias = mongoengine.StringField(max_length=255)
    cover = mongoengine.StringField()
    director =  mongoengine.StringField(max_length=255)
    directorid =mongoengine.StringField()
    genre = mongoengine.StringField(max_length=255)
    language = mongoengine.StringField(max_length=255)
    minus = mongoengine.IntField()
    name = mongoengine.StringField(max_length=255)
    region = mongoengine.StringField(max_length=255)
    relesetime = mongoengine.StringField(max_length=255)
    score = mongoengine.FloatField()
    storyline = mongoengine.StringField()
    tag =mongoengine.StringField()
    vote = mongoengine.IntField()
    feature = mongoengine.StringField()

