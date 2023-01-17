import socket 

BYTES_TO_READ = 4096
# need to specify host address because were a server
# can also use 'localhost'
HOST = "127.0.0.1"
# 8080 is nice little con   vention
PORT = 8080

def handle_connection(conn, addr):
    ''' handles connection '''
    # conn is a socket, but not the same socket that was used to create the socket. I think its more of a
    # communication socket between the server and the client maybe?
    with conn:
        print(f"Connect by: {addr}")
        while True:
            data = conn.recv(BYTES_TO_READ)
            # break out of while loop if socket collpases or shuts down
            if not data:
                break
            # otherwise
            print(data)
            # send it right back on that same connection where we recieved data from
            # sendall vs. send technically both work similarly, send doesnt guarantee that all data is sent. 
            conn.sendall(data)


def start_server():
    ''' starts server '''
    # with block autocloses some resources otherwise that socket remains open and thats not good 
    # creates resource as s, but autocloses that socket created after its used, like an automated s.close()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # bind to our host-port
        s.bind((HOST,PORT))

        # set socket options -> setsockopt(level, option, value)
        # 
        # resuse allows socket to rebind to the same addr under certain circumstances. During weird time out phase. This is will allow us to 
        # rebind to the same addr before the conn expires

        # when socket is closed theres a period of time, that socket conn remain open to finish up the 
        # ack that it is being closed and nothign else comes in on it

        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # listen on the host port
        s.listen()
    
        # after listening, handle connection
        # accepts conn that was just made and address it came from
        conn, addr = s.accept()
        handle_connection(conn, addr)


start_server()