from random import choice
from random import randint
from news.models import NewsItem

"""
    Random news generator for Django shell
    Usage:
        from rand_new import *
        insert_new_new_to_database()

"""
cities = ["Ankara",
          "Karabuk",
          "Zonguldak",
          "Hakkari",
          "Muş",
          "Los Encılıs",
          ]
thinks = ["Fikibok",
        "Fuze",
        "Labrador",
        "Teriyer",
        "Tihulu",
        "Metallica",
        "Gnu",
        "Windows",
        ]
titles = [
          "{}\'de {} istalası",
          "{} çok içti, {}\'de mevzu oldu",
          "Bize de mi {} diyen {} ortalığı çok karıştırdı",
          "Öğretmenim {} bana silgi attı diyen {} afaroz edildi!",

    ]
def get_random_new():
    if randint(0,1):
        return choice(titles).format(
                                choice(thinks),
                                choice(cities)
                                )
    else:
        return choice(titles).format(
                                choice(cities),
                                choice(thinks)
                                )
def insert_new_new_to_database():
    new_new = get_random_new()
    haber = NewsItem()
    haber.title = new_new
    haber.content = new_new
    haber.save()
