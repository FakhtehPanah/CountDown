import time

def countdown(t):
    while t:
        minutes,seconds = divmod(t, 60)
        hours, minutes = divmod(minutes, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1

t = input("Enter a number: ")

countdown(int(t))