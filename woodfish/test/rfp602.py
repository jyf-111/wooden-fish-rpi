from press.rfp602_do import Rfp602
import time

if __name__ == "__main__":
    Rfp602 = Rfp602(24, 0.1)
    try:
        while True:
            input = Rfp602.get_input()
            print("{}".format(input))
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass
