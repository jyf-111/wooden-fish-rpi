import smbus


class Pcf8591:
    def __init__(self, SMBus, address):
        self.bus = smbus.SMBus(SMBus)
        self.address = address

    def read(self, chn):
        # 通道选择，范围是0-3之间
        if chn == 0:
            self.bus.write_byte(self.address, 0x40)
        if chn == 1:
            self.bus.write_byte(self.address, 0x41)
        if chn == 2:
            self.bus.write_byte(self.address, 0x42)
        if chn == 3:
            self.bus.write_byte(self.address, 0x43)
        return self.bus.read_byte(self.address)

    def write(self, val):
        # 模块输出模拟量控制，范围为0-255
        self.bus.write_byte_data(self.address, 0x40, int(val))

    def __del__(self):
        self.bus.close()
