import socket
import sys

def client(PORT):
    IP = 'localhost'
    BUFFER_SIZE = 1024
    MESSAGE = "Hello, World!\n"

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(MESSAGE.encode("utf-8"), (IP, PORT))

    data, addr = s.recvfrom(BUFFER_SIZE)
    print("received data: " + data.decode("utf-8"))

    s.close()

if __name__ == "__main__":
    try:
        PORT = sys.argv[1]
    except IndexError:
        print("Please, specify PORT arg...")

    assert PORT != "", 'specify port'
    client(int(PORT))
