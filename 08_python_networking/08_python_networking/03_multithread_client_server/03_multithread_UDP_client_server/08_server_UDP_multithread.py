import socket
import threading

# thread function
def thd_fun(data, addr, s):
    # reverse the given string from client
    data = data[::-1]

    # send back reversed string to client
    s.sendto(data, addr)

if __name__ == '__main__':
    host = ""
    cur_port = 0
    BUFFER_SIZE = 1024

    # create and bind a UDP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, cur_port))
    cur_port = s.getsockname()[1] # get used port

    print("Socket binded to port", cur_port)
    print("Socket is listening")

    while True:
        # receive data from client
        data, addr = s.recvfrom(BUFFER_SIZE)
        print('Connected to :', addr[0], ':', addr[1])

        # start a new thread
        t = threading.Thread(target=thd_fun, args=(data, addr, s))
        t.start()

    s.close()
