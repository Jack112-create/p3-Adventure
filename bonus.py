from threading import Thread
from time import *
import random
import threading

def countdown():
    global my_timer
    
    my_timer = random.randint(5,10)
    print(f'You have {my_timer} seconds to answer')

    for x in range(my_timer):
        my_timer = my_timer - 1
        sleep(1)
    print('Out of time')


countdown_thread = threading.Thread(target=countdown)

countdown_thread.start()
while my_timer > 0:
    print('What is 1 + 1?')
    answer = int(input('> '))
    if answer != 2:
        print('Try Again')
        answer = int(input('> '))
    elif answer == 2 and my_timer > 0:
        print('Correct')
        break
    