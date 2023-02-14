import subprocess
import sys
import time


client = subprocess.Popen([sys.executable, 'bot-handlers.py'])
time.sleep(10)

client2 = subprocess.Popen([sys.executable, 'cheker.py'])

client.wait()