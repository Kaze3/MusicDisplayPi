import enum

class MainInterface():
    class Status(enum.Enum):
        playing = 0
        stopped = 1
        paused = 2
