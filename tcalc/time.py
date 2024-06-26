class Time():
    def __init__(self, s):
        if type(s) is str:
            self.parse(s)
        elif type(s) is int:
            self.minutes = s

    def parse(self, s):
        t = s.split(':')
        if len(t) == 2:
            self.minutes = int(t[0]) * 60 + int(t[1])
        else:
            self.minutes = int(t[0])

    def __str__(self):
        h, m = divmod(self.minutes, 60)
        return f'{h}:{m:0>2}'

    def __add__(self, other):
        return Time(self.minutes + other.minutes)

    def __sub__(self, other):
        return Time(self.minutes - other.minutes)
