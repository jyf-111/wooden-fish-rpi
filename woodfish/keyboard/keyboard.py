import socket
import logging
import dbus

import keyboard.keymap as keymap
from importlib import resources
import source
from content import Content
from threading import Thread


class Keyboard(Thread):
    PORT_CTRL = 17
    PORT_INTR = 19

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

        self.content = Content()
        self.content.load_content()

    def __del__(self):
        self._disconnect()

    def _accept(self):
        logging.debug("Listening control channel")
        self.conn_control, self.addr_info = self.s_control.accept()
        logging.debug("Connected control channel")

        logging.debug("Listening interrupt channel")
        self.conn_interrupt, self.addr_info = self.s_interrupt.accept()
        logging.debug("Connected interrupt channel")

    def _disconnect(self):
        if hasattr(self, "conn_control"):
            self.conn_control.close()
        if hasattr(self, "conn_interrupt"):
            self.conn_interrupt.close()

    def send(self):
        self.conn_interrupt.send(
            bytes(keymap.convert_char_to_hid(self.content.get_next_char()))
        )
        self.conn_interrupt.send(bytes(keymap.convert_char_to_hid("NONE")))

    def run(self):
        logging.info("wait for keyboard accept")
        while True:
            try:
                self._accept()
                logging.info("keyboard connection accepted")
            except Exception as e:
                logging.warn(f"Error occurred: {e}")
                self._disconnect()
