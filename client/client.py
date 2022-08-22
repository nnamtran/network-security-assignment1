import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 3461                # Reserve a port for your service.
s.connect((host, port))

print ('Connecting to ,' + host)
print ('from port:' + str(port))

msg = s.recv(1024)
print(msg.decode("utf-8"))
# while True:
#   msg = s.recv(1024)
#   s.send(msg)
 
#   print ('SERVER >> ' + msg)
#s.close                     # Close the socket when done