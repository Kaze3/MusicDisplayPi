import datetime
import time
import threading

class MainController:

    def get_is_running(self):
        return self.is_running

    def __init__(self, interface, display):
        self.interface = interface
        self.display = display

    def init(self):
        self.interface.init()

    def start(self, check_interval=0.2):
        self.display.start()
        self.check_interval = check_interval
        self.next_call = time.time()
        self.check_interface()
        self.is_running = True

    def stop(self):
        if self.is_running:
            self.timer.cancel()
            self.is_running = False
            self.display.close()

    def check_interface(self):
        status = self.interface.get_status()
        update = [''] * self.display.get_number_of_lines()

        if status == self.interface.Status.stopped:
            update[0] = 'Stopped'
        elif status == self.interface.Status.playing:
            divider = ' -=- '
            track = self.interface.get_current_track()
            update[0] = track['track'] + '. ' + track['title'] + ' // ' + track['artist'] + divider
            update[1] = track['album'] + ' (' + track['date'] + ') // ' + track['genre'] + divider
            update[2] = self.format_time(track['elapsed']) + '/' + self.format_time(track['time']) + ' ' + chr(16)
            self.display.set_flashing_line(0, 2)
        elif status == self.interface.Status.paused:
            divider = ' -=- '
            track = self.interface.get_current_track()
            update[0] = track['track'] + '. ' + track['title'] + ' // ' + track['artist'] + divider
            update[1] = track['album'] + ' (' + track['date'] + ') // ' + track['genre'] + divider
            update[2] = self.format_time(track['elapsed']) + '/' + self.format_time(track['time']) + ' ' + chr(160)
            self.display.set_flashing_line(1, 2)
                        
        self.display.update_lines(update)

        self.next_call = self.next_call + self.check_interval
        self.timer = threading.Timer(self.next_call - time.time(), self.check_interface)
        self.timer.start()        

    def format_time(self, time):
        return str(datetime.timedelta(seconds=int(float(time))))
