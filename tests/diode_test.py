from led.diode import diode
import time

if __name__ == "__main__":
    diode = diode(7)
    diode.turn_on()
    time.sleep(1)
    diode.turn_off()
