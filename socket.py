import socket

# Create a socket 
mysock = socket.socket(sockey.AF_INET, socket.SOCK_STREAM)
    ''' socket.socket to create a socket
        AF_INET to address family of the internet
        SOCK_STREAM indicates TCP (union-connection based) '''
    
# Connect tothe server
host = socket.gethostbyname("www.google.com")
mysock.connect((host,80))
    '''Need host to connect to
       Host is an IP address, ssometime domain,
       .gethostbyname(), perform DNS lookup
        connect(), to create connection
        port is second argument, 80 is the webtraffic'''

# Sending data on a socket
message = "GET/HTTP/1.1\r\n\r\n"
mysock.sendall(message)
    '''Message string is an HTTP GET request, to send any data
       sendall() send the data, continue until succeed'''

# Receive data on a socket
data = mysock.recv(1000)
    ''' recv() return data on the socket, blocking wait by default
        argument is maximimum number of bytes to received '''
