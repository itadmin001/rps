from tkinter import *
from PIL import Image, ImageTk

win=Tk()
win.geometry("820x450")
win.title("Welcome to Rock Paper Scissors!")

ico = Image.open('rps/rps-ico-64.png')
photo = ImageTk.PhotoImage(ico)
win.wm_iconphoto(False, photo)

win_frame = Frame(win)
win_frame.pack()

rk = Image.open('rps/rock.png')
pp = Image.open('rps/paper.png')
sc = Image.open('rps/scissors.png')

win_frame.columnconfigure(0,weight=1,minsize=136)
win_frame.columnconfigure(1,weight=1)
win_frame.columnconfigure(2,weight=1,minsize=136)
win_frame.rowconfigure(2,weight=1)

main_display = Label(win_frame,width=100,height=7,anchor='center',background="#ddd",font=('arial','20','bold'),text="Starting Text")
main_display.grid(row=1,column=1,padx=10,pady=10)

paper = ImageTk.PhotoImage(pp)
paper_label = Label(win,image=paper)
paper_label.place(relx=0.44,rely=.90,anchor='center')

scissors = ImageTk.PhotoImage(sc)
scissors_label = Label(win,image=scissors)
scissors_label.place(relx=0.57,rely=.89,anchor='center')

rock = ImageTk.PhotoImage(rk)
roc_label = Label(win,image=rock)
roc_label.place(relx=0.5,rely=.70,anchor='center')

win.mainloop()