import pyautogui
import time
import keyboard

def turn_90_degrees():
    screen_width, screen_height, = pyautogui.size()

    pyautogui.moveTo(screen_width / 2, screen_height / 2)

    move_amount = 103.59

    pyautogui.moveRel(move_amount, 0, duration=0.1)

while True:
    if keyboard.is_pressed('F8'):
        turn_90_degrees()
        time.sleep(0.5)
    
    if keyboard.is_pressed('F7'):
        print("F7 pressed. Killing Script.")
        break

    time.sleep(0.01)
