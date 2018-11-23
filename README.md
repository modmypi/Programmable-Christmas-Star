# Programmable Christmas Tree Star
![banner](https://github.com/modmypi/Programmable-Christmas-Star/blob/master/github_star.png)

Bring some Raspberry Pi based festive cheer to your Christmas this year with the ModMyPi [Christmas Star](https://www.modmypi.com/raspberry-pi-christmas-tree-star) and bring your tree to life!

## What's in this repository

This repository should be used by cloning the repo first using

`git clone https://github.com/modmypi/Programmable-Christmas-Star`

Which will give you a copy locally.

Inside there is a script called `star.py` which contains a [GPIO Zero](https://github.com/RPi-Distro/python-gpiozero) compatible code allowing you to simply create and use the Star with only a couple of lines of Python.

To switch on the Star you can use:

```
from star import Star

star = Star()

star.on()
```

There are several example files to shouw you what can be done with the star:

### Example files

* `all_on.py` - turns on all of the LEDs.
* `in_out.py` - blinks the inner and outer ring of LEDs alternately.
* `random_leds.py` - turns on and off all the LEDs
* `slow_walk.py` - slowly walks around the LEDs increasing pace until they can't go any faster.
* `twinkle.py` - a pulsing walking pattern around the LEDs.

These files can all be run using:
`sudo python3 name_of_example.py`

## Star Commander
You can follow the [tutorial on our website](https://www.modmypi.com/blog/christmas-tree-star-guide) and learn how to use the Star Commander script.

This script allows you to command how the start glows from the command line over SSH. There are 4 built in modes (plus an off switch) to control the star with ease without having to climb the tree and attach a monitor each time.

Let us know how you get on with the Star and we hope you have a Merry Christmas.
