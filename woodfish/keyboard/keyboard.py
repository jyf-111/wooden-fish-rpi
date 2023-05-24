import socket
import logging
import dbus
import os

import keyboard.keymap as keymap
from importlib import resources
import source
from content import Content
from threading import Event, Thread


class Keyboard(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        bus = dbus.SystemBus()
        bluez = bus.get_object("org.bluez", "/org/bluez")
        manager = dbus.Interface(bluez, "org.bluez.ProfileManager1")

        with resources.open_text(source, "sdp_record.xml") as f:
            opts = {
                "AutoConnect": True,
                "ServiceRecord": f.read(),
            }

        uuid = "05262649-d40f-483d-b445-73b000d19028"
        manager.RegisterProfile("/org/bluez/hci0", uuid, opts)
        logging.debug("Registered keyboard profile")

        self.PORT_CTRL = 17
        self.PORT_INTR = 19

        self.s_control = socket.socket(
            socket.AF_BLUETOOTH, socket.SOCK_SEQPACKET, socket.BTPROTO_L2CAP
        )
        self.s_control.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s_control.bind((socket.BDADDR_ANY, self.PORT_CTRL))
        self.s_control.listen(5)

        self.s_interrupt = socket.socket(
            socket.AF_BLUETOOTH, socket.SOCK_SEQPACKET, socket.BTPROTO_L2CAP
        )
        self.s_interrupt.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s_interrupt.bind((socket.BDADDR_ANY, self.PORT_INTR))
        self.s_interrupt.listen(5)

        self.event = Event()
        self.content = Content()

        os.system("hciconfig hci0 up")
        os.system("hciconfig hci0 name 'woodfish'")
        os.system("hciconfig hci0 class 0x000500")
        os.system("hciconfig hci0 piscan")
        os.system("hciconfig hci0 sspmode 1")
        os.system("hciconfig hci0 noauth")
        os.system("hciconfig hci0 noencrypt")
        os.system("sdptool add SP")

        self.content.load_content()

    def __del__(self):
        self.s_interrupt.close()
        self.s_control.close()

    def _accept(self):
        logging.debug("Listening control channel")
        self.conn_control, self.addr_info = self.s_control.accept()
        logging.debug("Connected control channel")

        logging.debug("Listening interrupt channel")
        self.conn_interrupt, self.addr_info = self.s_interrupt.accept()
        logging.debug("Connected interrupt channel")

    def _send(self):
        self.conn_interrupt.send(
            bytes(keymap.convert_char_to_hid(self.content.get_next_char()))
        )
        self.conn_interrupt.send(bytes(keymap.convert_char_to_hid("NONE")))

    def run(self):
        logging.info("wait for keyboard accept")
        self._accept()
        logging.info("keyboard accepted")

        while True:
            self.event.wait()
            self._send()
            self.event.clear()
