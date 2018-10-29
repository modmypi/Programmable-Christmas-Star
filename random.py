from star import Star
from gpiozero.tools import random_values
from signal import pause

star = Star(pwm=True)
leds = star.leds

try:
    for led in leds:
        led.source_delay = 0.1
        led.source = random_values()
    pause()
except KeyboardInterrupt:
    star.off()
    star.close()
