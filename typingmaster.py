import threading
import time
from copy import copy
from tkinter import *
from tkinter import messagebox
from threading import *
from pynput.keyboard import *
root = Tk()
text = ""
start_time = 0
ch = 0
jk = 0
#defining all variables

paragraphs = "Over the years many adventurers have tried to find this precious body. But these waters swarm with vicious creatures: tigersharks, hammerheads, ghost sharks, and worse! Now, it's your turn to dive"
fetched_text = ""
acc = "0"
net_wpm = '0'
c_error =  0
datalist = [] #containing the recommended words
numles = 0
error = ""

#defining all functions here
#Creating two threads for running three functions in parallal: fetching_text continously, press function , basic start
def parallel2():
    if __name__ == '__main__':
        t3 = threading.Thread(target=bastart)
        t3.start()
        t4 = threading.Thread(target=fetch_text)
        t4.start()
def parallel():
  if __name__ == '__main__':
      t1 = threading.Thread(target=parallel2)
      t2 = threading.Thread(target=startwrap)
      t1.start()
      t2.start()
def startwrap():
    global paragraphs
    start(paragraphs)
def start(lesson):
    global i, error, text, c_error

    text = lesson
    error = ""

    with Listener(on_press=press) as listener:
        listener.join()
def press(key):
    global error, ch, fetched_text, text , jk, c_error
    if key == Key.space and text[jk] == " ":
        fetched_text += " "
        jk = jk + 1
        ch = ch + 1
    elif text[jk] == "\n":
        jk += 1
    elif key == KeyCode.from_char(text[jk]):
        fetched_text += text[jk]
        jk = jk + 1
        return

    elif key != Key.shift and key != Key.shift_r and key != Key.caps_lock and key != Key.esc and key != Key.down and key != Key.up:
        print('errr', key)
        c_error += 1
        error = error + text[jk]
    if key == Key.esc or jk == len(text):
        return False
#this function makes random wors for user to practice with depending on mistakes
def randomstr(x):
    reqstr = ""
    stlist=[]
    alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    import random
    for i in range(4):
        elem=random.randint(0,25)
        strelem=alpha[elem]
        stlist.append(strelem)

    chrpos = random.randint(0, 4)
    stlist.insert(chrpos,x)
    for i in range(5):
        chr = stlist[i]
        reqstr +=chr
    return reqstr
#creating exact paragraphs that we need
def rohail(check):
    check = check.lower()
    characters = "abcdefghijklmnopqrstuvwxyz"
    count = []
    list_keys=[]
    list_occurence=[]
    for character in characters:
      count = check.count(character)
      if count > 0:
        list_keys.append(character)
        list_occurence.append(count)
    x=list_occurence.copy()
    x.sort()
    length=len(x)
    if len(x)>1 or len(x)== 1:
        most=x[length-1]
        indx1 = list_occurence.index(most)
        firstmostrepeated = list_keys[indx1]
        for i in range(15):
            y = randomstr(firstmostrepeated)
            datalist.append(y)
    if len(x)>2 or len(x)== 2:
        secondmostwrong=x[length-2]
        indx2 = list_occurence.index(secondmostwrong)
        secondmostrepeated = list_keys[indx2]
        for i in range(10):
            y = randomstr(secondmostrepeated)
            datalist.append(y)
    if len(x)>3 or len(x)== 3:
        thirdmostwrong=x[length-3]
        indx3 = list_occurence.index(thirdmostwrong)
        thirdmostrepeated = list_keys[indx3]
        for i in range(7):
            y = randomstr(thirdmostrepeated)
            datalist.append(y)
    return(datalist)
#this function is desinged to fetch the text typed by the user
def gettext():
    y=itextlabel.get("1.0",END)
    return y
 # This function is binding function highlighting the key that is pressed
def bindef(labl):
    labl.config(bg="yellow")
    labl.after(100, lambda: labl.config(bg="black"))
 #basic starting function when user presses start button
def bastart():
    global start_time, error, fetched_text, c_error
    menubar.entryconfig("Levels", state="disable")
    fetched_text = ""
    acclabel.config(text="Accuracy = 0 %")
    errlabel.config(text="Error = 0")
    wpmlabel.config(text="WPM = 0")
    error = ""
    c_error = 0
    start_time = time.time()
    itextlabel.config(state="normal")
    itextlabel.delete("1.0", END)
    endbtn.config(state="normal")
    startbtn.config(state="disable")
    recmbtn.config(state="disable")
