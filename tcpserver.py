from socket import *
import pickle
from _thread import *
import sys

host = sys.argv[1] 
ThreadCount = 0
serverPort = 9890
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((host,serverPort))
serverSocket.listen(1)
print('The server is ready to receive')

def threaded_client(connectionSocket):
    while True:
        try:
            data = connectionSocket.recv(1024)
            data1 = pickle.loads(data)
        except EOFError:
            print("Connection to client closed")
            connectionSocket.close()
            break
        command = data1[0].split()
        if(command[0] == 'set'):
            key = command[1]
            value = data1[1]
            size = command[2]
            dictionary={}
            if(len(value) == int(size)):
                try: 
                    with open('data.pickle', 'rb') as file:
                        dictionary = pickle.load(file)
                except:
                    tempDict = {'key': 'value'}
                    with open('data.pickle', 'wb') as file:
                        pickle.dump(tempDict,file)
                       
                dictionary[key] = value
                with open('data.pickle', 'wb') as file:
                    pickle.dump(dictionary,file)
                message = 'STORED'
            else:
                message = 'NOT STORED'
            connectionSocket.send(message.encode())
            
        elif(command[0] == 'get'):
            key = command[1]
            with open('data.pickle', 'rb') as file:
                 dictionary = pickle.load(file)
            if key not in dictionary:
                connectionSocket.send(str.encode('VALUE '+key+' '+'\n'+'NOT FOUND\n'+'END'))
            else:
                value = dictionary[key]
                connectionSocket.send(str.encode('VALUE '+key+' '+str(len(value))+'\n'+value+'\n'+'END'))
        else:
            message='ERROR!'
            connectionSocket.send(message.encode())
    connectionSocket.close()

while 1:
    connectionSocket, addr = serverSocket.accept()
    print('Connected to: ' + addr[0] + ':' + str(addr[1]))
    start_new_thread(threaded_client, (connectionSocket, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
serverSocket.close()
