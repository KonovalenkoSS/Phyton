from time import sleep

class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']
    def running(self):
        i = 0
        while i < 6:
            print(f'Светофор переключается - {TrafficLight.__color[i]}')
            if i == 0:
                sleep(3)
            elif i == 1:
                sleep(1)
            elif i == 2:
                sleep(3)

            i += 1

TrafficLight = TrafficLight()
TrafficLight.running()