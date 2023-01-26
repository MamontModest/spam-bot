import subprocess
import sys
import time

server = subprocess.Popen([sys.executable, 'cheker.py'])
time.sleep(10)  # Даем время серверу на запуск

client = subprocess.Popen([sys.executable, 'bot-handlers.py'])
time.sleep(10)

client2 = subprocess.Popen([sys.executable, 'spam.py'])

server.wait()