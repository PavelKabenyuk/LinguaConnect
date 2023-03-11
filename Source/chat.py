from vidstream import AudioSender
from vidstream import AudioReceiver

import threading
import socket


class Chat:
    def __init__(self, my_port, client_ip, client_port):
        self.my_ip = socket.gethostbyname(socket.gethostname())
        self.my_port = my_port
        self.client_ip = client_ip
        self.client_port = client_port

    def run(self):
        receiver = AudioReceiver(self.my_ip, self.my_port)
        receive_thread = threading.Thread(target=receiver.start_server())

        sender = AudioSender(self.client_ip, self.client_port)
        sender_thread = threading.Thread(target=sender.start_stream())

        receive_thread.start()
        sender_thread.start()