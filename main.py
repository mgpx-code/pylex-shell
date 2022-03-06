import socket

hostname = socket.gethostname()
while True:
  userinput = input(hostname + '\$')
