class Time():
    def __init__(self, s):
        t = s.split(':')
        if len(t) == 2:
            self.minutes = int(t[0]) * 60 + int(t[1])
        else:
            self.minutes = int(t[0])

    def __str__(self):
        h, m = divmod(self.minutes)
        return f'{h}:{m:0>2}'
