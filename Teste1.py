# pip install pyautogui
import pyautogui as pyag
import time
pesq = ""
print("Digite o que você quer pesquisar:")
pyag.moveTo(200,600,0.2)
pyag.click()
pesq = input()
pyag.moveTo(20,750,0.3)
pyag.click()
pyag.moveTo(200,75,0.3)
pyag.click()
pyag.write("Chrome",0.1)
time.sleep(0.5)
pyag.keyDown("Enter")
time.sleep(0.7)
pyag.write(pesq, 0.1)
pyag.keyDown('Enter')
time.sleep(2)
pyag.hotkey('ctrl', 'w')
pyag.locateOnScreen()