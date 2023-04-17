#python_GUI_project
#Programmers_calculator
#5_Square
#Muhammed_Zabiullah_Khan
#imported_necessary_tkinter_modules
import tkinter.messagebox as box
from tkinter import*
import mysql.connector as con
#imported_math_module
from math import*
#assinging_in_tkinter_to_window_variable
window=Tk()
#setting_window_title_&_geomtry_&_background_color
window.title('calculator')
window.geometry('550x550')

window.config(background='blue',borderwidth=10,relief=RIDGE)
#defining_function_to_on_button_for_switch_on_the_calculator
def switch_on():
    global dx
    dx = [button_1, button_2, button_3, button_4,button_5, button_5, button_6,
    button_7, button_8,
    button_9, button_switch, button_0, button_bin, button_char, button_div,
    button_equals,
    button_fac, button_cos, button_hex, button_info, button_minus,
    button_point, button_plus,
    button_mul, button_reset, button_save, button_sin, button_sqr,
    button_switch_off, button_tan]
    dislay.config(bg='yellow')
    for i in dx:
        i.config(state='normal')
#defining_function_for_off_button_to_switch_off_the_calculator
def switch_offz():
    global dx
    dislay.config(bg='black')
    reset()
    for j in dx:
        if j==button_switch:
            j.config(state='normal')
        else:
            j.config(state='disabled')
#created_a_string_var_to_store_values_of_buttons
collector=''
#defining_function_to_collect_values_of_buttons_and_passing_to_var_collector
#and_also_to_display_on_gui_calculator_screen
def collect(num):
    global collector
    collector += str(num)
    dislay.config(text=collector)
#function_to_eval_collected_values_using_eval()_builtin_function
def eql():
    global collector
    collector = eval(str(collector))
    dislay.config(text=collector,fg='red')
#functions_to_pass_values_to_collect
def one():
    collect(b_1)
def two():
    collect(b_2)
def three():
    collect(bt_3)
def four():
    collect(bt_4)
def five():
    collect(bt_5)
def six():
    collect(bt_6)
def seven():
    collect(bt_7)
def eight():
    collect(bt_8)
def nine():
    collect(bt_9)
def zero():
    collect(bt_0)
def add():
    collect(plus)
def minz():
    collect(bt_min)
def divz():
    collect(bt_div)
def mul():
    collect(bt_mul)
#function_to_find_sin_cos_tan_char_fact_bin_hex_isqrt_with_exception_error_handling
def sinz():
    global collector
    try:
        collector=eval('sin(int(collector))')
        dislay.config(text="%0f"%collector)
    except:
        dislay.config(text='impossible')
    finally:
        collector = str(collector)
def cosz():
    global collector
    try:
        collector = eval('cos(int(collector))')
        dislay.config(text="%0f" % collector)
    except:
        dislay.config(text='impossible')
    finally:
        collector = str(collector)
def binz():
    global collector
    try:
        collector = eval('bin(int(collector))')
        dislay.config(text=collector)
    except:
        dislay.config(text='impossible')
    finally:
        collector = str(collector)
def tanz():
    global collector
    try:
        collector = eval('tan(int(collector))')
        dislay.config(text=collector)
    except:
        dislay.config(text='impossible')
    finally:
        collector = str(collector)
def hexzo(n):
    alfa = ['A', 'B', 'C', 'D', 'E', 'F']
    num = []
    for i in range(17):
        if i % 10 == 0 and i > 0:
            for j in alfa:
                num.append(j)
                num.append(i)
        else:
            num.append(i)
            rem = []
            vvr = ''
    while n > 0:
        a = n % 16
        n = n // 16
        rem.append(a)
    for sq in rem:
        vvr += str(num[sq])
        result = vvr[::-1]
        return result
def hexz():
    global collector
    try:
        collector = eval('hexzo(int(collector))')
        dislay.config(text=collector)
    except:
        dislay.config(text='impossible')
    finally:
        collector = str(collector)
def sqrz():
    global collector
    try:
        collector = eval('isqrt(int(collector))')
        dislay.config(text=collector)
    except:
        dislay.config(text='impossible')
    finally:
        collector = str(collector)
def fact(z):
    if z==1:
        return z
    else:
        return z*(fact(z-1))
def facz():
    global collector
    try:
        collector = eval('fact(int(collector))')
        dislay.config(text=collector)
    except:
        dislay.config(text='impossible')
    finally:
        collector = str(collector)
def charz():
    global collector
    try:
        collector = eval('chr(int(collector))')
        dislay.config(text=collector)
    except:
        dislay.config(text='impossible')
    finally:
        collector = str(collector)
