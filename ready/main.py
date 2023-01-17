import subprocess
import sys
import time

server = subprocess.Popen([sys.executable, 'cheker.py'])
time.sleep(10)  # Даем время серверу на запуск

client = subprocess.Popen([sys.executable, 'bot-handlers.py'])

server.wait()