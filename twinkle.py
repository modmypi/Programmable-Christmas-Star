from star import Star
from time import sleep

star = Star(pwm=True)

try:
    leds = star.leds
    while True:
        for led in leds:
            led.pulse()
            sleep(.2)
except KeyboardInterrupt:
    star.close()
