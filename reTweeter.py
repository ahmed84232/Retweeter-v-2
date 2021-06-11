from pyautogui import locateAllOnScreen, press, moveTo, click, center, hotkey
from pyperclip import paste, copy
from os.path import join, dirname
from time import sleep
from pynput.keyboard import Key, Listener
from threading import Thread
import winsound

retweeter_running = False
mypath = dirname(__file__)


def retweeter():

    global retweeter_running
    rt = 0

    while retweeter_running:

        sleep(0.5)
        locations1 = locateAllOnScreen(join(mypath, "Retweet1.png"), confidence=0.9)
        locations2 = locateAllOnScreen(join(mypath, "Retweet2.png"), confidence=0.9)
        locations3 = locateAllOnScreen(join(mypath, "Retweet3.png"), confidence=0.9)


        for loc in locations1:
            
            if not retweeter_running or rt == 300:
                break
            
            if retweeter_running and rt<300:
                
                x, y = center(loc)
                moveTo(x, y, 0.1)
                click()
                press("enter")
                rt +=1
                
        for loc2 in locations2:
            
            if retweeter_running and rt<300:

                x, y = center(loc2)
                moveTo(x, y, 0.1)
                click()
                press("enter")
                rt += 1
               
        for loc3 in locations3:

            if retweeter_running and rt<300:

                x, y = center(loc3)
                moveTo(x, y, 0.1)
                click()
                press("enter")
                rt += 1


        moveTo(1229, 987, 0.1)
        press("pagedown")


def on_press(key):

    global retweeter_running

    if key == Key.left and not retweeter_running:

        retweeter_running = True
        t = Thread(target=retweeter)
        t.start()

    elif key == Key.right:

        retweeter_running = False


with Listener(on_press=on_press) as listener:

    print("Press LEFT to start retweeting all the Page, RIGHT to stop the ReTweeter.")
    listener.join()
