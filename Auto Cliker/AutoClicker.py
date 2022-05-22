import pyautogui as pg
import keyboard
from time import sleep

on = [False]

def _buttons():
    return pg.confirm('Какая кнопка мыши?', 'Найстроки', ['Левая', 'Правая'])
def _clicks():
    int_ = pg.confirm('Сколько клинов в 0.1 секунд?:', 'Найстроки', ['1','2','5','10','25','50','75','100','200','300','400','500','1000','5000','10000'])
    return int(int_)

def AutoClicker(x, y, _button, _cliks):
    pg.click(x, y, _cliks, button=_button)
    if keyboard.is_pressed(']'):
        print('Авто кликер отключен!')
        on[0] = False
        sleep(1)

_button = _buttons()
_click = _clicks()
print('Для включения авто-кликер нажмите на кнопку [, для выключения ]')
while True:
    if keyboard.is_pressed('['):
        if _button == 'Левая':
            _button = 'left'
        elif _button == 'Правая':
            _button = 'right'
        print('Авто кликер роботает!')
        on[0] = True
        while on[0]:
            AutoClicker(pg.position()[0],pg.position()[1], _button, _click)
    elif keyboard.is_pressed(']'):
        on[0] = False
        print('Авто кликер закрыт!')
        break
   