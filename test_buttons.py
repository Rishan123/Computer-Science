from gpiozero import Button
import time

a = Button(12,pull_up=False)
b = Button(25,pull_up=False)
c = Button(24,pull_up=False)
d = Button(23,pull_up=False)
while True:
    if a.is_pressed:
        print('hui')
    else:
        print('bye')
    time.sleep(0.1)