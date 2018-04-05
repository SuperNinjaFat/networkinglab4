"""magic_eight_server.py

Author:              Tony Calarese, Paul Lindberg
Class:               CSI-235
Assignment:          Lab 4
Date Assigned:       3/07/2018
Due Date:            4/06/2018 11:59 PM
Description:
To have a working magic eight ball working on a local client and getting it to work on a
server working on a localhost as well with the magic_eight_ball_server.py as well.

This code has been adapted from that provided by Prof. Joshua Auerbach:
Champlain College CSI-235, Spring 2018
The following code was written by Tony Calarese (anthony.calarese@champlain.edu) and was adpted from Joshua Auberach's code for  lab 2
Also Paul Lindberg (paul.lindberg@mymail.champlain.edu)
"""

# Adapted from srv_asyncio1.py
import asyncio
import argparse
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
        """"
        This function will make sure that the function is properly connecting and verify the connection that is being made
        """"
        self.transport = transport
        self.address = transport.get_extra_info('peername')
        self.data = b''
        print('Accepted connection from {}'.format(self.address))

    # most changed part
    def data_received(self, data):
        """"
        This will buffer the data that is being received from the client
        """"
        self.data += data
        if self.data.endswith(b'?'):
            answer = random.choice(ANSWERS)
            self.transport.write(answer)
            self.data = b''

    def connection_lost(self, exc):
        """"
        This function will conqure if the connection is lost and will respond corelating to what has happened to the port and such
        """"
        if exc:
            print('Client {} error: {}'.format(self.address, exc))
        elif self.data:
            print('Client {} sent {} but then closed'
                  .format(self.address, self.data))
        else:
            print('Client {} closed socket'.format(self.address))


if __name__ == '__main__':
    #address = "localhost"# 127.0.0.1 #localhost
    loop = asyncio.get_event_loop()
    coro = loop.create_server(EightBallServer, "localhost", 7000)
    server = loop.run_until_complete(coro)
    print('Listening at {}'.format("localhost"))
    try:
        loop.run_forever()
    finally:
        server.close()
        loop.close()

