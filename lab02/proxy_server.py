import socket 
from threading import Thread

BYTES_TO_READ = 4096
PROXY_SERVER_HOST = "127.0.0.1"
PROXY_SERVER_PORT = 8080

# proxy servers accepts request and relays tehm to target and when receives response it relays to the original connection
# that requested in the first place 

# all request gonna go to google.com 
# google.com proxy target 
# server sockets for proxy clients and client sockets to connect to google 


def send_request(host, port, request_data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # sending data to google 
        client_socket.connect((host, port))
        client_socket.send(request_data)
        client_socket.shutdown(socket.SHUT_WR)

        # getting response from google 
        data = client_socket.recv(BYTES_TO_READ)
        result = b"" + data
        while(len(data) > 0):
            data = client_socket.recv(BYTES_TO_READ)
            result += data
        return result 
def handle_connection(conn, addr):
    with conn:
        print(f"Connected by {addr}")
        # initialize empty request variable 
        request = b""
        while True:
            data = conn.recv(BYTES_TO_READ)
            if not data:
                break
            print(data)
            request += data 
        response = send_request('www.google.com', 80, request)
        conn.sendall(response)

def start_threaded_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((PROXY_SERVER_HOST,PROXY_SERVER_PORT))
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # listen() defaults to 1 
        server_socket.listen(2)

        while True:
            conn, addr = server_socket.accept()

            # what function should be executed, and what arguments for the function sent in tuple
            thread = Thread(target=handle_connection, args=(conn, addr))
            thread.run()


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((PROXY_SERVER_HOST,PROXY_SERVER_PORT))
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # listen() defaults to 1 
        server_socket.listen(2)
        conn, addr = server_socket.accept()

        handle_connection(conn, addr)


# start_server()
start_threaded_server()