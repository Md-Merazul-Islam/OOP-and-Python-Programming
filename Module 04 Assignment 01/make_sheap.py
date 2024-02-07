import pyautogui 

def shape(n):  
    for i in range(1, n + 1):
        ln = "#" * i
        print(ln)
        pyautogui.press('enter')
    

print("Enter the value of N : ")
n = int(input())
shape(n)


