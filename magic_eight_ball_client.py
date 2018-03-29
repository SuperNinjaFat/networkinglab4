"""magic_eight_client.py

TODO -- complete header docstring

Champlain College CSI-235, Spring 2018
This code builds off skeleton code written by 
Prof. Joshua Auerbach (jauerbach@champlain.edu)
"""



import socket
import argparse
import time

TEST_QUESTIONS = [b'Am I awesome?', b'Will I pass this class?', 
                  b'Will a single threaded server suffice?']

class EightBallClient:

    def __init__(self, host, port):
        self.hostname = host
        self.port = port

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.hostname, self.port))
        self.byte_string_buffer = ""
        print('Client has been assigned socket name', self.sock.getsockname())
    
    def recv_until_delimiters(self, delimiters, buffer_size=1024) :
        byte_string = ""
        if len(self.byte_string_buffer) != 0 :
            # [len(delimiter):] == delimiter: # if the buffer doesn't end with a delimiter, put the new call
            byte_string = self.byte_string_buffer
        else:
            byte_string = self.sock.recv(constants.MAX_BYTES)

        for delimiter in delimeters:
            while byte_string.find(delimiter) == -1:  # if delimiter is not included, then merge.
                temp_byte_string = self.sock.recv(constants.MAX_BYTES)
                byte_string = b"".join((byte_string, temp_byte_string))
                if temp_byte_string == b"":
                    raise EOFError('Socket Closed or Down')
        # Now that there is a delimiter, either return the message that ends with a delimiter

        messages = byte_string.split(delimiter, 1)

        #zero is what we want to return and the one position is what we put in buffer
        self.byte_string_buffer = messages[1]
        # and return the first one in the list.
        return messages[0]

    def ask_question(self, question):
        pass
        
    def recv_next_response(self):
        pass
        
    def close(self):
        self.sock.close()


def run_interactive_client(host, port):
    pass

def run_single_test_client(host, port):
    pass

def test(host, port, workers):
    pass
        
        
if __name__ == '__main__':
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