# when user will click stop button this function shall trigger the claculations
def forcestop():
    global numles, end_time, net_wpm, acc, c_error, error, jk
    jk = 0
    c_error = int(c_error)
    print("error when stop is clicked",error)

    end_time = time.time()
    _time = end_time - start_time
    _time = _time / 60
    typed_text = gettext()
    lenchar = len(typed_text)
    gross_wpm = round((lenchar / 5) / _time)
    net_wpm = round(gross_wpm - (c_error/5) / _time)
    acc = round((net_wpm / gross_wpm) * 100)
    if acc<0 :
        acc=0
    if c_error < 0 :
        c_error = 0
    if net_wpm < 0:
        net_wpm = 0
    acc = str(acc)
    net_wpm = str(net_wpm)
    menubar.entryconfig("Levels", state="disable")
    errlabel.config(text="Error=" + str(c_error))
    acclabel.config(text="Accuracy="+acc+"%")
    wpmlabel.config(text="WPM="+net_wpm)
    recmbtn.config(state="normal")
    startbtn.config(state="disable")
    endbtn.config(state="disable")
    #itextlabel.config(state="disable")
def recom():
    global error, text, fetched_text, jk, c_error, start_time
    if error == "":
        messagebox.showinfo("Information", "You have not made any mistakes, there are no recommended lessons")
        root.destroy()
    else:
        messagebox.showinfo("Information","You will get recommended Lessons based on the mistakes you have made in previous lesson")
        y = rohail(error)
        req_txt = ""
        fetched_text = ""
        jk = 0
        for i in y:
            if i == len(y)-1:
                req_txt += i
            req_txt += i+" "
        print(req_txt)

        text = req_txt
        dtextlabel.config(text=req_txt)
        itextlabel.delete("1.0", END)
        acclabel.config(text="Accuracy = 0 %")
        errlabel.config(text="Error = 0")
        wpmlabel.config(text="WPM = 0")
        endbtn.config(state="normal")
        startbtn.config(state="disable")
        recmbtn.config(state="disable")
        start_time = time.time()
        error = ""
        c_error = 0
        return y
# following functions help to have different levels
def testp():
    global paragraphs, text, jk
    x = open("Data/Typing Test.txt", "r")
    paragraphs = x.read()
    dtextlabel.config(text=paragraphs)
    itextlabel.delete("1.0", END)
    itextlabel.config(state="disable")
    jk = 0
    text = paragraphs

def level1():
    global paragraphs, fetched_text , jk, error, c_error, text
    error = ""
    c_error = 0
    x = open("Data/Text1.txt", "r")
    paragraphs=x.read()
    dtextlabel.config(text=paragraphs)
    itextlabel.config(state="disable")
    itextlabel.delete("1.0", END)
    fetched_text = ""
    jk = 0
    text = paragraphs

def level2():
    global paragraphs, fetched_text, text , jk, error, c_error
    error = ""
    c_error = 0
    x = open("Data/Text2.txt", "r")
    paragraphs = x.read()
    dtextlabel.config(text=paragraphs)
    itextlabel.config(state="disable")
    itextlabel.delete("1.0", END)
    fetched_text = ""
    jk = 0
    text = paragraphs

def level3():
    global paragraphs,fetched_text, text , jk, error, c_error
    error = ""
    c_error = 0
    x = open("Data/Text3.txt", "r")
    paragraphs = x.read()
    dtextlabel.config(text=paragraphs)
    itextlabel.config(state="disable")
    itextlabel.delete("1.0", END)
    fetched_text = ""
    jk = 0
    text = paragraphs
    print("Error after level 3 is selected",error)

def level4():
    global paragraphs, fetched_text, text , jk, error, c_error
    error = ""
    c_error = 0
    x = open("Data/Text4.txt", "r")
    paragraphs = x.read()
    dtextlabel.config(text=paragraphs)
    itextlabel.config(state="disable")
    itextlabel.delete("1.0", END)
    fetched_text = ""
    jk = 0
    text = paragraphs

