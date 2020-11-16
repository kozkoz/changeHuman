import tkinter as tk
from tkinter import *
# from tkinter import messagebox
import tkinter.messagebox as mb

import cv2
from PIL import Image, ImageTk
import numpy as np
import os
import time
import threading
import multiprocessing
import requests
import json
import base64

import wave  
import pygame.mixer as pyx
import sys
import random

HEIGHT = 800
WIDTH = 1600

finalImage = ["成功画像.png","失敗画像.png"]
musicSet = ["aaa.pm3","圧倒的敗北.mp3","変身前.mp3","正義は勝つ.pm3","top.mp3","今宵、君は月と踊る.mp3"]
movieSet = ["正義しか勝たん.mp4","圧倒的敗北.mp4","変身前.mp4","正義しか勝たん.mp4",]


root=tk.Tk()
root.title("camera")
root.geometry("640x480")
# root.resizable(width=False, height=False)
canvas=tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

pyx.init(frequency = 44100, size = -16, channels = 2, buffer = 4096) # 初期設定
sounds = pyx.Sound(musicSet[4]) # 再生ファイルを設定
sd_loop = -1 # 再生回数(-1:無限ループ)
channel = sounds.play(loops = sd_loop) # 音楽再生


image_path = "image.png"

img_top = Image.open("sippai.png")
tkimg = ImageTk.PhotoImage(img_top)


def video(num):
    print("videoStart")
    channel.pause() # 一時停止
    # frame1.destroy()
    # btn1.destroy()
    # pyx.init(frequency = 44100, size = -16, channels = 2, buffer = 4096) # 初期設定
    # sounds = pyx.Sound(musicSet[num]) # 再生ファイルを設定
    # sd_loop = 1 # 再生回数(-1:無限ループ)
    # ch = sounds.play(loops = sd_loop) # 音楽再生
    
    cnn=cv2.VideoCapture(movieSet[num])
    while(cnn.isOpened()):
        ret, frame = cnn.read()
        # root.attributes('-fullscreen', True)
        if ret==True:

        # 以下通常の動画表示
            
            cv2.imshow('movie',frame)  #反転frameを表示
            cv2.moveWindow('movie',0,0)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
        # ここまで

    cnn.release()
    # ch.pause()
    cv2.destroyAllWindows()


def capStart():

    print('camera-ON')
    try:
        global c, w, h, img
        c=cv2.VideoCapture(0)
        w, h= c.get(cv2.CAP_PROP_FRAME_WIDTH), c.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print('w:'+str(w)+'px+h:'+str(h)+'px')
        
    except:
        import sys
        print("error-----")
        print(sys.exec_info()[0])
        print(sys.exec_info()[1])
        '''終了時の処理はここでは省略します。
        c.release()
        cv2.destroyAllWindows()'''

def u():#
    global img
    ret, frame =c.read()
    frame = cv2.flip(frame, 1) # horizontal flip
    if ret:
        img=ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
        canvas.create_image(w/2,h/2,image=img)
    else:
        print("u-Fail")
    root.after(1,u)
    

