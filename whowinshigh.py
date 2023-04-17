#WhoScoreHigh_game
#python_project_1
#Muhammed_zabiullah_khan
#5_square

#declaring_modules
import math
import tkinter.messagebox as box
from tkinter import *
import random
import mysql.connector as con

#assigning module to root object variable & setting the window geometry
window=Tk()
window.title('Mining Game')
window.geometry('500x500')


global score_collector
#indexing_for_score_colours
colours=['blue','purple','red','maroon','green']
x=0
def score():
    global x
    Label(window,text=score_collector,fg=colours[x],bg='grey',font='none 20 bold').grid(row=4,column=2,columnspan=1)
    if x>=len(colours)-1:
        x=0
        x+=1
#function_to_disable_buttons_if_game_is_over_or_won
def disable():
    csr="button_"
    for i in range(1,17):
        eval(csr+str(i)).config(state="disabled")

    def save():
        global na
        na=namez.get()
        def sql_connect():
            global db
            db = con.connect(host='localhost',user='root',password='qwerty')
        def create_database():
            mycursor=db.cursor()
            mycursor.execute('create database if not exists game')
            db.commit()
        def use_database():
            mycursor=db.cursor()
            mycursor.execute('use game')
            db.commit()
            
        def create_table():
            mycursor=db.cursor()
            mycursor.execute('create table if not exists profiles(name varchar(20) default "player",score int)')
            db.commit()
        def insert_data():
            mycursor=db.cursor()
            mycursor.execute('insert into profiles(name,score) value("{}","{}")'.format(na,score_collector))
            db.commit()

        def main():
            sql_connect()
            create_database()
            use_database()
            create_table()
            insert_data()

        main()
        box.showinfo('saved','successfully saved')
            

    window_1=Tk()
    Label(window_1,text='Enter Your Name',font='none 15 bold').pack()
    namez=Entry(window_1,font='none 12 bold')
    namez.pack()
    btq=Button(window_1,text='Submit',command=save)
    btq.pack()

def hgscore():

    def sql_connect():
        global db
        db = con.connect(host='localhost',port='3306',user='root',passwd='Qwerty#99')

    def use_database():
        mycursor=db.cursor()
        mycursor.execute('use game')
        db.commit()
    def show_score():
        mycursor=db.cursor()
        mycursor.execute('select score from profiles order by score desc')
        ssw=mycursor.fetchall()
        kkr=''
        for i in ssw:
            kkr+=str(i)
            kkr+='\n'
        window2=Tk()
        Label(window2,text=kkr,font='none 15 bold',fg='red').pack()   
        db.commit()
        
    def main():
        sql_connect()
        use_database()
        show_score()

    if __name__=="__main__":
        main()


def players():
    def sql_connect():
        global db
        db = con.connect(host='localhost',port='3306',user='root',passwd='Qwerty#99')

    def use_database():
        mycursor=db.cursor()
        mycursor.execute('use game')
        db.commit()
    def show_players():
        mycursor=db.cursor()
        mycursor.execute('select name from profiles order by score desc')
        ssw=mycursor.fetchall()
        kkr=''
        for i in ssw:
            kkr+=str(i)
            kkr+='\n'
        window2=Tk()
        Label(window2,text=kkr,font='none 15 bold',fg='red').pack()   
        db.commit()
        
    def mainz():
        sql_connect()
        use_database()
        show_players()

    mainz()

    
        
#variable_to_detect_clicks
click_detector = " "
#variable_to_collector_score

score_collector=0
#function_for_declaring_win
def chk():
    if len(click_detector) >= 16:
        box.showinfo("won", f'Congrats earned{score_collector}Satoshis')
        disable()
        global window_1
        
    else:
        pass
#function_for_buttons_until_fun_16
def fun_1():
    global click_detector
    click_detector += 'a'
    n=random.randint(1,4)
    button_1.config(state='disabled')
    global rst
    global score_collector
    score_collector+=n
    rst=Label(window,text=n,width=5,height=3,bg='gray',fg='black',font='none 15 bold').grid(row=0,column=0)
    if n==0:
        disable()
        box.showinfo('Game over',"Game Over")
    chk()
    score()
def fun_2():
    n_1=random.randint(0,4)
    button_2.config(state='disabled')
    global rst
    global score_collector
    score_collector += n_1
    rst=Label(window,text=n_1,width=5,height=3,bg='gray',fg='black',font='none 15 bold').grid(row=0,column=1)
    if n_1==0:
        disable()
        box.showinfo('Game over',"Game Over")
    global click_detector
    click_detector += 'b'
    chk()
    score()
