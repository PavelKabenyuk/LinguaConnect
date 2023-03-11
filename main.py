from random import *

# Import scripts
from Source import chat


def main():
    port = randint(1000, 3000)
    print("Working on port: ", port, "\n")

    client = input("Input target IP: "), int(input("Input target port: "))

    chat.reactor.listenUDP(port, chat.Client(client=client))
    chat.reactor.run()


if __name__ == '__main__':
    main()