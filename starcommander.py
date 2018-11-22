from time import sleep
from star import Star

star = Star(pwm=True)
star.off()

try:
    print("Welcome to Star Commander!")
    while True:
        num = input("What light type would you like on? ")
        if(num == '-h' or num == '--help' or num == 'help'):
            print("Here\'s some help.")
            print("0 = off")
            print("1 = on")
            print("2 = pulse")
            print("3 = blink")
            print("4 = alternate pulse inner and outer")
        elif(num == ''):
            print("Please enter a number between 0 and 4.")
        else:
            star.off()
            num = int(num)
            #if(num == 0) star will be turned off.
            if(num == 1):
                star.on()
            elif(num == 2):
                star.pulse()
            elif(num == 3):
                star.blink()
            elif(num == 4):
                star.inner.pulse()
                sleep(.5)
                star.outer.pulse()
            elif(num <  0 or num > 4):
                print("Please enter a number between 0 and 4.")
except KeyboardInterrupt:
    print("Exiting Star Commander.")
    star.close()
