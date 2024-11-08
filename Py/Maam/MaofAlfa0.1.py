from ctypes import pointer
from logging import root
from tkinter import *
from pty import CHILD
from tokenize import Pointfloat
from turtle import width
from tkinter.ttk import Combobox

#====Прогресивный налог======

dataSS = [0, 75960, 108960, 174960, 243120, 505920, 651600, 100000000]
prozentDataS = [0, 0.1, 0.14, 0.2, 0.31, 0.35, 0.47, 0.5 ]
ficstNalogmasiv = [0, 7596, 12216, 25416, 46546, 138526, 206995, 0]


#=====Бетох=======

esekmas = [0, 75972, 528240, 1000000]
esekproz = [0 ,0.0597, 0.1783, 0]
esekdata = [0,4536, 85175]

#=====================


def clicked():
    AAA = Pribl.get()
    BBB = Pointer.get()
    Chistaya = int(AAA)
    Point = float(BBB)
    Ficst = 2628 
    for i in range (8): 
        if Chistaya < dataSS[i] :
            SS = Chistaya - dataSS [i-1] # разница между чистой и нижней границей 
            SS = SS * prozentDataS[i] # налог разницы
            ficstNalog = ficstNalogmasiv [i-1]
            SS += ficstNalog 
            Ficst = Ficst * Point
            Nalog1 = SS - Ficst
            if Nalog1 < 0:
                Nalog1 = 0
            break

    for i in range (4):
        if Chistaya < esekmas[i]:
            SP = Chistaya - esekmas[i - 1]
            SP *= esekproz [i] 
            SP = SP + esekdata[i-1]
            break

    Vkormn = Chistaya - (SP + Nalog1)
    
    

    Maof.configure( text=round(Vkormn))

#=======Расчет налогов 


root = Tk()

#=======Настроки Окна=======

root['bg'] = '#BEBEBE'  #цвет фона
root.title('Расячет налогов') # Название проги 
#root.wm_attributes('-alpha', 0.99) # прозрачность окна 
root.geometry('400x400') #размер окна 
#root.resizable(width=False, height = False) # рамеры окна которые моджно двигать 

#=======Тело Оформление=======

Ppribl = Label(root, text="Ведите чистую прибль          ", font=(" Helvetica ", 19)) 
Ppribl.grid(column=1, row=1)
Ppointer = Label(root, text="Ведите очки личной скидки", font=(" Helvetica ", 19)) 
Ppointer.grid(column=1, row=2)  

Maof = Label(root, text="0", font=(" Helvetica ", 19)) 
Maof.grid(column=1, row=10)                    

btn = Button(root, text="Рассчитать", command=clicked) 
btn.grid(column=1, row=9)
combo = Combobox(root)


Pribl = Entry(root, width=10)
Pribl.grid(column=2, row=1)
Pointer = Entry(root, width=10)
Pointer.grid(column=2, row=2)



#=======Обязательный Блок=======
Pribl.focus()
root.mainloop()
