#Author: Abheek Gulati

import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 5005
MESSAGE = raw_input("Enter the string you'd like to capitalize: ")

print "UDP target IP: ", UDP_IP
print "UDP target port: ", UDP_PORT
print "message: ", MESSAGE

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

data, addr = sock.recvfrom(1024)
print "received string: ", data

sock.close()
