import socket
import bluetooth
import logging


class Ble:
    def __init__(self, PORT):
        self.PORT = PORT
        self.local_address = bluetooth.read_local_bdaddr()
        self.server = socket.socket(
            socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM
        )
        self.server.bind((self.local_address[0], PORT))

    def accept(self):
        logging.info("start Listening for connections on port %d", self.PORT)
        self.server.listen(1)
        self.client, self.address = self.server.accept()
        logging.info("Connected to %s", self.address)

    def send(self, data):
        self.client.send(data.encode())

    def __del__(self):
        self.client.close()
        self.server.close()
