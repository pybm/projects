import time
#import beepy
import os

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1

def beep(times=1):

    for _ in range(times):

        os.system('afplay /System/Library/Sounds/Glass.aiff')

        time.sleep(0.5)

def main():
    while True:
        print("Starting 5-minute countdown.")
        countdown_timer(5 * 60)

# Initial implementation using beepy (kept for reference)        
#        for _ in range(3):
#            beepy.beep(sound=1) 
#            time.sleep(0.5)
        beep(3)

        print("Starting 1-minute countdown.")
        countdown_timer(1 * 60)
#        beepy.beep(sound=5)  # replaced due to compatibility issues
        beep(1)

if __name__ == '__main__':
    main()
