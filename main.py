from os import getcwd

filepathall = getcwd()+"\\img"
geshi = open("传输格式.txt").read()

import pyautogui
#import urllib, requests
import pyperclip
import time
from pathlib import Path

print("正在加载学生名单……")
with open("学生名单.txt", encoding="utf-8") as f:
    namelist = set([x.replace("\n", "") for x in f.readlines()])
print("学生名单加载完成：", namelist)
lenth = len(namelist)
print("学生总人数：", lenth)
replier = dict()
for x in namelist:
    thisstudent = Path(filepathall+"\\"+x+"."+geshi)
    if thisstudent.is_file():
        replier[x] = (False, x+"."+geshi)
print("学生名单筛选完成：", replier.keys())


#screenSize = pyautogui.screenshot().size
def countdown(t):
    for i in range(t, 0, -1):
        print("请在", i, "秒内把微信窗口打开，并进入文件传输助手聊天框内")
        time.sleep(1)

countdown(5)

print("系统正在初始化，请不要移动鼠标或点击屏幕")
print("*******")
mes = pyautogui.locateOnScreen("message.png")
assert mes != None
print("chatbox located at:", mes)
upload = pyautogui.locateOnScreen("upload.png")
assert upload != None
print("upload buttom located at:", upload)
pyautogui.click(upload.left, upload.top)
time.sleep(1)
path = pyautogui.locateOnScreen("path.png")
assert path != None
print("file path located at:", path)
name = pyautogui.locateOnScreen("name.png")
assert name != None
print("file name located at:", name)
close = pyautogui.locateOnScreen("close.png")
assert close != None
print("close tab located at:", close)
pyautogui.click(close.left, close.top)
time.sleep(1)

print("*****")
print("开始自动回复……")

def copyMessage():
    pyautogui.click(mes.left+10, mes.top-40, clicks=2)
    pyautogui.hotkey('ctrl', 'c')
    return pyperclip.paste()

def locateNewMessage():
    dot = pyautogui.locateOnScreen("reddot.png")
    if dot == None:
        return None
    else:
        return dot.left, dot.top

def autoreply(dick):
    pyperclip.copy("无名氏")
    time.sleep(0.5)
    for downcount in range(lenth):
        time.sleep(0.2)
        p = pyperclip.paste()
        pyautogui.click(mes.left, mes.top + 100)
        pyautogui.hotkey("Down")
        message = copyMessage()
        if p != message:
            print(message)
            # pyautogui.click(p[0], p[1])
            if message in dick:
                sended = dick[message]
                if sended[0]:
                    send(sended[1])
                else:
                    image(filepathall, sended[1])
            for _ in range(downcount):
                time.sleep(0.5)
                pyautogui.click(mes.left, mes.top + 100)
                pyautogui.hotkey("Down")
        time.sleep(0.5)
        pyautogui.click(mes.left, mes.top + 100)
        pyautogui.hotkey("Down")

def autoreply0():
    pyautogui.click(mes.left, mes.top + 100)
    pyautogui.hotkey("Down")
    for i in range(lenth):
        send("""关于小助手的简介：
这是一个自动回复机器人，请大家在群里通知的日期之前添加小助手微信号
小助手开始使用之后，会先给各位发一下关于小助手的使用说明
使用方法：
老师在群里通知查看作业/课测批改之后，请各位私信小助手发送自己的全名
（要求无错字，与报名的时候一致）
小助手会尽量在一天之内把批改截图发给到您
请不要给小助手发除了您名字之外的信息
（这样会使您自己收不到批改）
请不要发别人的名字
（这样有可能会使别人收不到批改，小助手后台会有记录）
请不要给小助手发非文字内容
（这样有可能会导致小助手的死亡）""")
        time.sleep(0.5)
        for _ in range(i+1):
            pyautogui.click(mes.left, mes.top + 100)
            pyautogui.hotkey("Down")
            time.sleep(0.5)

def image(filepath, filename):
    pyautogui.click(upload.left, upload.top)
    time.sleep(1)
    pyperclip.copy(filepath)
    time.sleep(0.5)
    pyautogui.click(path.left-100, path.top)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.hotkey('Enter')
    time.sleep(1)
    pyperclip.copy(filename)
    time.sleep(0.5)
    pyautogui.click(name.left+20, name.top+30)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.hotkey('Enter')
    time.sleep(0.5)
    pyautogui.hotkey('Enter')

def send(reply):
    pyperclip.copy(reply)
    time.sleep(0.5)
    pyautogui.click(mes.left, mes.top+100)
    pyautogui.hotkey('ctrl', 'v')
    if reply == "啊":
        pyautogui.press('Down')
    pyautogui.press('Enter')

with open("初始化.txt") as f:
    if f.read() == "0":
        autoreply0()
    else:
        autoreply(replier)