def level5():
    global paragraphs, fetched_text, text , jk, error, c_error
    error = ""
    c_error = 0
    x = open("Data/Text5.txt", "r")
    paragraphs = x.read()
    dtextlabel.config(text=paragraphs)
    itextlabel.config(state="disable")
    fetched_text = ""
    jk = 0
    itextlabel.delete("1.0", END)
    text = paragraphs
#continously updating the text box and error count and fetching text
def update_textbox(text1):
    global c_error
    itextlabel.delete("1.0",END)
    itextlabel.insert("1.0",text1)
    errlabel.config(text="Errors = "+str(c_error))
def fetch_text():
    while True:
        upd_btn.invoke()
        time.sleep(0.00001)


#root.attributes("-fullscreen",True)
root.config(bg="black")
root.title("TypFast")
menubar = Menu(root)

m1=Menu(menubar,tearoff=0)
m1.add_command(label="Typing test", command= testp)
m1.add_command(label="Level 1", command= level1)
m1.add_command(label="Level 2", command= level2)
m1.add_command(label="Level 3", command= level3)
m1.add_command(label="Level 4", command= level4)
m1.add_command(label="Level 5", command= level5)


root.config(menu=menubar)
menubar.add_cascade(label="Levels",menu=m1)


headframe=Frame(root)
headframe.config(bg="black")
headlabel=Label(text="TYPFAST",font="Algerian 20 underline", height=2, bg='black', fg="yellow")
headlabel.grid()
headframe.grid(row=0,column=0)

dtextframe=Frame(root)
dtextlabel=Label(text=paragraphs,justify="left", wraplength=1020,font="newtimesroman 14 underline ",bg= 'black', fg="white")
dtextlabel.grid()
dtextframe.grid(row=1,column=0)

uinputframe=Frame(root)
itextlabel=Text(width=93,height=7,state="disable",font="newtimesroman 14 ",bg= 'black', fg="beige")
itextlabel.grid()
uinputframe.grid(row=2,column=0)

keyboardframe=Frame(root)
keyboardframe.config(bg="black")
#defining four frames for each row.
numframe=Frame(keyboardframe)
numframe.config(bg="black")
#labels for all numbers
la_1=Label(numframe,text="1",width=5,height=2, font="12,arial,bold",background="black",foreground="white",relief = GROOVE)
la_1.grid(row=0,column=0)
la_2=Label(numframe,text="2",width=5,height=2, font="12,arial,bold",background="black",foreground="white",relief = GROOVE)
la_2.grid(row=0,column=1)
la_3=Label(numframe,text="3",width=5,height=2, font="12,arial,bold",background="black",foreground="white",relief = GROOVE)
la_3.grid(row=0,column=2)
la_4=Label(numframe,text="4",width=5,height=2, font="12,arial,bold", background="black",foreground="white",relief = GROOVE)
la_4.grid(row=0,column=3)
la_5=Label(numframe,text="5",width=5,height=2,font="12,arial,bold", background="black",foreground="white",relief = GROOVE)
la_5.grid(row=0,column=4)
la_6=Label(numframe,text="6",width=5,height=2,font="12,arial,bold", background="black",foreground="white",relief = GROOVE)
la_6.grid(row=0,column=5)
la_7=Label(numframe,text="7",width=5,height=2, font="12,arial,bold", background="black",foreground="white",relief = GROOVE)
la_7.grid(row=0,column=6)
la_8=Label(numframe,text="8",width=5,height=2, font="12,arial,bold", background="black",foreground="white",relief = GROOVE)
la_8.grid(row=0,column=7)
la_9=Label(numframe,text="9",width=5,height=2, font="12,arial,bold", background="black",foreground="white",relief = GROOVE)
la_9.grid(row=0,column=8)
la_0=Label(numframe,text="0",width=5,height=2, font="12,arial,bold", background="black",foreground="white",relief = GROOVE)
la_0.grid(row=0,column=9)

numframe.grid(row=0,column=0,pady=5)

