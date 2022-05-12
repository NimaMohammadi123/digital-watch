import tkinter as tk 
from datetime import datetime


window = tk.Tk()

window.title("clock")

window.minsize(200,80)

frm =tk.Frame(master=window)

def clock():
    hours_lbl["text"] = clock_format(datetime.now().hour)
    minuts_lbl["text"] = clock_format(datetime.now().minute)
    seconds_lbl["text"] = clock_format(datetime.now().second)
    window.after(1000,clock)
    
def clock_format(num):
    if num<10:
        return f"0{num}"
    else:
        return num    
font_style = (None , 20,"bold")

hours_lbl =tk.Label(master=frm , text="00"  , font=font_style)
minuts_lbl =tk.Label(master=frm , text="00", font=font_style)
seconds_lbl =tk.Label(master=frm , text="00", font=font_style)

hours_lbl.grid(row=0 , column=0 )
minuts_lbl.grid(row=0 , column=1 )
seconds_lbl.grid(row=0 , column=2 )

frm.pack()
clock()

window.mainloop()