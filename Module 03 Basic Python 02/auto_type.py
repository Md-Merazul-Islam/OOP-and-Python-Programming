import pyautogui
import time 
i =1
while True:
    time.sleep(0.05)
    pyautogui.write('i love you'+ str(i) ,interval=0.02)
    pyautogui.press('enter')
    i+=1