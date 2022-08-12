# インポート
import tkinter
import audio

# Tkinter関係の処理
root = tkinter.Tk()
root.title("タイマー/Timer") # title
root.minsize(370, 400) # サイズ
root.resizable(height=False, width=False) # サイズ変更を無効
root.option_add("*font", ["MS Pゴシック", 22]) # フォント

# 変数作成
detection = 0 # 現在何をしているのかを知るための変数 0=何もしていない 1=タイマー 2=ストップウォッチ
imput = int(0)
inputSeconds = int(0)
inputSeconds2 = int(0)
inputMinutes = int(0)
inputMinutes2 = int(0)
inputHours = int(0)
inputHours2 = int(0)
dp = 0
h = 0
m = 0
s = 0
temp = 0
audiotemp = 0

# 関数(処理関連)

def display():
    global h ,m, s
    if len(str(h)) == 1:
        disph = f"0{h}"
    else:
        disph = h

    if len(str(m)) == 1:
        dispm = f"0{m}"
    else:
        dispm = m

    if len(str(s)) == 1:
        disps = f"0{s}"
    else:
        disps = s

    label["text"] = f"{str(disph)}:{str(dispm)}:{str(disps)}"

def timer():
    global detection, h ,m, s, dp

    h = int(h)
    m = int(m)
    s = int(s)

    if detection == 1:
        if s != 0:
            s = s - 1
        else:
            if m != 0:
                m = m - 1
                s = 59
            else:
                if h != 0:
                    h = h - 1
                    m = 59
                    s = 59
        if h == 0 and m == 0 and s == 0:
            detection = 0
            stopreset()
            Canvas["bg"] = "red"
            label["bg"] = "red"
            TkeyLabel["bg"] = "red"
            TkeyLabel["text"] = "終了"
            root.attributes("-topmost", True)
            audio.start()
        else:
            pass
        display()
        root.after(1000, timer)
    else:
        pass

def stopwatch():
    global detection, h, m, s

    h = int(h)
    m = int(m)
    s = int(s)

    if detection == 2:
        if s == 59:
            if m == 59:
                h = h + 1
                m = 0
            else:
                m = m + 1
                s = 0    
        else:
            s = s + 1
        display()
        root.after(1000, stopwatch)
    else:
        pass

# 関数(テンキー関連)
def caution():
    global temp

    if temp == 0:
        TkeyLabel["text"] = "動作している途中はテンキー操作ができません。"
        temp = 1
        root.after(3000, caution)
    else:
        TkeyLabel["text"] = ""

def advance():
    global detection, h ,m, s, inputHours, inputHours2, inputMinutes, inputMinutes2, inputSeconds, inputSeconds2, input, dp, temp

    if detection == 0:
        inputHours = inputHours2
        inputHours2 = inputMinutes
        inputMinutes = inputMinutes2
        inputMinutes2 = inputSeconds
        inputSeconds = inputSeconds2
        inputSeconds2 = imput

        h = 10*inputHours + inputHours2
        m = 10*inputMinutes + inputMinutes2
        s = 10*inputSeconds + inputSeconds2

        display()
        dp = 1
    else:
        caution()
        temp = 0

def zero():
    global imput
    imput = 0
    advance()

def one():
    global imput
    imput = 1
    advance()

def two():
    global imput
    imput = 2
    advance()

def three():
    global imput
    imput = 3
    advance()

def four():
    global imput
    imput = 4
    advance()

def five():
    global imput
    imput = 5
    advance()

def six():
    global imput
    imput = 6
    advance()

def seven():
    global imput
    imput = 7
    advance()

def eight():
    global imput
    imput = 8
    advance()

def nine():
    global imput
    imput = 9
    advance()

def start():
    global h, m, s, detection, dp
    
    if dp == 0:
        # ストップウォッチ
        detection = 2
        stopwatch()
    else:
        # タイマーの処理
        detection = 1
        timer()

def stopreset():
    global detection, h, m, s, inputHours , inputHours2, inputMinutes, inputMinutes2, inputSeconds, inputSeconds2, dp, audiotemp
    if detection == 1 or detection == 2:
        detection = 0
    else:
        h = 0
        m = 0
        s = 0
        inputSeconds = int(0)
        inputSeconds2 = int(0)
        inputMinutes = int(0)
        inputMinutes2 = int(0)
        inputHours = int(0)
        inputHours2 = int(0)
        dp = 0
        Canvas["bg"] = "white"
        label["bg"] = "white"
        TkeyLabel["bg"] = "white"
        TkeyLabel["text"] = ""

        display()
        root.attributes("-topmost", False)
        audio.stop()



# 背景色変更
Canvas = tkinter.Canvas(bg="white", width=405,height=485)
Canvas.place(x=-5, y=-5)

# 残り時間表示ラベル
label = tkinter.Label(text="00:00:00", font=("MS Pゴシック", "50", "bold"), bg="white")
label.place(x=50, y=0)

# テンキー
buttonstart = tkinter.Button(text="Start", width=6, command=start) # スタートボタン
buttonstart.place(x=10, y=310)

buttonstop = tkinter.Button(text="S/R", width=6, command=stopreset) # S/R
buttonstop.place(x=250, y=310)

button0 = tkinter.Button(text="0", width=6, command=zero) # 0
button0.place(x=130, y=310)

button1 = tkinter.Button(text="1", width=6, command=one) # 1
button1.place(x=10, y=240)

button2 = tkinter.Button(text="2", width=6, command=two) # 2
button2.place(x=130, y=240)

button3 = tkinter.Button(text="3", width=6, command=three) # 3
button3.place(x=250, y=240)

button4 = tkinter.Button(text="4", width=6, command=four) # 4
button4.place(x=10, y=170)

button5 = tkinter.Button(text="5", width=6, command=five) # 5
button5.place(x=130, y=170)

button6 = tkinter.Button(text="6", width=6, command=six) # 6
button6.place(x=250, y=170)

button7 = tkinter.Button(text="7", width=6, command=seven) # 7
button7.place(x=10, y=100)

button8 = tkinter.Button(text="8", width=6, command=eight) # 8
button8.place(x=130, y=100)

button9 = tkinter.Button(text="9", width=6, command=nine)
button9.place(x=250, y=100)

# 注意書き
TkeyLabel = tkinter.Label(text="", font=("MS Pゴシック", "10", "bold"), bg="white")
TkeyLabel.place(x=10, y=365)

# mainloop
root.mainloop()
