import time
import threading

class MainController:

    def get_is_running(self):
        return self.is_running

    def __init__(self, interface, display, formatter):
        self.interface = interface
        self.display = display
        self.formatter = formatter

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

        if status == self.interface.Status.stopped:
            self.display.update_lines(self.formatter.get_stopped_lines())
        elif status == self.interface.Status.playing:
            self.formatter.set_track_info(self.interface.get_current_track())
            self.display.update_lines(self.formatter.get_playing_lines())
            self.display.set_flashing_line(0, self.display.get_number_of_lines() - 1)
        elif status == self.interface.Status.paused:
            print("Paused...")
            self.formatter.set_track_info(self.interface.get_current_track())
            self.display.update_lines(self.formatter.get_paused_lines())
            self.display.set_flashing_line(1, self.display.get_number_of_lines() - 1)
                        
        self.next_call = self.next_call + self.check_interval
        self.timer = threading.Timer(self.next_call - time.time(), self.check_interface)
        self.timer.start()
