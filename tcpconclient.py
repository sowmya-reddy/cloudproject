from socket import *
import pickle
import threading
import sys

serverName = sys.argv[2]
serverPort = 9890

def threaded_clients(clientSocket):
    clientSocket.connect((serverName,serverPort))
    print("Connected to server. Use commands 'set' and 'get' to retrieve or store key value pairs. Use Ctrl D in new line to exit command line and 'quit' to close the connection")
    datakey=['Misfits','Inseparable','Matrix','Poet','Freedom','Beautiful','Magician','Unbound','Harlem','Emptiness','Cuckoo']
    datavalue=['Misfits','Inseparable','Matrix','Poet Warrior','On Freedom: Four Songs of Care and Constraint','Beautiful World','The Magician','Unbound','Harlem Shuffle','The Book of Form and Emptiness','Cloud Cuckoo Land']
    if(cmd=='get'):
        while True:
            for i in range(len(datakey)):
               keyval=[]
               keyval.append('get '+ datakey[i])
               data = pickle.dumps(keyval)
               clientSocket.sendall(data)
               key=datakey[i]
               value = clientSocket.recv(1024)
               if(value.decode("utf-8")=="NOT STORED"):
                   print('VALUE ' + key + '\n' + 'NOT STORED')
               elif(value.decode("utf-8")=="STORED"):
                   print('VALUE ' + key + '\n' + 'STORED')
               else:
                   print('VALUE ' + key + ' '+ str(len(value)))
                   print(value.decode("utf-8"))
        print("Connection closed")
        clientSocket.close()
    elif(cmd=='set'):
        for i in range(len(datakey)):
           keyval=[]
           keyval.append('set '+ datakey[i]+ ' ' + str(len(datavalue[i])))
           keyval.append(str(datavalue[i]))
           data = pickle.dumps(keyval)
           clientSocket.sendall(data)
           key=datakey[i]
           value = clientSocket.recv(1024)
           if(value.decode("utf-8")=="NOT STORED"):
               print('VALUE ' + key + '\n' + 'NOT STORED')
           elif(value.decode("utf-8")=="STORED"):
               print('VALUE ' + key + '\n' + 'STORED')
           else:
               print('VALUE ' + key + ' '+ str(len(value)))
               print(value.decode("utf-8"))
        print("Connection closed")
        clientSocket.close()

cmd=sys.argv[1]
clientSocket = socket(AF_INET, SOCK_STREAM)
t = threading.Thread(target=threaded_clients, args=(clientSocket,))
t.start()