def fun_3():
    n_2=random.randint(1,4)
    button_3.config(state='disabled')
    global score_collector
    score_collector += n_2
    Label(window,text=n_2,width=5,height=3,bg='gray',fg='black',font='none 15 bold').grid(row=0,column=2)
    if n_2==0:
        disable()
        box.showinfo('Game over',"Game Over")
    global click_detector
    click_detector += 'c'
    chk()
    score()
def fun_4():
    n_3=random.randint(0,4)
    button_4.config(state='disabled')
    global score_collector
    score_collector += n_3
    Label(window,text=n_3,width=5,height=3,bg='gray',fg='black',font='none 15 bold').grid(row=0,column=3)
    if n_3==0:
        disable()
        box.showinfo('Game over',"Game Over")
    global click_detector
    click_detector += 'd'
    chk()
    score()
def fun_5():
    n_4=random.randint(1,4)
    button_5.config(state='disabled')
    global score_collector
    score_collector +=n_4
    Label(window,text=n_4,width=5,height=3,bg='gray',fg='black',font='none 15 bold').grid(row=1,column=0)
    if n_4==0:
        disable()
        box.showinfo('Game over',"Game Over")
    global click_detector
    click_detector += 'e'
    chk()
    score()
def fun_6():
    n_5=random.randint(0,4)
    button_6.config(state='disabled')
    global score_collector
    score_collector += n_5
    Label(window,text=n_5,width=5,height=3,bg='gray',fg='black',font='none 15 bold').grid(row=1,column=1)
    if n_5==0:
        disable()
        box.showinfo('Game over',"Game Over")
    global click_detector
    click_detector += 'f'
    chk()
    score()
def fun_7():
    global n_6
    n_6=random.randint(1,4)
    button_7.config(state='disabled')
    global score_collector
    score_collector += n_6
    Label(window,text=n_6,width=5,height=3,bg='gray',fg='black',font='none 15 bold').grid(row=1,column=2)
    if n_6==0:
        disable()
        box.showinfo('Game over',"Game Over")
    global click_detector
    click_detector += 'g'
    chk()
    score()
def fun_8():
    global n_7
    n_7=random.randint(0,4)
    button_8.config(state='disabled')
    global score_collector
    score_collector +=n_7
    Label(window,text=n_7,width=5,height=3,bg='gray',fg='black',font='none 15 bold').grid(row=1,column=3)
    if n_7==0:
        disable()
        box.showinfo('Game over',"Game Over")
    global click_detector
    click_detector += 'h'
    chk()
    score()
def fun_9():
    global n_8
    n_8=random.randint(1,4)
    button_9.config(state='disabled')
    global score_collector
    score_collector += n_8
    Label(window,text=n_8,width=5,height=3,bg='gray',fg='black',font='none 15 bold').grid(row=2,column=0)
    if n_8==0:
        disable()
        box.showinfo('Game over',"Game Over")
    global click_detector
    click_detector += 'i'
    chk()
    score()
def fun_10():
    global n_9
    n_9=random.randint(0,4)
    button_10.config(state='disabled')
    global score_collector
    score_collector += n_9
    Label(window,text=n_9,width=5,height=3,bg='gray',fg='black',font='none 15 bold').grid(row=2,column=1)
    if n_9==0:
        disable()
        box.showinfo('Game over',"Game Over")
    global click_detector
    click_detector += 'j'
    chk()
    score()
def fun_11():
    global n_10
    n_10=random.randint(1,4)
    global score_collector
    score_collector += n_10
    button_11.config(state='disabled')
    Label(window,text=n_10,width=5,height=3,bg='gray',fg='black',font='none 15 bold').grid(row=2,column=2)
    if n_10==0:
        disable()
        box.showinfo('Game over',"Game Over")
    global click_detector
    click_detector += 'k'
    chk()
    score()
def fun_12():
    global n_11
    n_11=random.randint(1,4)
    button_12.config(state='disabled')
    global score_collector
    score_collector += n_11
    Label(window,text=n_11,width=5,height=3,bg='gray',fg='black',font='none 15 bold').grid(row=2,column=3)
    if n_11==0:
        disable()
        box.showinfo('Game over',"Game Over")
    global click_detector
    click_detector += 'l'
    chk()
    score()
