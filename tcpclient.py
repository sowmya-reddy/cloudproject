from socket import *
import pickle
import threading
import sys
import time

serverName = sys.argv[1]
serverPort = 9890

def threaded_clients(clientSocket):
    clientSocket.connect((serverName,serverPort))
    print("Connected to server. Use commands 'set' and 'get' to retrieve or store key value pairs. Use Ctrl D in new line to exit command line and 'quit' to close the connection")
    close_flag=False
    while True:
        user_writing = [] 
        while True: 
           try:
               cmd=input()
               if(cmd=='quit'):
                    close_flag=True
                    break
               user_writing.append(cmd)
           except EOFError:
               break
        if(close_flag):
            break
        data = pickle.dumps(user_writing)
        clientSocket.sendall(data)
        time.sleep(10)
        value = clientSocket.recv(1024)
        print(value.decode("utf-8"))
    print("Connection closed")
    clientSocket.close()
  
clientSocket = socket(AF_INET, SOCK_STREAM)
t = threading.Thread(target=threaded_clients, args=(clientSocket,))
t.start()
