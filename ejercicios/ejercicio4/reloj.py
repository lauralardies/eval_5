from datetime import datetime
import os
import time

while True:
    os.system('cls')
    print(datetime.now().strftime("%H:%M:%S")) # Me da la hora y me la expresa en horas, minutos y segundos
    time.sleep(1)