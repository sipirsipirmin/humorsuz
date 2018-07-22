from random import randint
from news.models import NewsItem

cities = ["Ankara","Karabuk","Zonguldak","Hakkari","Muş","Los Encılıs"]
thinks = ["Fikibok","Fuze","Labrador","Teriyer","Tihulu","Metallica","Gnu",
          "Windows"
        ]
titles = [
          "{}\'de {} istalası",
          "{} çok içti, {}\'de mevzu oldu",
          "Bize de mi {} diyen {} ortalığı çok karıştırdı",
          "Öğretmenim {} bana silgi attı diyen {} afaroz edildi!",

    ]
def get_random_new():
    if randint(0,1) % 2 == 0:
        return titles[randint(0,len(titles)-1)].format(thinks[randint(0,len(thinks)-1)], cities[randint(0,len(cities)-1)])
    else:
        return titles[randint(0,len(titles)-1)].format(cities[randint(0,len(cities)-1)],thinks[randint(0,len(thinks)-1)])
def insert_new_new_to_database():
    new_new = get_random_new()
    haber = NewsItem()
    haber.title = new_new
    haber.content = new_new
    haber.save()
