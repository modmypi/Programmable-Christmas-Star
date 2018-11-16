from star import Star
from time import sleep

star = Star()

try:
    star.on()
    while True:
        sleep(.5)
except KeyboardInterrupt:
    star.close()
