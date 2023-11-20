##THIS SAME CODE HAS BEEN COPIED TO TWO FILES TO MAKE OUT TWO CLIENTS FOR THE SERVER 

import socket #improting the socekt module for the connection establishment 
import threading #importing the threads module to assign the threads to client 

def recieve(client_socket):
    while True:
        try:
            #REVIENG THE MESSAGE FROM ANOTHER CLIENT 
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        #raises the error if the conneciton is lost 
        except ConnectionResetError:
            print("Connection to the server closed.")
            break

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 5555))  # Connect to the server IP and port
    #TAKING THE USER INPUT FOR THE USERNAME ALLOCATION 
    username = input("Enter your username: ")
    client_socket.send(username.encode('utf-8'))

    receive_thread = threading.Thread(target=recieve, args=(client_socket,))
    receive_thread.start()
    #sending the messages to another clients 
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

start_client()
