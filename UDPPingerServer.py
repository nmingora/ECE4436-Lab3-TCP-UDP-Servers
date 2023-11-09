# Import modules for the UDP echo server
import random
from socket import *

# Set up the UDP socket for communication
echoServer = socket(AF_INET, SOCK_DGRAM)
# Bind the socket to an open port
echoServer.bind(('', 12000))

while True:
    # Decide whether to simulate packet loss
    packetLossSim = random.randint(0, 10)
    # Wait for a message and record the sender's address
    clientData, clientAddress = echoServer.recvfrom(1024)
    # Convert the client's message to uppercase
    clientData = clientData.upper()
    # Simulate packet loss: If the simulation number is below 4, do not respond
    if packetLossSim < 4:
        continue
    # If no packet loss, send the modified data back to the client
    echoServer.sendto(clientData, clientAddress)

