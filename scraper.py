from bs4 import BeautifulSoup
import requests
import datetime
import re
from room import Room


class Scraper(object):

    def __init__(self):
        today = datetime.datetime.now()

        timetable_page = 'https://gestionedidattica.unipd.it/Aule//index.php?content=gestore_spazi&area=27&day=' + str(today.strftime('%d')) + '&month=' + str(today.strftime('%m')) + '&year=20' + str(today.strftime('%y')) + '&from=07:30:00&to=21:30:00&vista=day&length=30&minCapacity=8&maxCapacity=240'
        user_agent = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'}
        # print(timetable_page)

        timetable = requests.get(timetable_page, headers=user_agent)

        soup = BeautifulSoup(timetable.content, 'html.parser', from_encoding='iso-8859-1')

        all_tables = soup.find_all('table', class_='tblchk')

        room_list = []

        for table in all_tables:
            table_decoder = BeautifulSoup(str(table), 'html.parser')

            room_name = re.compile('(?<=\>)(.*?)(?= -)')
            # print(room_name.findall(str(table_decoder.find_all("caption")))[0])
            temp_room = Room(room_name.findall(str(table_decoder.find_all("caption")))[0])

            free_time_slots = int(len(table_decoder.find_all("td"))/7)

            for w in range(free_time_slots):
                time = re.compile('\d\d:\d\d')
                # print(time.findall(str(table_decoder.find_all("td")[2+w*7]))[0])
                # print(time.findall(str(table_decoder.find_all("td")[3+w*7]))[0])
                temp_room.add_time_slot(time.findall(str(table_decoder.find_all("td")[2+w*7]))[0], time.findall(str(table_decoder.find_all("td")[3+w*7]))[0])

            room_list.append(temp_room)

        self.room_list = room_list
        self.age = datetime.datetime.now() - today

    def get_room_list(self):
        return self.room_list

