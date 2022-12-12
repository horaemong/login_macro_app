import cv2 as cv
from difflib import get_close_matches  # 현재는 사용치 않았지만 비스무리한 단어를 찾는데 굉장히 유용합니다. 
import subprocess 
import os
import time
import pyautogui  
import pyperclip 
import datetime
import os

def open_app():
    try:
        path = r"경로"
        subprocess.Popen(path)
    except:
        print("cannot open KakaoTalk")
        
def login_app(password):
    button_location = pyautogui.locateOnScreen('login_password.png', confidence=0.9)
    button_location_2 = pyautogui.locateOnScreen('login_login.png', confidence=0.9)
    if button_location is None and button_location_2 is None:
        print("패스워드 버튼 찾기 실패 ㅠㅠ")
    elif button_location is not None:
        button_point = pyautogui.center(button_location)
        pyautogui.click(button_point.x, button_point.y)
        pyautogui.write(password) 
        pyautogui.press('enter')
    elif button_location_2 is not None:
        button_point = pyautogui.center(button_location_2)
#     pyautogui.moveTo(button_point.x, button_point.y, duration=0)
#     pyautogui.move(0, -45, 0.5, pyautogui.easeInQuad)  # Move 45 pixels Up
        pyautogui.doubleClick(button_point.x, button_point.y-45)
        pyautogui.write(password)
        pyautogui.press('enter')
   
   

open_app()

#창이 열렸는지 확인
win = ''
while not win:
    try:
        win = pyautogui.getWindowsWithTitle('카카오톡')[0]
    except:
        print("카카오톡 창을 찾을 수 없습니다.")
        time.sleep(1)

login_app('비밀번호')


#pyinstaller app.py