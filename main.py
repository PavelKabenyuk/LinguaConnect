from random import randint

# Import scripts
from Source import chat


def main():
    my_port = randint(1000, 3000)
    print("My port: ", my_port, "\n")

    client_ip = input("Input target IP: ")
    client_port = input("Input target port: ")

    start = chat.Chat(my_port, client_ip, client_port)
    start.run()


if __name__ == '__main__':
    main()