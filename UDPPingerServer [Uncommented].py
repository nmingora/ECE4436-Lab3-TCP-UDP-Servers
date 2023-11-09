import random
from socket import *

echoServer = socket(AF_INET, SOCK_DGRAM)
echoServer.bind(('', 12000))

while True:
    packetLossSim = random.randint(0, 10)
    clientData, clientAddress = echoServer.recvfrom(1024)
    clientData = clientData.upper()
    if packetLossSim < 4:
        continue
    echoServer.sendto(clientData, clientAddress)
