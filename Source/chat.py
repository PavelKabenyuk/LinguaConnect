from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
import pyaudio


class Client(DatagramProtocol):
    def __init__(self, client="client"):
        self.client = client

    def startProtocol(self):
        py_audio = pyaudio.PyAudio()
        self.buffer = 1024
        #TODO need to defind number of chanels by itself
        self.output_stream = py_audio.open(format=pyaudio.paInt16,
                                           output=True, rate=44100, channels=1,
                                           frames_per_buffer=self.buffer)
        self.input_stream = py_audio.open(format=pyaudio.paInt16,
                                          input=True, rate=44100, channels=1,
                                          frames_per_buffer=self.buffer)
        reactor.callInThread(self.record)

    def record(self):
        while True:
            data = self.input_stream.read(self.buffer)
            self.transport.write(data, self.client)

    def datagramReceived(self, datagram, addr):
        self.output_stream.write(datagram)