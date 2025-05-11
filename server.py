import socket

# Set up the socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to all IPs on port 8080
server_socket.bind(('', 8080))
server_socket.listen(1)

print("Server is running... Visit your Pi's IP address on port 8080")

while True:
    client_connection, client_address = server_socket.accept()
    print("Got a request!")
    
    # Create a basic HTTP response
    response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
    response += "<html><body><h1>Hello from Raspberry Pi!</h1></body></html>"
    
    client_connection.sendall(response.encode())
    client_connection.close()
