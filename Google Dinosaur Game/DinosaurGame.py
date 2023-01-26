import pyautogui 
from PIL import Image, ImageGrab 

import time

def hit(key):
    pyautogui.press(key)
    return

def isCollide(data):
    # for birds
    for i in range(300, 415):
        for j in range(410, 565):
            if data[i, j] < 100:
                hit("down")
                return
    # for cactus
    for i in range(300, 415):
        for j in range(565, 690):
            if data[i, j] < 100:
                hit("up")
                return
    return

if __name__ == "__main__":
    print("Dino game about to start in 3 seconds")
    time.sleep(2)
     
    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        isCollide(data)
            
        
    '''
        # Draw the rectangle for cactus
        for i in range(250, 300):
            for j in range(565, 690):
                data[i, j] = 0
        
        # Draw the rectangle for birds
        for i in range(250, 300):
            for j in range(410, 565):
                data[i, j] = 171

        image.show()
        break
    '''