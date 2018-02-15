from mm_modules import pupilsocket, pytcp, pyudp
import logging
from time import time

## Establish Logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

fileHandler = logging.FileHandler('{}.log'.format(time()))
fileHandler.setLevel(logging.DEBUG)
fileHandler.setFormatter(formatter)

streamHandler = logging.StreamHandler()
streamHandler.setFormatter(formatter)

logger.addHandler(streamHandler)
logger.addHandler(fileHandler)
logger.info('Logging initialised at {}.'.format(fileHandler))

# TCP Socket Sample
tcpSock = pytcp.TCPsocket('127.0.0.1', 8088)
tcpSock.sock_bind()

# UDP Socket Sample
udpSock = pyudp.UDPsocket('127.0.0.1', 8008)
udpSock.sock_bind()

while True:
    udpData, t1s = udpSock.sock_listen()
    print(udpData, t1s)