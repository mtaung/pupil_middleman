"""
This is a very simple script to debug/demo the way middleman retrieves & sends bytes.
What is seen here can be implemented in any language, to comm. with pupil-recorder
especially those without native zmq support. 
"""

import socket
import time

UDP_IP = "localhost"
UDP_PORT = 8008

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)

beepSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def ping(input):
    beepSock.sendto(bytes(str(input), "utf-8"), (UDP_IP, UDP_PORT))

# Ugly timestamper necessary for best speed
# ping((int(round(time.time()*1000))))

ping('1')
time.sleep(5)
ping('2')
time.sleep(5)
ping('3')
time.sleep(5)
ping('4')
time.sleep(5)
ping('0')
