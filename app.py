from COPART import Copart
from IAAI import Iaai
from MANHEIM import ManheimDataCar

from threading import Thread

class Main:

    def __init__(self, id_user, car_name, from_year):
        self.id = id_user
        self.car = car_name
        self.from_year = from_year


    def start(self):
        copart = Copart(self.id, self.car, self.from_year)
        iaai = Iaai(self.id, self.car, self.from_year)
        manhaim = ManheimDataCar(self.id, self.car)

        t1 = Thread(target=copart.write_info_car_copart, args=())
        t2 = Thread(target=iaai.iaai, args=())
        t3 = Thread(target=manhaim.manhaim, args=())

        t1.start()
        t2.start()
        t3.start()


if __name__ == '__main__':
    main = Main(2, 'toyota camry', 2010)
    main.start()



