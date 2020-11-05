import sys
import tkinter

root = tkinter.Tk()
root.title(u"test")
root.geometry("800x450")




def test1():
    Label1.place_forget()
    Label2 = tkinter.Label(root, text="2")  #文字ラベル設定
    Label2.pack(side="top") # 場所を指定　（top, bottom, left, or right)
    btn1 = tkinter.Button(root, text='わーい', command=test2)
    btn1.place(x=140, y=170)


def test2():
    Label2 = tkinter.Label(root, text="2")  #文字ラベル設定
    Label2.place_forget()
    Label3 = tkinter.Label(root, text="3")  #文字ラベル設定
    Label3.pack(side="top") # 場所を指定　（top, bottom, left, or right）
    btn1 = tkinter.Button(root, text='わーい', command=test3)
    btn1.place(x=140, y=170)

def test3():
    Label3 = tkinter.Label(root, text="3")  #文字ラベル設定
    Label3.place_forget()
    Label4 = tkinter.Label(root, text="4")  #文字ラベル設定
    Label4.pack(side="top") # 場所を指定　（top, bottom, left, or right）
    btn1 = tkinter.Button(root, text='わーい', command=test4)
    btn1.place(x=140, y=170)

def test4():
    Label4 = tkinter.Label(root, text="4")  #文字ラベル設定
    Label4.place_forget()
    Label5 = tkinter.Label(root, text="5")  #文字ラベル設定
    Label5.pack(side="top") # 場所を指定　（top, bottom, left, or right）
    btn1 = tkinter.Button(root, text='わーい', command=test5)
    btn1.place(x=140, y=170)


def test5():
    Label5 = tkinter.Label(root, text="5")  #文字ラベル設定
    Label5.place_forget()
    Label1 = tkinter.Label(root, text="1")  #文字ラベル設定
    Label1.pack(side="top") # 場所を指定　（top, bottom, left, or right）
    btn1 = tkinter.Button(root, text='わーい', command=test1)
    btn1.place(x=140, y=170)





# def testChange():
btn1 = tkinter.Button(root, text='わーい', command=test1)
btn1.place(x=140, y=170)
    #  print(n)
    #  n = 1
    # elif n== 1:
    #  button = test2
    #  print(n)
    #  n = 3
    # else: 
    #  button = test3
    #  print(n)


Label1 = tkinter.Label(root, text="1")  #文字ラベル設定
Label1.pack(side="top") # 場所を指定　（top, bottom, left, or right）

# btn1 = tkinter.Button(root, text='わーい', command=testChange)
# btn1.place(x=140, y=170)
# btn2 = tkinter.Button(root, text='計算', command=test2)
# btn2.place(x=140, y=170)

Label1.place(x=130, y=200)


root.mainloop()