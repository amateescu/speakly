import os
import subprocess
import sys
import zmq

gyro = os.path.join(os.path.abspath(sys.path[0]), '../gyro/gyro')
textToSpeech = os.path.join(os.path.abspath(sys.path[0]), '../tts/GoogleTextToSpeech.py')

context = zmq.Context()
sock = context.socket(zmq.SUB)
sock.setsockopt(zmq.SUBSCRIBE, '')

sock.connect(sys.argv[1])

while True:
    message = sock.recv()
    subprocess.check_call([ gyro, '5' ])
    subprocess.check_call([ 'python', textToSpeech, '-l', 'en', '-s', message, '-p'])
