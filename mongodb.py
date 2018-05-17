from pprint import pprint
import mongoengine as me


class Star(me.EmbeddedDocument):
    name = me.StringField()
    gender = me.StringField()


class Movie(me.Document):
    title = me.StringField()
    year = me.IntField()
    has_sequel = me.BooleanField()
    imdb_url = me.URLField()
    score = me.DecimalField()
    cast = me.EmbeddedDocumentListField(Star)


def list_movies():
    return Movie.objects.as_pymongo()


if __name__ == '__main__':
    #create connection to mongodb
    me.connect(db='movies')

    #create stars
    marlon_brando = Star(name='Marlon Brando', gender='Male')
    al_pacino = Star(name='Al Pacino', gender='Male')
    talia_shire = Star(name='Talia Shire', gender='Female')

    #create movie
    the_godfather = Movie(title='The Godfather', year=1972, has_sequel=True,
                          imdb_url='https://www.imdb.com/title/tt0068646',
                          score=9.2, cast=[marlon_brando, al_pacino, talia_shire])

    #save movie to database
    the_godfather.save()

    #list all movies
    for movie in list_movies():
        pprint(movie)

    #find and remove The Godfather from db
    movie = Movie.objects.get(title='The Godfather')
    movie.delete()
