from press.rfp602 import rfp602
import time

if __name__ == "__main__":
    rfp602 = rfp602(24, 0.1)
    try:
        while True:
            input = rfp602.get_input()
            print("{}".format(input))
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass
