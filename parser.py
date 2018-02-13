import datetime
from scraper import Scraper
from colorama import init, Fore, Back, Style

best_rooms = ["Aula Be", "Aula Ve", "Aula Qe"]
fine_rooms = ["Aula Ae", "Aula Pe", "Aula Ie", "Aula Oe", "Aula Ke"]
shitty_rooms = ["Aula Ge"]


init()


now = datetime.datetime.now()
scraper = Scraper()

data = scraper.get_room_list()

free_room = []

for room in data:
    if room.is_free(now):
        # print(room.name)
        free_room.append(room)


for room in free_room:

    for best in best_rooms:
        if room.name == best:
            print(Fore.GREEN + room.name)

    for fine in fine_rooms:
        if room.name == fine:
            print(Fore.BLUE + room.name)

    for shitty in shitty_rooms:
        if room.name == shitty:
            print(Fore.RED + room.name)
