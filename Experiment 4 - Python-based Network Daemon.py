import socket 
 
def start_daemon(host='0.0.0.0', port=5000): 
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    server_socket.bind((host, port)) 
    server_socket.listen(5) 
    print(f"Listening on {host}:{port}") 
 
    while True: 
        client_socket, client_address = server_socket.accept() 
        print(f"Connection received from {client_address}") 
        client_socket.sendall(b"Hello! You are connected.\n") 
        client_socket.close() 
 
start_daemon()
