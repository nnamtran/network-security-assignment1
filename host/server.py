import socket               # Import socket module
s = socket.socket()         # Create a socket object
host = '0.0.0.0' # Get local machine name
port = 3461                # Reserve a port for your service.


print('Server started!')
print('Waiting for clients...')

s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.


while True:
  clientsocket, address = s.accept()
  print(f"Connection from {address} has been established")
  clientsocket.send(bytes("Welcome to the server", "utf-8"))


# c, addr = s.accept()     # Establish connection with client.
# print('Got connection from,' + str(addr))
# while True:
#   msg = c.recv(1024)
#   print (str(addr) + ' >> ' + msg)
  
#   c.send(msg)
#   #c.close()                # Close the connection