#Превое приложение
```
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Первое приложение")
root.geometry("500x300")

text1 = ttk.Label(text="из")
text1.place(relx=0.1,rely=0.11)

text2 = ttk.Label(text="в")
text2.place(relx=0.5,rely=0.1)

metrics = ["Миллиметры", "Сантиметры", "Дециметры", "Метры", "Киллометры"]

items2 = ttk.Combobox(values=metrics)
items2.place(relx=0.6, rely=0.1, width=150, height=30)


items1 = ttk.Combobox(values=metrics)
items1.place(relx=0.15, rely=0.1, width=150, height=30)



root.mainloop()
```