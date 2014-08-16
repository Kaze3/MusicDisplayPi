from .maininterface import MainInterface
import mpd

class MpdInterface(MainInterface):
    DEFAULT_ADDRESS = "henry"
    DEFAULT_PORT = 6600

    def __init__(self, address = DEFAULT_ADDRESS, port = DEFAULT_PORT):
        self.address = address
        self.port = port

    def init(self):
        self.client = mpd.MPDClient()
        self.client.timeout = 10
        self.client.idletimeout = None
        self.client.connect(self.address, self.port)

    def terminate(self):
        self.client.close()
        self.client.disconnect()

    def get_version(self):
        return self.client.mpd_version

    def get_status(self):
        status = self.client.status()
        
        if status['state'] == 'play':
            return MainInterface.Status.playing

        if status['state'] == 'pause':
            return MainInterface.Status.paused

        return MainInterface.Status.stopped
        
    def get_current_track(self):
        song = self.client.currentsong()
        status = self.client.status()

        track_info = dict([
            ('track', song['track']), 
            ('title', song['title']), 
            ('artist', song['artist']),
            ('album', song['album']),
            ('genre', song['genre']),
            ('date', song['date']),
            ('time', song['time']),
            ('elapsed', status['elapsed'])
         ])

        return track_info
