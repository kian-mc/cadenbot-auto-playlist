import pyautogui, time, keyboard


while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('1'):  # if key '1' is pressed
            time.sleep(1)
            pyautogui.press('backspace')
            pyautogui.typewrite('You Selected Radio Los Santos!')
            time.sleep(2)
            pyautogui.press('backspace', presses=30)
            f = open('RadioLosSantos.txt', 'r')
            for word in f:
                 time.sleep(2)
                 pyautogui.typewrite("-p ")
                 pyautogui.typewrite(word)
                 pyautogui.press("enter")
            pyautogui.typewrite('Process finished with exit code 0')
            pyautogui.press("enter")-p Kendrick Lamar - Swimming Pools (Drank)
            
            -p 

            break  # finishing the loop
        if keyboard.is_pressed('2'):
             time.sleep(1)
             pyautogui.press('backspace')
             pyautogui.typewrite('You selected Los santos rock radio!')
             time.sleep(2)
             pyautogui.press('backspace', presses=35)
             f = open('ClassicRock.txt', 'r')
             for word in f:
                 time.sleep(2)
                 pyautogui.typewrite("-p ")
                 pyautogui.typewrite(word)
                 pyautogui.press("enter")
             pyautogui.typewrite('Process finished with exit code 0')
             pyautogui.press("enter")

             break  # finishing the loop
        if keyboard.is_pressed('s'): # -stop
             time.sleep(1)
             pyautogui.press('backspace')
             pyautogui.typewrite('-p stop')
             pyautogui.press('enter')

             break  # finishing the loop

        if keyboard.is_pressed('?'): # -np
             time.sleep(1)
             pyautogui.press('backspace')
             pyautogui.typewrite('-np')
             pyautogui.press('enter')

             break  # finishing the loop

        if keyboard.is_pressed('k'): # -skip
             time.sleep(1)
             pyautogui.press('backspace')
             pyautogui.typewrite('-skip')
             pyautogui.press('enter')

             break  # finishing the loop
        if keyboard.is_pressed('r'): # -repeat
             time.sleep(1)
             pyautogui.press('backspace')
             pyautogui.typewrite('-repeat')
             pyautogui.press('enter')

             break  # finishing the loop

        if keyboard.is_pressed('q'): # -queue
             time.sleep(1)
             pyautogui.press('backspace')
             pyautogui.typewrite('-queue')
             pyautogui.press('enter')

             break  # finishing the loop
    except:
        break  # if user pressed a key ot
