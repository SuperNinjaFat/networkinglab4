"""magic_eight_client.py

TODO -- complete header docstring

Champlain College CSI-235, Spring 2018
This code builds off skeleton code written by 
Prof. Joshua Auerbach (jauerbach@champlain.edu)
"""



import socket
import argparse
import time
import magic_eight_ball_server
from threading import Thread

TEST_QUESTIONS = [b'Am I awesome?', b'Will I pass this class?',
                  b'Will a single threaded server suffice?']

TEST_RESPONSES = [b"It is certain!", b"Better not tell you now.",
                  b"Don't count on it."]

RESPONSE_DELIMITERS = [b'.', b'!']

class EightBallClient:

    def __init__(self, host, port):
        self.hostname = host
        self.port = port

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.hostname, self.port))
        self.byte_string_buffer = ""
        print('Client has been assigned socket name', self.sock.getsockname())
    
    def recv_until_delimiters(self, delimiters, buffer_size=1024):
        byte_string = ""
        if len(self.byte_string_buffer) != 0 :
            # [len(delimiter):] == delimiter: # if the buffer doesn't end with a delimiter, put the new call
            byte_string = self.byte_string_buffer
        else:
            byte_string = self.sock.recv(buffer_size)
        while not any(i in byte_string for i in delimiters):  # if delimiter is not included, then merge.
            temp_byte_string = self.sock.recv(buffer_size)
            byte_string = b"".join((byte_string, temp_byte_string))
            if temp_byte_string == b"":
                raise EOFError('Socket Closed or Down')
        # Now that there is a delimiter, either return the message that ends with a delimiter
        closestdelimiter_number = 0
        closestdelimiter = b''
        for i in range(len(delimiters)):
            if byte_string.find(delimiters[i]) >= closestdelimiter_number:
                closestdelimiter = delimiters[i]  # take the lower indices that the delimiter is found at and then use that delimiter to split the string

        messages = byte_string.split(closestdelimiter, 1)#### Not sure that delimiter_temp is the right variable.

        #zero is what we want to return and the one position is what we put in buffer
        self.byte_string_buffer = messages[1]
        # and return the first one in the list.
        return messages[0] + closestdelimiter

    def ask_question(self, question):
        """asks the server a question"""
        self.sock.send(question)

    def recv_next_response(self):
        """receives the next available question response"""
        return self.recv_until_delimiters(RESPONSE_DELIMITERS)

    def close(self):
        self.sock.close()


def run_interactive_client(host, port):
    # TODO:
    #   -create client object
    #   -loop asking user for questions
    #   -use the client to ask the question
    #   -use the client to receive the next response
    #   -print response
    EightBall = EightBallClient(host, port)
    #looping questions
    print()
    print("I am the mysterious magic 8-Ball.")
    print("Ask me a yes-or-no question! Type \"q\" to quit!")
    while True:
        print()
        question = input("8-Ball Question: ")
        if question is ('q'):
            break
        elif question.endswith("?") and question.count("?") is 1:
            EightBall.ask_question(question.encode())
            #recieve in loop
            answer = EightBall.recv_next_response()
            #print
            print(answer)
        else:
            print("Bad question syntax.")
    EightBall.close()

def run_single_test_client(host, port):
    # TODO:
    #   -create client object
    #   -use the client to repeatedly ask the test questions
    #   -use the client to get responses to all the asked questions
    #   -make sure the responses are correct
    EightBall = EightBallClient(host, port)
    #looping questions
    for i in TEST_QUESTIONS:
        print()
        print(EightBall.sock.getsockname(),i)
        EightBall.ask_question(i)
        #recieve in loop
        answer = EightBall.recv_next_response()
        #print

        print(EightBall.sock.getsockname(),answer)
        #done

def test(host, port, workers):
    # TODO -- create workers number of threads each
    #       running run_single_test_client concurrently
    for i in range(workers):
        t = ("csi235.site", 7000)
        Thread(target=run_single_test_client, args=t).start()
        
        
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
