from woodfish.led.diode import Diode
import time

if __name__ == "__main__":
    Diode = Diode(7)
    Diode.turn_on()
    time.sleep(1)
    Diode.turn_off()
