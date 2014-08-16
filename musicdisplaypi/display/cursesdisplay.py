from .screendisplay import ScreenDisplay
import sys
import curses
import datetime
import time
import threading

class CursesDisplay(ScreenDisplay):
    
    def __init__(self, lines=1, line_length=5, update_interval=1):
        super(CursesDisplay, self).__init__(lines, line_length, update_interval)
        self.timer = None
        self.stdscr = None

    def start(self):
        self.stdscr = curses.initscr()
        curses.curs_set(0)
        self.next_call = time.time()
        self.clear_display()
        self.update()

    def clear_display(self):
        hor_line = '-' * (self.line_length + 2)

        self.stdscr.addstr(0, 0, hor_line)
        for i in range(self.lines):
            self.stdscr.addstr(i+1, 0, '|' + ' ' * (self.line_length) + '|')

        self.stdscr.addstr(self.lines+1, 0, hor_line)
        self.stdscr.refresh()

    def update(self):
        super(CursesDisplay, self).update()

        self.update_curses()

        self.next_call = self.next_call + self.update_interval
        self.timer = threading.Timer(self.next_call - time.time(), self.update)
        self.timer.start()

    def update_curses(self):
        ''' Update the curses display '''
        for i in range(self.lines):
            self.stdscr.addstr(i+1, 1, self.displayed_info[i])

        self.stdscr.refresh()

    def close(self):
        if self.timer != None:
            self.timer.cancel()
        
        if self.stdscr != None:
            curses.endwin()

if __name__ == '__main__':
    display = CursesDisplay(lines=3, line_length=20, update_interval=0.25)
    
    test_update = [ 
        'A Nightmare To Remember :: Dream Theater | ',
        'Black Clouds and Silver Linings | ',
        '01:23/06:58 | ' ]

    another_update = [ 
        'Bombtrack :: Rage Against The Machine | ',
        'Rage Against The Machine | ',
        '00:12/03:34 | ' ]
    
    display.update_lines(test_update)
    
    while True:
        try:
            time.sleep(20)
            display.update_lines(another_update)
        except KeyboardInterrupt:
            display.close()
            sys.exit(1)
