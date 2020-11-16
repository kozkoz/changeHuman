import sys
import wave  
import pygame.mixer as pyx  
import tkinter as tk
import cv2
from PIL import Image,ImageTk
import numpy as np
import os

root = tkinter.Tk()
root.title("test")
root.geometry("800x450")
sound_file = "shine3.mp3"
Label1 = tkinter.Label(root, text="1")  #文字ラベル設定
Label1.pack(side="top") # 場所を指定　（top, bottom, left, or right）




def test1():
    Label1.pack_forget()
    Label2 = tkinter.Label(root, text="2")  #文字ラベル設定
    Label2.pack(side="top") # 場所を指定　（top, bottom, left, or right)

    btn1 = tkinter.Button(root, text='わーい', command = lambda:[test2(), Label2.pack_forget()])
    btn1.place(x=140, y=170)


def test2():
    Label3 = tkinter.Label(root, text="3")  #文字ラベル設定
    Label3.pack(side="top") # 場所を指定　（top, bottom, left, or right）
    btn1 = tkinter.Button(root, text='わーい', command = lambda:[test3(), stop(), Label3.pack_forget()])
    btn1.place(x=140, y=170)
    

    

    pyx.init(frequency = 44100, size = -16, channels = 2, buffer = 4096) # 初期設定    
    sd_loop = -1 # 再生階数(-1:無限ループ)
    sounds = pyx.Sound(sound_file) # 再生ファイルを設定
    channel = sounds.play(loops = sd_loop) # 音楽再生

    def stop():
        channel.pause() # 一時停止


def test3():
    Label4 = tkinter.Label(root, text="4")  #文字ラベル設定
    Label4.pack(side="top") # 場所を指定　（top, bottom, left, or right）
    btn1 = tkinter.Button(root, text='わーい', command = lambda:[test4(), Label4.pack_forget()])
    btn1.place(x=140, y=170)

def test4():
    # Label4 = tkinter.Label(root, text="4")  #文字ラベル設定
    # Label4.place_forget()
    Label5 = tkinter.Label(root, text="5")  #文字ラベル設定
    Label5.pack(side="top") # 場所を指定　（top, bottom, left, or right）
    btn1 = tkinter.Button(root, text='わーい', command = lambda:[test5(), Label5.pack_forget()])
    btn1.place(x=140, y=170)


def test5():
    # Label5 = tkinter.Label(root, text="5")  #文字ラベル設定
    # Label5.place_forget()
    Label1 = tkinter.Label(root, text="1")  #文字ラベル設定
    Label1.pack(side="top") # 場所を指定　（top, bottom, left, or right）
    btn1 = tkinter.Button(root, text='わーい', command = lambda:[test1(), Label1.pack_forget()])
    btn1.place(x=140, y=170)





btn1 = tkinter.Button(root, text='わーい', command=test1)
btn1.place(x=140, y=170)







root.mainloop()