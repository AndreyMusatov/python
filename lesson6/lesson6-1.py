from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i < 10: #для ограничения цыкла повторений
            print(f'Светофор переключается,\n {TrafficLight.__color[0]}')
            sleep(7)
            print(f'Светофор переключается, \n {TrafficLight.__color[1]}')
            sleep(2)
            print(f'Светофор переключается, \n {TrafficLight.__color[2]}')
            sleep(7)
            print(f'Светофор переключается, \n {TrafficLight.__color[1]}')
            sleep(2)
        i += 1


TrafficLight = TrafficLight()
TrafficLight.running()
