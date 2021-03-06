import time
from socket import *
import os

pings = 1


# original code

def main():

        #Create a UDP socket
    client = socket(AF_INET, SOCK_DGRAM)
    client.connect(('192.168.88.148', 12000))

        # Set a timeout value of 1 second
    # clientSocket.settimeout(1)

        #Ping to server
    # command = "hostname -I"
    # output = os.popen(command)
    # ip = output.read()
    ip = input("Enter Message: ")
    print()
    print("Message = %s" %(ip))

    addr = ("192.168.88.148", 12000)

    msg = bytes(ip, "utf-8")
    client.sendto(msg, addr)

    data, addr = client.recvfrom(2048) # buffer size is 1024 bytes
    

    print("Sent by Server: %s" %(data.decode()))
    

if __name__ == "__main__":
    main()
