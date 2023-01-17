import socket

BYTES_TO_READ = 4096

def get(host, port):
    # prepending b before the quotes makes it bytes
    request = b"GET / HTTP/1.1\nHost:" + host.encode('utf-8') + b"\n\n"
    # header is host field, so we need two different strings 
    # create a new socket s
    # internet socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # because were a client, we do connect 
    s.connect((host, port))
    s.send(request)

    # SHUT_WR stands for write 
    # shuts down the write socket
    # its good practice
    # google has no way of knowing if transmission is done until we shutdown WR 
    s.shutdown(socket.SHUT_WR)
    result = s.recv(BYTES_TO_READ)

    while (len(result) > 0):
        print(result)
        result = s.recv(BYTES_TO_READ)
    
    s.close()

# 80 is standard for http requests that are not encrypted
get("www.google.com", 80)