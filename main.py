import tkinter as tk
from tkinter import ttk

d = {1: ['январь', 'октябрь'], 2: ['май'], 3: ['август'], 4: ['февраль', 'март', 'ноябрь'], 5: ['июнь'],
     6: ['декабрь', 'сентябрь'], 0: ['апрель', 'июль']}

days_in_week = {0: ['суббота'], 1: ['воскресенье'], 2: ['понедельник'], 3: ['вторник'], 4: ['среда'], 5: ['четверг'],
                6: ['пятница']}


def cdsk():
    aa = int(combo.get())
    bb = combo2.get()
    for i, j in d.items():
        if bb in j:
            bb = i
            break
    cc = int(combo3.get()[2:])
    dd = (6 + cc + cc // 4) % 7
    for k, l in days_in_week.items():

        if k == (aa + bb + dd) % 7:
            day['text'] = l


win = tk.Tk()
win.geometry('450x400+100+100')
win.config(bg='white')
days = [i for i in range(1, 32)]
combo = ttk.Combobox(win, value=days)
combo.current(0)
combo.pack()

months = (
'январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь')
combo2 = ttk.Combobox(win, value=months)
combo2.current(0)
combo2.pack()

arr = [i for i in range(1800, 2025)]
combo3 = ttk.Combobox(win, value=arr)
combo3.current(0)
combo3.pack()

tk.Button(win, text='Определить день недели', fg='red', command=cdsk).pack()
day = tk.Label(win, text='')
day.pack()

win.mainloop()
