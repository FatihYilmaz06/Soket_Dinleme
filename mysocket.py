import socket
import threading

bind_ip = '0.0.0.0' # Bilgisayarın IP'si örn(192.168.1.201)
bind_port = 0000 #dinlemek istediğiniz port Orn(6060)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)  # max backlog of connections

print('Listening on {}:{}'.format(bind_ip, bind_port))



def handle_client_connection(client_socket):
    request = client_socket.recv(1024)
    print('Received {}'.format(request))

    # client_socket.send('ACK!')
    # client_socket.close()


while True:
    client_sock, address = server.accept()
    print('Accepted connection from {}:{}'.format(address[0], address[1]))

    client_handler = threading.Thread(
        target=handle_client_connection,
        args=(client_sock,)
        #
    )
    client_handler.start()
