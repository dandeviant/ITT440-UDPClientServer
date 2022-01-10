import time
from socket import *
import os

pings = 1

# sample code
#Send ping 10 times 
# while pings < 11:  

    # #Create a UDP socket
    # clientSocket = socket(AF_INET, SOCK_DGRAM)

    # #Set a timeout value of 1 second
    # clientSocket.settimeout(1)

    # #Ping to server
    # message = 'test'

    # addr = ("192.168.88.148", 12000)

    # #Send ping
    # start = time.time()
    # msg = bytes(message, "utf-8")
    # clientSocket.sendto(msg, addr)

    # #If data is received back from server, print 
    # try:
    #     data, server = clientSocket.recvfrom(1024)
    #     data2 = data.decode('utf-8')
    #     end = time.time()
    #     elapsed = end - start
    #     print(data2 + " " + str(pings) + " "+ str(elapsed))    

    # #If data is not received back from server, print it has timed out  
    # except timeout:
    #     print('REQUEST TIMED OUT')

    # pings = pings - 1


# original code

def main():

        #Create a UDP socket
    client = socket(AF_INET, SOCK_DGRAM)
    client.connect(('192.168.88.148', 12000))

        # Set a timeout value of 1 second
    # clientSocket.settimeout(1)

        #Ping to server
    command = "hostname -I"
    output = os.popen(command)
    ip = output.read()
    print("Message = %s" %(ip))

    addr = ("192.168.88.148", 12000)

    msg = bytes(ip, "utf-8")
    client.sendto(msg, addr)

    data, addr = client.recvfrom(1024) # buffer size is 1024 bytes
    

    print("Sent by Server: %s" %(data.decode()))
    

if __name__ == "__main__":
    main()