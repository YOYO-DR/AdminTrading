from tkinter import *
w=Tk()
w.geometry("300x500")
w.configure(bg='#141414')
def bttn(x,y,text,bcolor,fcolor):
  
  def on_enter(event):
    myButton['background'] = bcolor
    myButton['foreground'] = fcolor
  def on_leave(event):
    myButton['background'] = fcolor
    myButton['foreground'] = bcolor
  def cmd():
    print(f'Tu cliqueaste {text}')

  myButton=Button(w,width=42,height=2,text=text,
                  fg=bcolor,
                  bg=fcolor,
                  border=0,
                  activeforeground=fcolor,
                  activebackground=bcolor,
                  command=cmd)
  
  myButton.bind("<Enter>", on_enter)
  myButton.bind("<Leave>", on_leave)

  myButton.pack(anchor='center',ipady=5)
  #myButton.place(x=0,y=0)

bttn(0,0,"A C E R",'#ffcc66','#141414')
bttn(0,0,"A P P L E",'#25dae9','#141414')
bttn(0,0,"D E L L",'#f86263','#141414')
bttn(0,0,"A S U S",'#ffa157','#141414')
w.mainloop()