from random import randint

import socket

# Import scripts
from Source import chat
from Tests import local


def main():
    my_port = randint(1000, 3000)
    my_ip = socket.gethostbyname(socket.gethostname())
    print("My ip:", my_ip)
    print("My port:", my_port, "\n")

    client_ip = input("Input target IP: ")
    client_port = input("Input target port: ")

    start = chat.Chat(my_ip, int(my_port), client_ip, int(client_port))
    start.run()


if __name__ == '__main__':
    main()