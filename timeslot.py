
class TimeSlot(object):

    def __init__(self, beginning_time, end_time):
        self.beginning = beginning_time
        self.end = end_time

    # Check if now the room is free
    def is_free(self, now):
        if (self.beginning.time() < now.time()) and (now.time() < self.end.time()):
            return True
        else:
            return False


