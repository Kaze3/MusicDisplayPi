import datetime

class StandardFormatter():
    def __init__(self, lines=4, divider=' -=- '):
        self.number_of_lines = lines
        self.divider = divider

        self.reset_lines()

    def reset_lines(self):
        self.update = [''] * self.number_of_lines

    def set_track_info(self, info):
        self.track = info['track']
        self.title = info['title']
        self.artist = info['artist']
        self.album = info['album']
        self.date = info['date']
        self.genre = info['genre']
        self.elapsed = info['elapsed']
        self.time = info['time']
        
    def get_playing_lines(self):
        self.reset_lines()

        self.update[0] = self.track + '. ' + self.title + ' // ' + self.artist + self.divider
        self.update[1] = self.album + ' (' + self.date + ') // ' + self.genre + self.divider
        self.update[3] = self.format_time(self.elapsed) + '/' + self.format_time(self.time) + ' ' + chr(16)

        return self.update

    def get_paused_lines(self):
        return self.get_playing_lines()

    def get_stopped_lines(self):
        self.reset_lines()
        self.update[0] = 'Stopped'
        return self.update

    def format_time(self, time):
        return str(datetime.timedelta(seconds=int(float(time))))
        