def fun_13():
    global n_12
    n_12=random.randint(1,4)
    button_13.config(state='disabled')
    global score_collector
    score_collector += n_12
    Label(window,text=n_12,width=5,height=3,bg='gray',fg='black',font='none 15 bold').grid(row=3,column=0)
    if n_12==0:
        disable()
        box.showinfo('Game over',"Game Over")
    global click_detector
    click_detector += 'm'
    chk()
    score()
def fun_14():
    global n_13
    n_13=random.randint(0,4)
    button_14.config(state='disabled')
    global score_collector
    score_collector += n_13
    Label(window,text=n_13,width=5,height=3,bg='gray',fg='black',font='none 15 bold').grid(row=3,column=1)
    if n_13==0:
        disable()
        box.showinfo('Game over',"Game Over")
    global click_detector
    click_detector += 'n'
    chk()
    score()
def fun_15():
    global n_14
    n_14=random.randint(1,4)
    button_15.config(state='disabled')
    global score_collector
    score_collector += n_14
    Label(window,text=n_14,width=5,height=3,bg='gray',fg='black',font='none 15 bold').grid(row=3,column=2)
    if n_14==0:
        disable()
        box.showinfo('Game over',"Game Over")
    global click_detector
    click_detector += '0'
    chk()
    score()
def fun_16():
    global n_15
    n_15=random.randint(0,4)
    button_16.config(state='disabled')
    global score_collector
    score_collector += n_15
    Label(window,text=n_15,width=5,height=3,bg='gray',fg='black',font='none 15 bold').grid(row=3,column=3)
    if n_15==0:
        disable()
        box.showinfo('Game over',"Game Over")
    global click_detector
    click_detector += 'p'
    chk()
    score()

#main_menu

file=Menu(window)
hiscr=Menu(file,tearoff=0)

hiscr.add_command(label='HighScores',command=hgscore)
hiscr.add_command(label='Players',command=players)
hiscr.add_command(label='Exit',command=exit)

file.add_cascade(label='File',menu=hiscr)

window.config(menu=file)

#buttons_for_the_game
button_1=Button(window,width=10,height=5,bg='skyblue',state='normal',command=fun_1)
button_1.grid(row=0,column=0)
button_2=Button(window,width=10,height=5,bg='crimson',state='normal',command=fun_2)
button_2.grid(row=0,column=1)
button_3=Button(window,width=10,height=5,bg='green',state='normal',command=fun_3)
button_3.grid(row=0,column=2)
button_4=Button(window,width=10,height=5,bg='orange',state='normal',command=fun_4)
button_4.grid(row=0,column=3)
button_5=Button(window,width=10,height=5,bg='yellow',state='normal',command=fun_5)
button_5.grid(row=1,column=0)
button_6=Button(window,width=10,height=5,bg='violet',state='normal',command=fun_6)
button_6.grid(row=1,column=1)
button_7=Button(window,width=10,height=5,bg='pink',state='normal',command=fun_7)
button_7.grid(row=1,column=2)
button_8=Button(window,width=10,height=5,bg='maroon',state='normal',command=fun_8)
button_8.grid(row=1,column=3)
button_9=Button(window,width=10,height=5,bg='purple',state='normal',command=fun_9)
button_9.grid(row=2,column=0)
button_10=Button(window,width=10,height=5,bg='red',state='normal',command=fun_10)
button_10.grid(row=2,column=1)
button_11=Button(window,width=10,height=5,bg='gold',state='normal',command=fun_11)
button_11.grid(row=2,column=2)
button_12=Button(window,width=10,height=5,bg='lime',state='normal',command=fun_12)
button_12.grid(row=2,column=3)
button_13=Button(window,width=10,height=5,bg='fuchsia',state='normal',command=fun_13)
button_13.grid(row=3,column=0)
button_14=Button(window,width=10,height=5,bg='olive',state='normal',command=fun_14)
button_14.grid(row=3,column=1)
button_15=Button(window,width=10,height=5,bg='navy',state='normal',command=fun_15)
button_15.grid(row=3,column=2)
button_16=Button(window,width=10,height=5,bg='teal',state='normal',command=fun_16)
button_16.grid(row=3,column=3)
#label_for_displaying_score_title
scr=Label(window,text='Your score is ',fg='black',font='none 12 bold')
scr.grid(row=4,column=0,columnspan=2,padx=20,pady=20)
#credits
Label(window,text='5 Square Tech',font='none 15 bold',bg='blue',fg='white').grid(row=5,column=0,columnspan=2,padx=0,pady=15,sticky=W)
window.mainloop()

