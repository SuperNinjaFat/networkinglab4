"""magic_eight_ball_server.py

TODO -- complete header docstring

Champlain College CSI-235, Spring 2018
This code builds off skeleton code written by
Prof. Joshua Auerbach (jauerbach@champlain.edu)
"""

# Adapted from srv_asyncio1.py
import asyncio
import magic_eight_ball_client
import random

ANSWERS = [b"It is certain!",
           b"It is decidedly so!",
           b"Without a doubt!",
           b"Yes definitely!",
           b"You may rely on it!",
           b"As I see it, yes!",
           b"Most likely!",
           b"Outlook good!",
           b"Yes!",
           b"Signs point to yes!",
           b"Reply hazy try again!",
           b"Ask again later!",
           b"Better not tell you now!",
           b"Cannot predict now!",
           b"Concentrate and ask again!",
           b"Don't count on it!",
           b"My reply is no!",
           b"My sources say no!",
           b"Outlook not so good!",
           b"Very doubtful!"]


class EightBallServer(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        self.address = transport.get_extra_info('peername')
        self.data = b''
        print('Accepted connection from {}'.format(self.address))

    def data_received(self, data):
        self.data += data
        if self.data.endswith(b'?'):
            answer = random.choice(ANSWERS)
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
