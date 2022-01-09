import time
from socket import *

pings = 1

#Send ping 10 times 
while pings < 11:  

    #Create a UDP socket
    clientSocket = socket(AF_INET, SOCK_DGRAM)

    #Set a timeout value of 1 second
    clientSocket.settimeout(1)

    #Ping to server
    message = 'test'

    addr = ("192.168.88.148", 12000)

    #Send ping
    start = time.time()
    msg = bytes(message, "utf-8")
    clientSocket.sendto(msg, addr)

    #If data is received back from server, print 
    try:
        data, server = clientSocket.recvfrom(1024)
        data2 = data.decode('utf-8')
        end = time.time()
        elapsed = end - start
        print(data2 + " " + str(pings) + " "+ str(elapsed))    

    #If data is not received back from server, print it has timed out  
    except timeout:
        print('REQUEST TIMED OUT')

    pings = pings - 1