#function_to_pass_point_value_to_collect_function
def pointz():
    collect(bt_point)
#function_to_save_answer_in_a_text_file_with_exception_error_handling
def savez():
    global collector
    def sql_connect():
        global db
        db=con.connect(host="localhost",port="3306",user="root",
                       passwd="Qwerty#99")
        print("database connected")
    def create_database():
        cur=db.cursor()
        cur.execute('create database if not exists calculator')
        db.commit()
    def use_database():
        cur=db.cursor()
        cur.execute('use calculator')
        db.commit()

    def create_table():
        cur=db.cursor()
        cur.execute('create table if not exists entries(ans varchar(20))')
        db.commit()
    def insert_data():
        cur=db.cursor()
        cur.execute('insert into entries(ans) value("{}")'.format(collector) )
        db.commit()
    def show_message():
        box.showinfo('Svsql','saved')

    def main():
        sql_connect()
        create_database()
        use_database()
        create_table()
        insert_data()
        show_message()
    main()
    
        
#function_to_display_dev_info
def infoz():
    dislay.config(text='5_Square @Zabi',fg='blue')
#function_to_reset_calculator
def reset():
    global collector
    collector=""
    collect(collector)
#heading_of_the_calculator
h_1=Label(window,text='Programmers Calculator',width=27,font='elephant 15 bold',fg='white',bg='blue')
h_1.grid(row=0,column=0,columnspan=20)
#display_of_the_calculator_packed_in_frame
f_1=Frame(window,borderwidth=1,height=1,relief=SUNKEN,bg='white')
f_1.grid(row=1,column=0,columnspan=10,pady=10)
dislay=Label(f_1,bg='black',width=19,height=2,font='none 20 bold',fg='black',borderwidth=3,relief=SUNKEN)
dislay.grid()
#buttons_of_the_calculator_with_values_storing_var
b_1=1
button_1=Button(window,text=b_1,width=4,height=1,state='disabled',font='none 15 bold',fg='black',borderwidth=3,relief=RAISED,command=one)
button_1.grid(row=2,column=0,pady=5,padx=2)
b_2=2
button_2=Button(window,text=b_2,width=4,height=1,state='disabled',font='none 15 bold',fg='black',borderwidth=3,relief=RAISED,command=two)
button_2.grid(row=2,column=1,padx=2)
bt_3=3
button_3=Button(window,text=bt_3,width=4,height=1,state='disabled',font='none 15 bold',fg='black',borderwidth=3,relief=RAISED,command=three)
button_3.grid(row=2,column=2,padx=2)
b_rst='Rst'
button_reset=Button(window,text=b_rst,width=3,state='disabled',height=1,font='none 15 bold',fg='black',bg='skyblue',borderwidth=3,relief=RAISED,command=reset)
button_reset.grid(row=2,column=3,padx=2)
button_info=Button(window,text='i',width=3,height=1,state='disabled',font='none 15 bold',fg='black',bg='skyblue',borderwidth=3,relief=RAISED,command=infoz)
button_info.grid(row=2,column=4,padx=2)
button_switch=Button(window,text='ON',width=3,height=1,font='none 15 bold',fg='white',bg='green',borderwidth=3,relief=RAISED,command=switch_on)
button_switch.grid(row=2,column=5,padx=10)
bt_4=4
button_4=Button(window,text=bt_4,width=4,height=1,state='disabled',font='none 15 bold',fg='black',borderwidth=3,relief=RAISED,command=four)
button_4.grid(row=3,column=0,pady=5,padx=2)
bt_5=5
button_5=Button(window,text=bt_5,width=4,height=1,state='disabled',font='none 15 bold',fg='black',borderwidth=3,relief=RAISED,command=five)
button_5.grid(row=3,column=1,padx=2)
bt_6=6
button_6=Button(window,text=bt_6,width=4,height=1,state='disabled',font='none 15 bold',fg='black',borderwidth=3,relief=RAISED,command=six)
button_6.grid(row=3,column=2,padx=2)
bt_sin='Sin'
button_sin=Button(window,text=bt_sin,width=3,height=1,state='disabled',font='none 15 bold',fg='black',bg='skyblue',borderwidth=3,relief=RAISED,command=sinz)
button_sin.grid(row=3,column=3,padx=2)
bt_cos='Cos'
button_cos=Button(window,text='Cos',width=3,height=1,state='disabled',font='none 15 bold',fg='black',bg='skyblue',borderwidth=3,relief=RAISED,command=cosz)
button_cos.grid(row=3,column=4,padx=2)
button_switch_off=Button(window,text='OFF',width=3,height=1,state='disabled',font='none 15 bold',fg='white',bg='red',borderwidth=3,relief=RAISED,command=switch_offz)
button_switch_off.grid(row=3,column=5,padx=10)
bt_7=7
button_7=Button(window,text=bt_7,width=4,height=1,state='disabled',font='none 15 bold',fg='black',borderwidth=3,relief=RAISED,command=seven)
button_7.grid(row=4,column=0,pady=5,padx=2)
bt_8=8
button_8=Button(window,text=bt_8,width=4,height=1,state='disabled',font='none 15 bold',fg='black',borderwidth=3,relief=RAISED,command=eight)
button_8.grid(row=4,column=1,padx=2)
bt_9=9
button_9=Button(window,text=bt_9,width=4,height=1,state='disabled',font='none 15 bold',fg='black',borderwidth=3,relief=RAISED,command=nine)
button_9.grid(row=4,column=2,padx=2)
bt_0=0
button_0=Button(window,text=bt_0,width=3,height=1,state='disabled',font='none 15 bold',fg='black',bg='skyblue',borderwidth=3,relief=RAISED,command=zero)
button_0.grid(row=4,column=3,padx=2)
bt_bin='Bin'
button_bin=Button(window,text=bt_bin,width=3,height=1,state='disabled',font='none 15 bold',fg='black',bg='skyblue',borderwidth=3,relief=RAISED,command=binz)
button_bin.grid(row=4,column=4,padx=2)
bt_tan='Tan'
button_tan=Button(window,text=bt_tan,width=3,height=1,state='disabled',font='none 15 bold',fg='black',bg='skyblue',borderwidth=3,relief=RAISED,command=tanz)
button_tan.grid(row=4,column=5,padx=10)
plus='+'
button_plus=Button(window,text=plus,width=4,height=1,state='disabled',font='none 15 bold',fg='black',bg='skyblue',borderwidth=3,relief=RAISED,command=add)
button_plus.grid(row=5,column=0,pady=5,padx=2)
bt_min="-"
button_minus=Button(window,text=bt_min,width=4,height=1,state='disabled',font='none 15 bold',fg='black',bg='skyblue',borderwidth=3,relief=RAISED,command=minz)
button_minus.grid(row=5,column=1,padx=2)
bt_mul='*'
button_mul=Button(window,text=bt_mul,width=4,height=1,state='disabled',font='none 15 bold',fg='black',bg='skyblue',borderwidth=3,relief=RAISED,command=mul)
button_mul.grid(row=5,column=2,padx=2)
bt_div='/'
button_div=Button(window,text=bt_div,width=3,height=1,state='disabled',font='none 15 bold',fg='black',bg='skyblue',borderwidth=3,relief=RAISED,command=divz)
button_div.grid(row=5,column=3,padx=2)
button_equals=Button(window,text='=',width=3,height=1,state='disabled',font='none 15 bold',fg='black',bg='skyblue',borderwidth=3,relief=RAISED,command=eql)
button_equals.grid(row=5,column=4,padx=2)
bt_hex='Hex'
button_hex=Button(window,text=bt_hex,width=3,height=1,state='disabled',font='none 15 bold',fg='black',bg='skyblue',borderwidth=3,relief=RAISED,command=hexz)
button_hex.grid(row=5,column=5,padx=10)
bt_point="."
button_point=Button(window,text=bt_point,width=4,height=1,state='disabled',font='none 15 bold',fg='black',bg='skyblue',borderwidth=3,relief=RAISED,command=pointz)
button_point.grid(row=6,column=0,pady=5,padx=2)
bt_sqr='Sqr'
button_sqr=Button(window,text=bt_sqr,width=4,height=1,state='disabled',font='none 15 bold',fg='black',bg='skyblue',borderwidth=3,relief=RAISED,command=sqrz)
button_sqr.grid(row=6,column=1,padx=2)
bt_per='Char'
button_char=Button(window,text=bt_per,width=4,height=1,state='disabled',font='none 15 bold',fg='black',bg='skyblue',borderwidth=3,relief=RAISED,command=charz)
button_char.grid(row=6,column=2,padx=2)
bt_fac='Fac'
button_fac=Button(window,text=bt_fac,width=3,height=1,state='disabled',font='none 15 bold',fg='black',bg='skyblue',borderwidth=3,relief=RAISED,command=facz)
button_fac.grid(row=6,column=3,padx=2)
bt_save='Save'
button_save=Button(window,text=bt_save,width=8,height=1,state='disabled',font='none 15 bold',fg='black',bg='skyblue',borderwidth=3,relief=RAISED,command=savez)
button_save.grid(row=6,column=4,columnspan=2,padx=2,sticky=W)
#end_of_the_program
window.mainloop()
