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


if __name__ == '__main__':
    #EDIT THIS PASTED IN CODE
    address = zen_utils.parse_command_line('asyncio server using callbacks')
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ZenServer, *address)
    server = loop.run_until_complete(coro)
    print('Listening at {}'.format(address))
    try:
        loop.run_forever()
    finally:
        server.close()
        loop.close()

    #EDIT THIS PASTED IN CODE
    parser = argparse.ArgumentParser(description='Example client')
    parser.add_argument('host', help='IP or hostname')
    parser.add_argument('-p', metavar='port', type=int, default=7000,
                        help='TCP port (default 7000)')
    parser.add_argument('-t', action='store_true', help='test mode')
    parser.add_argument('-n', metavar='num threads', type=int, default=4,
                        help='Num threads for test mode')
    args = parser.parse_args()
    if args.t:
        test(args.host, args.p, args.n)
    else:
        run_interactive_client(args.host, args.p)
