import interface.mpdinterface
import display.pilcddisplay
import controller
import time
import sys

def main():

    disp = display.pilcddisplay.PiLcdDisplay(
        lines=4,
        line_length=20,
        update_interval=0.5)
    
    cont = controller.MainController(
        interface.mpdinterface.MpdInterface(),
        disp)

    cont.init()

    try:
        cont.start()

        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Caught KeyboardInterrupt...")
        cont.stop()
        sys.exit(1)

if __name__ == "__main__":
    main()
