import RPi.GPIO as GPIO
from gpiozero import Button
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
motor_pins = [4,17,27,22]
button_pins = [23,24,25,12]
question = 1
asked = False
for pin in motor_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)
for pin in button_pins:
    GPIO.setup(pin,GPIO.IN)
GPIO.setup(8,GPIO.OUT)

halfstep_seq = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
]
def check_answer(correct_button,incorrect_buttons):
    global motor_pins, pin, question
    if correct_button:
        print('in correct loop')
        os.system('espeak "well done" --stdout |aplay')
        GPIO.output(8,True)
        for i in range(512):
            for halfstep in range(8):
                for pin in range(4):
                    GPIO.output(motor_pins[pin], halfstep_seq[halfstep][pin])
                time.sleep(0.001)
        question += 1
#         time.sleep(0.5)
    else:
        print('incorrect')
        if any(incorrect_buttons) == True:
            GPIO.output(8,False)
            print('deifinitely incorrect')
            os.system('espeak "incorrect" --stdout |aplay')
            question += 1
        
        else:
            print('please press button')
            
        
               
while True:
    d = GPIO.input(23)
    c = GPIO.input(24)
    b = GPIO.input(25)
    a = GPIO.input(12)
    print(a,b,c,d)
    if question == 1:
        GPIO.output(8,False)
        incorrect_buttons = [c,b,a]
        if asked == False:
            os.system('espeak "How was information stored on the first computer ever made? AE: SD Cards, BE: USB drives, CE: Hard drives, or DEE: Punch cards" --stdout |aplay')
            asked = True
        else:
            check_answer(d,incorrect_buttons)
            
        
    elif question == 2:
        GPIO.output(8,False)
        incorrect_buttons = [d,c,a]
        if asked == True:
            os.system('espeak "True or false? A light bulb is an input device. AE: True, BE: False " --stdout |aplay')
            asked = False
        else:
            check_answer(b,incorrect_buttons)
        

    elif question == 3:
        GPIO.output(8,False)
        incorrect_buttons = [d,c,b]
        if asked == False:
            os.system('espeak "What part of the computer performs calculations for the user? AE: The CPU, BE: The Internet, CE: Calculators, DEE: The RAM" --stdout |aplay')
            asked = True
        else:
            check_answer(a,incorrect_buttons)
        
    elif question == 4:
        GPIO.output(8,False)
        incorrect_buttons = [d,b,a]
        if asked == True:
            os.system('espeak "Which part of the computer handles monitors and displays? AE: The CPU, BE: The RAM, CE: The GPU, DEE: The PSU " --stdout |aplay')
            asked = False
        else:
            check_answer(c,incorrect_buttons)
    
    elif question == 5:
        GPIO.output(8,False)
        incorrect_buttons = [c,b,a]
        if asked == False:
            os.system('espeak "What part of the computer handles power? AE: The PSU, BE: The GPU, CE: The CPU, DEE: The RAM" --stdout |aplay')
            asked = True
        else:
            check_answer(a,incorrect_buttons)
    
    elif question == 6:
        GPIO.output(8,False)
        incorrect_buttons = [d,b,a]
        if asked == True:
            os.system('espeak "What parts make up RAM? AE: Lights and speakers, BE: Speakers and displays CE: Transistors and Capacitors, DEE: Resistors and Transistors" --stdout |aplay')
            asked = False
        else:
            check_answer(c,incorrect_buttons)

    elif question == 7:
        GPIO.output(8,False)
        incorrect_buttons = [c,b,a]
        if asked == False:
            os.system('espeak "How many megabytes are in a gigabyte? AE: ten, BE: a hundred, CE: a billion, DEE: a thousand " --stdout |aplay')
            asked = True
        else:
            check_answer(d,incorrect_buttons)
            
    elif question == 8:
        GPIO.output(8,False)
        incorrect_buttons = [c,d,b]
        if asked == True:
            os.system('espeak "Which component can store electrical energy? AE: Transistors, BE: Capacitors" --stdout |aplay')
            asked = False
        else:
            check_answer(b,incorrect_buttons)

    
    elif question == 9:
        GPIO.output(8,False)
        incorrect_buttons = [a,d,c]
        if asked == False:
            os.system('espeak "Is a printer an example of an output device?, AE: No, BE: Yes" --stdout |aplay')
            asked = True
        else:
            check_answer(b,incorrect_buttons)
    

    elif question == 10:
        GPIO.output(8,False)
        incorrect_buttons = [c,b,d]
        if asked == True:
            os.system('espeak "Does RAM store short-term or long-term memory?, AE: Short-term, BE: Long-term" --stdout |aplay')
            asked = False
        else:
            check_answer(a,incorrect_buttons) 
    

    elif question == 11:
        GPIO.output(8,False)
        incorrect_buttons = [a,c,b]
        if asked == False:
            os.system('espeak "How many bits in a nibble? AE: 1, BE: 2, CE: 3, DE: 4" --stdout |aplay')
            asked = True
        else:
            check_answer(d,incorrect_buttons) 
    time.sleep(0.15)
    
    
    
    
    
    
    
    
    