topkeyframe = Frame(keyboardframe,pady=5)
topkeyframe.config(bg="black")
#labels for all topkeys
la_q = Label(topkeyframe,text="Q",  bg="black", fg="white",relief=GROOVE, font="12,arial,bold",width=4,height=2)
la_q.grid(row=0,column=0)
la_w = Label(topkeyframe,text="W",  bg="black", fg="white",relief=GROOVE, font="12,arial,bold",width=4,height=2)
la_w.grid(row=0,column=1)
la_e = Label(topkeyframe,text="E",  bg="black", fg="white",relief=GROOVE, font="12,arial,bold",width=4,height=2)
la_e.grid(row=0,column=2)
la_r = Label(topkeyframe,text="R",  bg="black", fg="white",relief=GROOVE, font="12,arial,bold",width=4,height=2)
la_r.grid(row=0,column=3)
la_t = Label(topkeyframe,text="T",  bg="black", fg="white",relief=GROOVE, font="12,arial,bold",width=4,height=2)
la_t.grid(row=0,column=4)
la_y = Label(topkeyframe,text="Y",  bg="black", fg="white",relief=GROOVE, font="12,arial,bold",width=4,height=2)
la_y.grid(row=0,column=5)
la_u = Label(topkeyframe,text="U",  bg="black", fg="white",relief=GROOVE, font="12,arial,bold",width=4,height=2)
la_u.grid(row=0,column=6)
la_i = Label(topkeyframe,text="I",  bg="black", fg="white",relief=GROOVE, font="12,arial,bold",width=4,height=2)
la_i.grid(row=0,column=7)
la_o = Label(topkeyframe,text="O",  bg="black", fg="white",relief=GROOVE, font="12,arial,bold",width=4,height=2)
la_o.grid(row=0,column=8)
la_p = Label(topkeyframe,text="P",  bg="black", fg="white",relief=GROOVE, font="12,arial,bold",width=4,height=2)
la_p.grid(row=0,column=9)
topkeyframe.grid(row=1,column=0)

bottomkeyframe=Frame(keyboardframe,pady=5)
bottomkeyframe.config(bg="black")
#labels for bottom row of keys
la_a=Label(bottomkeyframe,text="A",width=4,height=2,font="12,arial,bold",bg="black",fg="white",relief=GROOVE)
la_a.grid(row=0,column=0)
la_s=Label(bottomkeyframe,text="S",width=4,height=2,font="12,arial,bold",bg="black",fg="white",relief=GROOVE)
la_s.grid(row=0,column=1)
la_d=Label(bottomkeyframe,text="D",width=4,height=2,font="12,arial,bold",bg="black",fg="white",relief=GROOVE)
la_d.grid(row=0,column=2)
la_f=Label(bottomkeyframe,text="F",width=4,height=2,font="12,arial,bold",bg="black",fg="white",relief=GROOVE)
la_f.grid(row=0,column=3)
la_g=Label(bottomkeyframe,text="G",width=4,height=2,font="12,arial,bold",bg="black",fg="white",relief=GROOVE)
la_g.grid(row=0,column=4)
la_h=Label(bottomkeyframe,text="H",width=4,height=2,font="12,arial,bold",bg="black",fg="white",relief=GROOVE)
la_h.grid(row=0,column=5)
la_j=Label(bottomkeyframe,text="J",width=4,height=2,font="12,arial,bold",bg="black",fg="white",relief=GROOVE)
la_j.grid(row=0,column=6)
la_k=Label(bottomkeyframe,text="K",width=4,height=2,font="12,arial,bold",bg="black",fg="white",relief=GROOVE)
la_k.grid(row=0,column=7)
la_l=Label(bottomkeyframe,text="L",width=4,height=2,font="12,arial,bold",bg="black",fg="white",relief=GROOVE)
la_l.grid(row=0,column=8)

bottomkeyframe.grid(row=2,column=0,pady=5)

floorkeyframe=Frame(keyboardframe)
floorkeyframe.config(bg="black")
#defining labels for last row.
la_z=Label(floorkeyframe,text="Z",width=4,height=2,font="12,arial,bold",bg="black",fg="white",relief=GROOVE)
la_z.grid(row=0,column=0)
la_x=Label(floorkeyframe,text="X",width=4,height=2,font="12,arial,bold",bg="black",fg="white",relief=GROOVE)
la_x.grid(row=0,column=1)
la_c=Label(floorkeyframe,text="C",width=4,height=2,font="12,arial,bold",bg="black",fg="white",relief=GROOVE)
la_c.grid(row=0,column=2)
la_v=Label(floorkeyframe,text="V",width=4,height=2,font="12,arial,bold",bg="black",fg="white",relief=GROOVE)
la_v.grid(row=0,column=3)
la_b=Label(floorkeyframe,text="B",width=4,height=2,font="12,arial,bold",bg="black",fg="white",relief=GROOVE)
la_b.grid(row=0,column=4)
la_n=Label(floorkeyframe,text="N",width=4,height=2,font="12,arial,bold",bg="black",fg="white",relief=GROOVE)
la_n.grid(row=0,column=5)
la_m=Label(floorkeyframe,text="M",width=4,height=2,font="12,arial,bold",bg="black",fg="white",relief=GROOVE)
la_m.grid(row=0,column=6)

