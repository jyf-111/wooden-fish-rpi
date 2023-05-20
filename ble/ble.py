import socket
import bluetooth


class ble:
    def __init__(self):
        self.local_address = bluetooth.read_local_bdaddr()
        self.server = socket.socket(
            socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM
        )

        self.server.bind((self.local_address[0], 4))
        self.server.listen(1)

        print("Listening for connections on port", 4)

        self.client, address = self.server.accept()
        print("Connected to", address)

    def send(self, data):
        self.client.send(data.encode())

    def __del__(self):
        self.client.close()
        self.server.close()
