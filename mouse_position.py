# coding:utf-8

import time
import tkinter
import pyautogui


def confirm():
    tk.destroy()


tk = tkinter.Tk(className='鼠标实时位置')
# tk['height'] = 200
# tk['width'] = 200
tk.geometry('350x100+50+50')
text = tkinter.Text()
text['height'] = 3
text['width'] = 20
text.pack()
button = tkinter.Button(master=tk, text='确定', command=confirm)
button['height'] = 2
button['width'] = 10
button.pack()

while 1:
    text.delete(1.0, 'end')
    x, y = pyautogui.position()
    position_str = f"X: {str(x).rjust(4)} Y: {str(y).rjust(4)}"
    text.insert('insert', f'\n{position_str}\n')
    tk.update()
    time.sleep(0.15)

# print(tk.winfo_width(), tk.winfo_height())

# tk.mainloop()
# t = threading.Thread(target=loop(tk))
# t.start()
# tk.mainloop()
