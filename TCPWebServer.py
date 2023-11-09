# Import socket module for network connections
from socket import *
import sys  # Used to terminate the program

# Set up the socket for IPv4 and TCP
hostListener = socket(AF_INET, SOCK_STREAM)

# Set up and start the TCP listener
# Set the port number for the service
servicePort = 6789
# Associate the socket with a port on the machine
hostListener.bind(('', servicePort))
# Start listening for incoming connections, 1 connection allowed before refusal
hostListener.listen(1)

# Main loop to handle client connections
while True:
    # Notify that the server is ready to accept connections
    print('The server is prepared to handle requests.')
    # Block and wait for an incoming connection
    clientConn, clientAddr = hostListener.accept()  # Connection and address of the client

    try:
        # Receive the request from the client, with a buffer size of 1024 bytes
        request = clientConn.recv(1024).decode()
        # Extract the requested file name from the HTTP request
        filePath = request.split()[1]
        # Remove the leading '/' from the file path and open the file
        with open(filePath[1:]) as fileHandle:
            # Read the file content into a variable
            fileContent = fileHandle.read()

        # Send the HTTP status code for OK, meaning the file was found
        clientConn.send("HTTP/1.1 200 OK\r\n\r\n".encode())

        # Transmit the content of the file to the client
        for content in fileContent:
            clientConn.send(content.encode())
        # Signal the end of the response with a newline character
        clientConn.send("\r\n".encode())

        # Close the client connection
        clientConn.close()

    except IOError:
        # Respond with a 404 error if the file is not found
        clientConn.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        clientConn.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())

        # Close the client connection after sending the error
        clientConn.close()

# Clean up the listener socket and exit the program
hostListener.close()
sys.exit()  # End the program
