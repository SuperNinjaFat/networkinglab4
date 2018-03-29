"""magic_eight_ball_server.py

TODO -- complete header docstring

Champlain College CSI-235, Spring 2018
This code builds off skeleton code written by
Prof. Joshua Auerbach (jauerbach@champlain.edu)
"""


# Adapted from srv_asyncio1.py
class EightBallServer:
    def connection_made(self, transport):
        self.transport = transport
        self.address = transport.get_extra_info('peername')
        self.data = b''
        print('Accepted connection from {}'.format(self.address))

    def data_received(self, data):
        self.data += data
        if self.data.endswith(b'?'):
            answer = "temp answer" # zen_utils.get_answer(self.data) # use the answers from the wiki website
            self.transport.write(answer)
            self.data = b''

    def connection_lost(self, exc):
        if exc:
            print('Client {} error: {}'.format(self.address, exc))
        elif self.data:
            print('Client {} sent {} but then closed'
                  .format(self.address, self.data))
        else:
            print('Client {} closed socket'.format(self.address))

