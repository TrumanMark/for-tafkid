from pty import CHILD
from tokenize import Pointfloat

#====Flags======



#====Прогресивный налог======

Chistaya = int(input('Введите чистую прибль: '))
Point = float(input('Ведите свое кол-во очков: '))
dataSS = [0, 75960, 108960, 174960, 243120, 505920, 651600, 100000000]
prozentDataS = [0, 0.1, 0.14, 0.2, 0.31, 0.35, 0.47, 0.5 ]
ficstNalogmasiv = [0, 7596, 12216, 25416, 46546, 138526, 206995, 0]
Ficst = 2628 

a

#=====Бетох=======

esekmas = [0, 75972, 528240, 1000000]
esekproz = [0 ,0.0597, 0.1783, 0]
esekdata = [0,4536, 85175]

#=====================
for i in range (8): 
    if Chistaya < dataSS[i] :
        SS = Chistaya - dataSS [i-1] # разница между чистой и нижней границей 
        SS = SS * prozentDataS[i] # налог разницы
        ficstNalog = ficstNalogmasiv [i-1]
        SS += ficstNalog 
        Ficst *= Point
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



















#=====ВВывод=====

b = int(input ('Выберете 1-Вывести всю информацию 2-Настроить вывод'))
a = [0, 0, 0, 0, 0]
if b == 1 :
    print ('Прогрессивный налог: ',round(Nalog1))
    print ('Бетох люми : ', round(SP))
    print ('Общий налог: ', round(SP + Nalog1))
    print ('В корман: ', round(Vkormn))
    print ('Процент положенный в корман: ', round(Vkormn/Chistaya * 100, 2),'%')
elif b == 2:
    print ('Прогрессивный налог 1-Да 2-Нет')
    a[0] = int(input())
    print ('Бетох люми 1-Да 2-Нет')
    a[1] = int(input())
    print ('Общий налог1-Да 2-Нет')
    a[2] = int(input())
    print ('В корман: 1-Да 2-Нет')
    a[3] = int(input())
    print ('Процент положенй в корман 1-Да 2-Нет ')
    a[4] = int(input())
if a[0] == 1 :
    print ('Прогрессивный налог: ',round(Nalog1))
if a[1] == 1 :
    print ('Бетох люми : ', round(SP))
if a[2] == 1 :
    print ('Общий налог: ', round(SP + Nalog1))
if a[3] == 1 :
    print ('В корман: 1-Да 2-Нет')
if a[4] ==1 :
    print ('Процент положенный в корман: ', round(Vkormn/Chistaya * 100, 2),'%')

print ( 'Cпасибо за использование')








