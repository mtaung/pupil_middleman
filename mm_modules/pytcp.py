import socket 
import logging, time

class TCPsocket:
    """
    Simple python object to bind to a TCP socket. 
    """

    def __init__(self, ip, port, buffersize=1024, logger):  
        self.ip = ip
        self.port = port
        self.buffersize = buffersize
        self.logger = logging.getLogger(__name__)
        self.logger.info('Creating TCP socket object')

    def sock_bind(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.ip, self.port))  
        self.logger.info("Socket bound to {} on port {}.".format(self.ip, self.port))

    def sock_listen(self, backlog=1):
        """
        listen to the socket via recvfrom(), 
        which only runs once, thus requiring iteration.
        """
        self.sock.listen(backlog)
        self.conn, self.addr = sock.accept()
        self.data = self.conn.recv(BUFFER_SIZE)
    
    def sock_close(self)
        self.conn

