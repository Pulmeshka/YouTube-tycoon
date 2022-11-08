from pywebio.output import *
from pywebio.input import *
import random
import time
from pywebio import start_server

def main():
    put_text('Бокс действий')
    box = output()
    put_scrollable(box, height=300)
    sub = 10
    video = 0
    chanel_name = input('Введите название вашего канала')
    while True:
        comand = select('Выберете команду', ['запись', 'статистика'])
        if comand == 'запись':
            box.append('идёт запись видео, ожидайте 10 секунд')
            time.sleep(10)
            add_sub =  random.randint(1, sub)
            sub = sub + add_sub
            video = video + 1
            box.append(f'Видео успешно записано и было опубликовано, новых подписчиков- {add_sub}')
        elif comand == 'статистика':
            box.append(f'статистика- {chanel_name}\nподписчики- {sub}\nвсего видео- {video}')
        else:
            toast('Error server')
start_server(main, port=8080, debug=True)