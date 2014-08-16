MusicDisplayPi
===============

*MusicDisplayPi* is a Python program for displaying network music player information (from e.g. `mpd <http://www.musicpd.org/>`_) on a text display.

Raspberry Pi
------------
The target use case for *MusicDisplayPi* has been to run it on a network-connected Raspberry Pi and display the music track information via an attached LCD screen (using ``PiLcdDisplay``). In the case of MPD, the client could be running on the Pi itself (with attached speakers) to create a self-contained network music player with display. Alternatively, the client could be running elsewhere on the network and the Raspberry Pi setup simply acts as a remote display.

.. image:: http://i.imgur.com/8qb79od.gif

Curses
------
The included ``CursesDisplay`` allows for the track information to be shown within a terminal via a curses-based display.
