from timeslot import TimeSlot
import datetime


class Room(object):

    def __init__(self, name):
        self.name = name
        self.timetable = []

    def print_stuff(self):
        print(self.name)

    def add_time_slot(self, beginning_time, end_time):
        self.timetable.append(TimeSlot(datetime.datetime.strptime(beginning_time, '%H:%M'), datetime.datetime.strptime(end_time, '%H:%M')))

    def get_timetable(self):
        return self.timetable

    def is_free(self, now):
        for _ in self.timetable:
            if _.is_free(now):
                return True

        return False
