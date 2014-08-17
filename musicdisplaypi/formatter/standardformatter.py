import datetime

class StandardFormatter():
    def __init__(self, lines=4, width=20, divider=' -=- '):
        self.number_of_lines = lines
        self.width = width
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

        self.update[0] = self.track + '. ' + self.title
        self.update[1] = self.artist
        self.update[2] = self.album + ' (' + self.date + ') // ' + self.genre

        for i in range(self.number_of_lines - 1):
            if len(self.update[i]) > self.width:
                self.update[i] = self.update[i] + self.divider

        self.update[self.number_of_lines - 1] = self.format_time(self.elapsed) + '/' + self.format_time(self.time) + ' ' + chr(16)

        return self.update

    def get_paused_lines(self):
        return self.get_playing_lines()

    def get_stopped_lines(self):
        self.reset_lines()
        self.update[0] = 'Stopped'
        return self.update

    def format_time(self, time_string):
        time = int(float(time_string))
        print(time_string)
        hours, remainder = divmod(time, 3600)
        minutes, seconds = divmod(remainder, 60)

        if time > 3600:
            return '{0:02d}:{1:02d}:{2:02d}'.format(hours, minutes, seconds)
        else:
            return '{0:02d}:{1:02d}'.format(minutes, seconds)
