import pyautogui as pt
from pynput import mouse 
import pyperclip as pc
from pynput.mouse import Button, Controller
from time import sleep 

pt.FAILSAFE = True
mouse = Controller()

def nav_to_image(image, clicks, off_x=0, off_y=0):
    position = pt.locateCenterOnScreen(image, confidence=.8)

    if position is None:
        print(f'{image} not found...')
        return 0 
    else:
        pt.moveTo(position, duration=.5)
        pt.moveRel(off_x, off_y, duration=.2)
        pt.click(clicks=clicks, interval=.1)

def get_message():
    nav_to_image('images\paperclip.png', 0, off_y=-80, off_x=+60)
    mouse.click(Button.left, 3)
    pt.rightClick()

    copy = nav_to_image('images/copy.png', 1)
    sleep(.5)
    return pc.paste() if copy != 0 else 0

def send_message(msg):
    nav_to_image('images/paperclip.png', 2, off_x=100)
    pt.typewrite(msg, interval=.1)
    pt.typewrite('\n')

def close_reply_box():
    nav_to_image('images/cross.png', 2)

def process_message(msg):
    raw_msg = msg.lower()

    if raw_msg == 'hello':
        return 'Hi dude , my name is beetle the bot'
    elif raw_msg == 'how are you ??':
        return 'I am binary.....got it !!'
    elif 'ok' in raw_msg:
        return 'Nice to talk to you man....right now i cant unserstand anything more , but who knows maybe one day i will able to become like the google assistant , you reply me with anything now if you want to try !!!'
    else:
        return 'I did not understand what you wrote.'

# loop the code 
delay = 10 
last_message = ''

counter = 0 
sleep(3)
while counter < 6:
    # checks for new messages
    nav_to_image('images/green_circle.png', 2, off_x=-100) #step 1
    close_reply_box() # step 2
    message = get_message() # step 3
    if message != 0 and message != last_message:
        last_message = message
        send_message(process_message(message))
    else:
        print('No new messages.....')
        counter += 1  
        

    sleep(10)