floorkeyframe.grid(row=3,column=0,pady=2)

spaceframe=Frame(keyboardframe)
spaceframe.config(bg="black")
spacewidget=Label(spaceframe,text="",width=24,height=2,fg="white",relief=GROOVE, bg="black",border=4)
spacewidget.grid(row=0,column=0)
spaceframe.grid(row=4,column=0)

keyboardframe.grid(row=3,column=0,pady=5)

menuframe=Frame(root, padx=28)
menuframe.config(bg="black")
upd_btn=Button(menuframe,text="",bg="white", command = lambda : update_textbox(fetched_text))
#upd_btn.grid(row=6,column=0)
wpmframe=Frame(menuframe)
wpmframe.config(bg="black")
wpmlabel=Label(wpmframe,text="WPM = "+net_wpm,bg="black",relief = GROOVE, height = 2,fg="yellow",font="Algerian 13 bold",width=20)
wpmlabel.grid()
wpmframe.grid(row=0,column=0)

accframe=Frame(menuframe)
accframe.config(bg="black")
acclabel=Label(accframe,text="Accuracy = "+acc+" %",bg="black",relief = GROOVE, height = 2,fg="yellow",font="Algerian 13 bold",width=20)
acclabel.grid()
accframe.grid(row=1,column=0,pady=6)

errframe=Frame(menuframe)
errframe.config(bg="black")
errlabel=Label(errframe, text="Error = "+"0",bg="black",relief = GROOVE, height = 2,fg="yellow",font="Algerian 13 bold",width=20)
errlabel.grid()

errframe.grid(row=2, column=0)

startframe=Frame(menuframe,pady=6)
startframe.config(bg="black")
startbtn=Button(startframe,text="Start",font="Algerian 13 bold",bg="black",fg="yellow",width=20,state="normal", command = parallel)
startbtn.grid()
startframe.grid(row=3, column=0)
endframe=Frame(menuframe, pady=6)
endframe.config(bg="black")
endbtn=Button(endframe,text="End",bg="black",fg="yellow",font="Algerian 13 bold",width=20,state = "disable", command = forcestop)
endbtn.grid()
endframe.grid(row=4,column=0)
recomframe=Frame(menuframe, pady=6)
recomframe.config(bg="black")
recmbtn=Button(recomframe, text="Recommended",bg="black",fg="yellow",font="Algerian 13 bold",width=20, state = "disable", command = recom)
recmbtn.grid()
recomframe.grid(row=5, column=0)
menuframe.grid(row=3, column=1)

#binding all keyborad keys with their actual presses

numberli = ["1","2","3","4","5","6","7","8","9","0"]
salphali = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
calphali = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V", "B", "N", "M"]

num_li_tr = [la_1,la_2,la_3,la_4,la_5,la_6,la_7,la_8,la_9,la_0 ]
alp_li_tr= [la_q,la_w,la_e,la_r,la_t,la_y,la_u,la_i,la_o,la_p,la_a,la_s,la_d,la_f,la_g,la_h,la_j,la_k,la_l,la_z,la_x,la_c,la_v,la_b,la_n,la_m]

for i in range(len(numberli)):
    root.bind(numberli[i],lambda event, label=num_li_tr[i]:bindef(label))

for i in range(len(salphali)):
    root.bind(salphali[i],lambda event, label=alp_li_tr[i]:bindef(label))

for i in range(len(calphali)):
    root.bind(calphali[i], lambda event, label=alp_li_tr[i]:bindef(label))

root.bind("<space>", lambda event, label=spacewidget:bindef(label))
root.mainloop()