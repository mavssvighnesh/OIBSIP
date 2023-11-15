import socket
import threading

def handle_client(client_socket, client_address, username):
    print(f"Accepted connection from {client_address[0]}:{client_address[1]} as {username}")

    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print(f"Connection closed with {client_address[0]}:{client_address[1]}")
                break

            print(f"{username}: {message}")
            # Broadcast the received message to all clients (except the sender)
            for c in clients:
                if c != client_socket:
                    c.send(f"{username}: {message}".encode('utf-8'))
        except ConnectionResetError:
            break

    client_socket.close()
    clients.remove(client_socket)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 5555))  # Change the IP address and port as needed
    server_socket.listen(2)
    print("Server is listening for incoming connections...")

    while True:
        client, address = server_socket.accept()
        username = client.recv(1024).decode('utf-8')
        clients.append(client)

        # Create a thread for each client
        client_handler = threading.Thread(target=handle_client, args=(client, address, username))
        client_handler.start()

clients = []

if __name__ == "__main__":
    start_server()
