from socket import *
import sys
hostListener = socket(AF_INET, SOCK_STREAM)
servicePort = 6789
hostListener.bind(('', servicePort))
hostListener.listen(1)
while True:
    clientConn, clientAddr = hostListener.accept()
    try:
        request = clientConn.recv(1024).decode()
        filePath = request.split()[1]
        with open(filePath[1:]) as fileHandle:
            fileContent = fileHandle.read()
        clientConn.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        for content in fileContent:
            clientConn.send(content.encode())
        clientConn.send("\r\n".encode())
        clientConn.close()
    except IOError:
        clientConn.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        clientConn.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        clientConn.close()
hostListener.close()
sys.exit()
