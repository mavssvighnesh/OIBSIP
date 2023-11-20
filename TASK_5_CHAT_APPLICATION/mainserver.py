import socket #importing socket module to establish the connection using ip 

import threading #importing the threading module to run multiple clients in multiple threads simultaneously 

#this method handles the clients and prints the messages of them 
def client_assigner(client_soc,client_ip, username):
    #print the connection info 
    print(f"Accepted connection from {client_ip[0]}:{client_ip[1]} as {username}")

    while True:
        try:
            message=client_soc.recv(1024).decode('utf-8')
            if not message:
                print(f"Connection closed with {client_ip[0]}:{client_ip[1]}")
                break
            #prints the username and message of the user 
            print(f"{username}: {message}")

            # Broadcast the received message to all clients (except the sender)
            for c in clients:
                if c != client_soc:
                    c.send(f"{username}: {message}".encode('utf-8'))
        #exception 
        except ConnectionResetError:
            break
    #closes the connection 
    client_soc.close()
    clients.remove(client_soc)

def main():
    server_soc=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_soc.bind(('127.0.0.1', 5555))  # Change the IP address and port as needed
    server_soc.listen(2)
    print("Server is listening for incoming connections...")

    while True:
        client, address = server_soc.accept()
        username = client.recv(1024).decode('utf-8')
        clients.append(client)

        # Create a thread for each client
        client_handler = threading.Thread(target=client_assigner, args=(client, address, username))
        client_handler.start()

clients = []


main()
