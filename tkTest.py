import tkinter

# 画面作成
tki = tkinter.Tk()
tki.geometry('300x200') # 画面サイズの設定
tki.title('ボタンのサンプル') # 画面タイトルの設定

# ボタンの作成
btn = tkinter.Button(tki, text='ボタン') # ボタンの設定(text=ボタンに表示するテキスト)
btn.place(x=130, y=80) #ボタンを配置する位置の設定

# 画面をそのまま表示
tki.mainloop()