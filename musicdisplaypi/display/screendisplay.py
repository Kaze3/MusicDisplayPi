class ScreenDisplay():
    INIT_CHAR = ' '

    def set_flashing_line(self, flashing, line):
        if line < 0 or line > self.lines - 1:
            return

        self.flash[line] = flashing
        #self.flash_indices[line] = self.flash_time

    def get_number_of_lines(self):
        return self.lines

    def get_line_length(self):
        return self.line_length

    def __init__(self, lines=1, line_length=5, update_interval=1, hold_time=8):
        initial_line = ScreenDisplay.INIT_CHAR * line_length

        self.update_interval = update_interval
        self.current_info = [initial_line] * lines
        self.update_info = [initial_line] * lines
        self.displayed_info = [initial_line] * lines
        self.scroll_indices = [0] * lines
        self.flash_time = 5
        self.flash = [0] * lines
        self.flash_indices = [self.flash_time] * lines
        self.hold = [0] * lines
        self.line_length = line_length
        self.lines = lines
        self.hold_time = hold_time

    def update_lines(self, update):
        ''' Update the information to be displayed '''
        if len(update) != self.lines:
            return
    
        self.update_info = update

    def update(self):
        ''' Update the display '''
        for i in range(self.lines):
            if self.update_info[i] != self.current_info[i]:
                self.scroll_indices[i] = 0
                self.hold[i] = self.hold_time
                self.current_info[i] = self.update_info[i]                

            info = self.current_info[i]
            info_length = len(info)

            if info_length <= self.line_length or self.scroll_indices[i] >= info_length:
                self.scroll_indices[i] = 0

            n = self.scroll_indices[i]

            if self.flash[i] == 1 and self.flash_indices[i] < self.flash_time/2:
                self.displayed_info[i] = ' ' * self.line_length
            else:
                if info_length <= self.line_length:
                    self.displayed_info[i] = info + ' ' * (self.line_length - info_length)
                elif n+self.line_length <= info_length:
                    self.displayed_info[i] = info[n:n+self.line_length]
                else:
                    self.displayed_info[i] = info[n:] + info[:self.line_length-info_length+n]
         
            if self.hold[i] > 0:
                self.hold[i] -= 1
            else:
                self.scroll_indices[i] += 1

            if self.flash_indices[i] == 0:
                self.flash_indices[i] = self.flash_time
            else:
                self.flash_indices[i] -= 1

if __name__ == "__main__":
    display = ScreenDisplay()
    test_update = [ "This is a test. " ]
    display.update_lines(test_update)
    for i in range(30):
        display.update()

