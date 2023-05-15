from dac.pcf8591 import pcf8591
import time

if __name__ == "__main__":
    pcf8591 = pcf8591(1, 0x48)
    try:
        while True:
            # print('AIN0 = ', pcf8591.read(0))
            # print('AIN1 = ', pcf8591.read(1))
            # print('AIN2 = ', pcf8591.read(2))
            # print('AIN3 = ', pcf8591.read(3))
            tmp = pcf8591.read(0)
            print(tmp)
            if tmp > 235:
                pcf8591.write(255)
            else:
                pcf8591.write(0)
            time.sleep(0.01)
    except KeyboardInterrupt:
        pass
    finally:
        pcf8591.write(0)
