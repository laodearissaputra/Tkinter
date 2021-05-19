from tkinter import *
import time
import os

root = Tk()
root.title('Bithealth')

frameCnt = 12
frames = [PhotoImage(file='thankyou.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(100, update, ind)
label = Label(root)
label.pack()
root.after(0, update, 0)
Button(root, text="Exit", command=root.destroy).pack()
root.mainloop()