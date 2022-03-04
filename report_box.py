##############################################
# This module opens a dialog window
##############################################
# import threading
# import time
from tkinter import SW
from tkinter import Tk
# from defaultModule import default_wbd_ as _default_wbd_
try:
    import Tkinter
except ImportError:
    import tkinter

msg_root_: Tk


def close_window():
    msg_root_.destroy()
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'
          'Report had been shown.\n\n'
          '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')


def dia_box_(report_):
    # from app import display_Console
    # display_Console.print_console()
    global msg_wn_, msg_root_
    wn_wdt: int = 400
    wn_hgt: int = 200
    lbl_txt_: str = '\n\n\n' + report_ + '\n\n\n'

    msg_wn_.title("Test Report")
    msg_root_.transient()
    msg_root_.geometry('400x200')
    msg_wn_.configure(bg='#120f6b')
    # msg_root_.focus()
    msg_root_.attributes('-topmost', True)
    msg_root_.update_idletasks()
    msg_root_.withdraw()

    cvs_wn_ = tkinter.Canvas(msg_wn_, width=wn_wdt, height=wn_hgt, bg="#ff6600", bd=0, relief="ridge")
    cvs_wn_.create_text(140, 80, width=260, fill='#ffffff', font='Helvetica 9 italic bold', text=lbl_txt_)
    cvs_wn_.grid(column=0, row=0, columnspan=2, rowspan=2)

    btn_ = tkinter.Button(msg_wn_, text="Close", bg="black", fg="#ffffff",
                           font='Helvetica 8 bold', command=close_window)
    btn_.place(x=245, y=175, anchor=SW, width=125, height=40)

    msg_root_.mainloop()

    return lbl_txt_