def cameraPng():
    while True:
        if c.isOpened() is False:
            print("IO Error")
        else:
            ret, frame = c.read()
            if ( ret == True ):
                cv2.imwrite("image.png", frame)
            else:
                print("Read Error")
        image =  open(image_path, "rb").read()
        response_type = "json"
        request_body = {"response_type": response_type}
        url = "https://ai-api.userlocal.jp/human_pose"
        res = requests.post(url, data=request_body, files={"image_data": image})
        data = json.loads(res.content)
        image = base64.b64decode(data["image_data"])
        with open("test.png", "wb") as f:
            f.write(image)
        global leftShoulder,rightShoulder,leftElbow,rightElbow
        print(data["result"])
        print("person1" in data["result"])
        if "person1" in data["result"]:
            print("person1 is checked")
            if "LShoulder" in data["result"]["person1"]:
                leftShoulder = data["result"]["person1"]["LShoulder"]
                print(leftShoulder)
                if 450 < leftShoulder[0] < 700 and 100 < leftShoulder[1] < 500:
                    print("leftShoulder is true")
                else:
                    print("leftShoulder is false")
                if "LElbow" in data["result"]["person1"]:
                    leftElbow = data["result"]["person1"]["LElbow"]
                    print(leftElbow)
                    if 300 < leftElbow[0] < 700 and 100 < leftElbow[1] < 500:
                        print("leftElbow is true")
                    else:
                        print("leftElbow is false")
                else:
                    print("右手が映っていません")
                    leftElbow = [0,0]
            else:
                print("右腕が映っていません")
                leftShoulder = [0,0]
            if "RShoulder" in data["result"]["person1"]:
                rightShoulder = data["result"]["person1"]["RShoulder"]
                print(rightShoulder)
                if 200 < rightShoulder[0] < 600 and 100 < rightShoulder[1] < 500:
                    print("rightShoulder is true")
                else:
                    print("rightShoulder is false")
                if "RElbow" in data["result"]["person1"]:
                    rightElbow = data["result"]["person1"]["RElbow"]
                    if 100 < rightElbow[0] < 500 and 100 < rightElbow[1] < 500:
                        print("rightElbow is true")
                    else:
                        print("rightElbow is false")
                else:
                    print("左手が映っていません")
                    rightElbow = [0,0]
            else:
                print("左腕が映っていません")
                rightShoulder = [0,0]
        else:
            print("noHuman")
        # i = 0
        global changeToF,i
            # i = int(random.random()*10)
        i = 0
        if 350 < leftShoulder[0] < 700 and 100 < leftShoulder[1] < 500 and 300 < leftElbow[0] < 700 and 100 < leftElbow[1] < 500 and 200 < rightShoulder[0] < 600 and 100 < rightShoulder[1] < 500 and 100 < rightElbow[0] < 500 and 100 < rightElbow[1] < 500: 
            print("Aaa")
            # global changeToF,i
            # i = int(random.random()*10)
            # i = 0
            if i == 0:
                changeToF = 1
                print("変身失敗！")
                
            else:
                changeToF = 3
                print("変身成功！")
            break
            
            # print
            # ここに動画の処理を入れるよ！
        time.sleep(3)
    print("cameraPng Finish")
    video(changeToF)
    result()



def userlocal():
    channel.unpause()
    th1 = threading.Thread(target=u)
    th2 = threading.Thread(target=cameraPng)
    # th1.start()
    th2.start()
    print("th2Start")
    # th2.join()
    # c.release()
    print("AAA")


def again():
    win_sounds.stop()

    pyx.init(frequency = 44100, size = -16, channels = 2, buffer = 4096) # 初期設定
    sounds = pyx.Sound(musicSet[5]) # 再生ファイルを設定
    
    sd_loop = -1 # 再生回数(-1:無限ループ)

    channel = sounds.play(loops = sd_loop) # 音楽再生

    userlocal()
    
def owari():

    message = tk.messagebox.askyesno("", "本当に終了する？")
    if message == True:
        root.destroy()
    

def result():
    #成功時の音楽
    pyx.init(frequency = 44100, size = -16, channels = 2, buffer = 4096) # 初期設定
    global win_sounds
    win_sounds = pyx.Sound(musicSet[changeToF]) # 再生ファイルを設定
    channel.stop()
    sd_loop = 1 # 再生回数(-1:無限ループ)
    win_sound = win_sounds.play(loops = sd_loop) # 音楽再生

    # frame5 = tk.Frame(canvas, bg='white')
    # frame5.place(height=HEIGHT, width=WIDTH)


    label_back = tk.Label(canvas, image=tkimg, bg="white")
    label_back.pack(side ="left")
    # label_letter = tk.Label(text = "おめでとう！")
    # label_letter.pack(side="top")
    frame_finish = tk.Frame(label_back)
    frame_finish.place(x = 600, y = 440)

    frame_continue = tk.Frame(label_back)
    frame_continue.place(x = 600, y = 380)

    # label_finish = tk.Label(frame_finish, image=finish, bg="white")
    # label_finish.bind('<Button-1>', owari)
    # label_finish.pack()

    btn_continue = tk.Button(frame_continue, text='もう一回', font=40, command = lambda:[label_back.pack_forget(), again()], height = 1, width = 10)  
    btn_continue.pack()
    btn_finish = tk.Button(frame_finish, text='終了する', font=40,  command = owari, height = 1, width = 10)
    btn_finish.pack()







th1 = threading.Thread(target=cameraPng)
th2 = threading.Thread(target=u)
capStart()
th1.start()
th2.start()



# capStart()
# print(musicSet[2])
# u()
# print("userLocalStart")
# userlocal()
# print(changeToF)
# print(musicSet[0])
# video(changeToF)

root.mainloop()