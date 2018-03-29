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
        pass
    
    def recv_until_delimiters(self, delimiters, buffer_size=1024) :        
        pass

    def ask_question(self, question):
        pass
        
    def recv_next_response(self):
        pass
        
    def close(self):
        pass


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
