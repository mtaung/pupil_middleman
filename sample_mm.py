from pupil_middleman import pupilsocket, pytcp, pyudp
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

## Connect sockets
# udp sock
udpListeningSock = pyudp.UDPsocket('127.0.0.1', 8008)
udpListeningSock.sock_bind()

pupilLink = pupilsocket.ZMQsocket('127.0.0.1', 50020)
pupilLink.zmq_connect()
logger.info('Pupil socket connected.')

pupilLink.notify({'subject': 'start_plugin',
                    'name': 'Annotation_Capture',
                    'args': {}})
logger.info('Pupil-Recorder Annotations plugin prompted.')

pupilLink.set_time(time())
logger.info('Pupil-Recorder time set.')

## Define Triggers using a dict for pseudo switch cases
## Note that this solution will not handle mixed cases
def trigStop():
    pupilLink.stop_recording()
def trig1():
    pupilLink.send_trigger('Event1', timestamp = time())
def trig2():
    pupilLink.send_trigger('Event2', timestamp = time())
def trig3():
    pupilLink.send_trigger('Event3', timestamp = time())
def trig4():
    pupilLink.send_trigger('Event4', timestamp = time())

triggerDict = {
    b'0': trigStop,
    b'1': trig1,
    b'2': trig2,
    b'3': trig3,
    b'4': trig4
    }

## Start recording & listen to udpListeningSock
pupilLink.start_recording()
while True:
    data, time = udpListeningSock.sock_listen()
    print(data, time)
    if data:
        triggerDict[data]()
