import time
import threading
from RPLCD import CharLCD
from .screendisplay import ScreenDisplay

class PiLcdDisplay(ScreenDisplay):

    def __init__(self, lines=1, line_length=5, update_interval=1):
        super(PiLcdDisplay, self).__init__(lines, line_length, update_interval)
        self.timer = None

    def start(self):
        ''' Start the LCD display update loop '''
        self.lcd = CharLCD(pin_rs=26, pin_e=24, pins_data=[22,18,16,12])
        self.lcd.clear()
        self.next_call = time.time()
        self.update()

    def update(self):
        ''' LCD display update loop '''
        super(PiLcdDisplay, self).update()

        self.update_lcd()

        self.next_call = self.next_call + self.update_interval
        self.timer = threading.Timer(self.next_call - time.time(), self.update)
        self.timer.start()

    def update_lcd(self):
        ''' Update the LCD display '''
        for i in range(self.lines):
            self.lcd.cursor_pos = (i, 0)
            self.lcd.write_string(self.displayed_info[i])

    def close(self):
        ''' Close the LCD display '''
        if self.timer != None:
            self.timer.cancel()
