import subprocess
import sys
import time


client = subprocess.Popen([sys.executable, 'bot-handlers.py'])
time.sleep(60)

client2 = subprocess.Popen([sys.executable, 'spam.py'])

client.wait()