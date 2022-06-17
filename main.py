from tkinter import *
import time

text_length = 0

def start_typing():
    disappear_text(120)

def disappear_text(time):
    global text_length
    if time >= 0:
        text = typing_area.get("1.0", 'end-1c')
        length = len(text)
        if length > text_length:
            text_length = length
        else:
            typing_area.delete('1.0', END)
    else:
        typing_area.delete('1.0', END)
    window.after(5000, disappear_text, time-1)



window = Tk()
window.geometry('900x550')
window.config(bg='#34B3F1', pady=40, padx=40)
window.title("Disappearing Text")

start = Button(text='Start ▶', width=15, height=2, background="#F15412", font=("Courier", 15, 'bold'), command=start_typing)
start.grid(row=1, column=0)
start.focus()

type_area_label = Label(text='Type Here', bg='#34B3F1', font=("Courier", 20, 'bold'))
type_area_label.grid(row=1, column=1)

typing_area = Text(padx=10, pady=10, background="#EEEEEE", height=8, font=("Courier", 13, 'bold'))
typing_area.grid(row=2, column=0, columnspan=3)

window.mainloop()