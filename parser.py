import datetime

from scraper import Scraper
from colorama import init, Fore, Back, Style

best_rooms = ["Aula Be", "Aula Ve", "Aula Oe"]
fine_rooms = ["Aula Ae", "Aula Pe", "Aula Ie", "Aula Qe", "Aula Ke"]
shitty_rooms = ["Aula Ge", "Aula Ce", "Aula De", "Aula Je", "Aula Le", "Aula Se"]



init()


now = datetime.datetime.now()
scraper = Scraper()

data = scraper.get_room_list()

free_room = []

for room in data:
    if room.is_free(now) :
        # print(room.name)
        free_room.append(room)


for room in free_room:
    for best in best_rooms:
        if room.name == best:
            print(Fore.GREEN + room.name + " from " + str(room.free_slot.beginning.time()) + " to " + str(room.free_slot.end.time()))

for room in free_room:
    for fine in fine_rooms:
        if room.name == fine:
            print(Fore.YELLOW + room.name + " from " + str(room.free_slot.beginning.time()) + " to " + str(room.free_slot.end.time()))

for room in free_room:
    for shitty in shitty_rooms:
        if room.name == shitty:
            print(Fore.LIGHTWHITE_EX + room.name + " from " + str(room.free_slot.beginning.time()) + " to " + str(room.free_slot.end.time()))
